from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from .models import Device
from django.contrib.auth import authenticate
from django.contrib.auth import login
#from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
import csv,io
from .forms import *
from .models import *
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved user")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            to_email= form.cleaned_data.get('email')
            print(username,raw_password)
            user = authenticate(username=username, password=raw_password)
            send_mail(
                    'Congratulations',
                    'Congratulations you are now registered',
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    fail_silently=False,
)
    else:
        form = SignUpForm()
    return render(request,'newops/signup.html',{'form':form})
def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
        return render(request,'newops/hello.html')
    else:
        form = AuthenticationForm()
        return render(request,'newops/login.html',{'form':form})
def hello(request):
    return render(request,'newops/hello.html')

#API 
class ApplicationDetail(APIView):
   
    def post(self, request):
        
        print(request.data)
        Application.objects.create(app_name = request.data.get('app_name'),app_function = request.data.get('app_function'),app_type = request.data.get('app_type'))
        return redirect('../hello')

def details(request):
    return render(request,'newops/applicationapi.html')


class AssestDetail(APIView):
   
    def post(self, request):
        
        customer_id_list = request.data.getlist('Customer_ID_id')
        app_name_list = request.data.getlist('app_name')
        page_list = request.data.getlist('page_name')
        device_list = request.data.getlist('device_registration_name')
        
            
        for i in range(len(customer_id_list)):
            customer_id_list[i] = Customer.objects.get(company_name=customer_id_list[i])

        obj = AssetGroup.objects.create(assestname = request.data.get('assestname'),Customer_ID = customer_id_list[0])
        for i in range(len(page_list)):
            obj.pagename.add(Pages.objects.filter(page_name=page_list[i]).first())
       
        for i in range(len(device_list)):
            obj.devicename.add(Device.objects.filter(device_registration_name=device_list[i]).first())
            
        for i in range(len(app_name_list)):
            
            obj.appname.add(Application.objects.filter(app_name=app_name_list[i]).first())
        obj.save()
        return redirect('../hello')

def assestdetails(request):
    return render(request,'newops/assestgroupapi.html',{'customerquery':Customer.objects.all(),'appquery':Application.objects.all(),'pagequery':Pages.objects.all(),'devicequery':Device.objects.all()})

class DeviceSpecDetail(APIView):
   
    def post(self, request):
        
        
        DeviceSpecification.objects.create(techSpecificationID = request.data.get('techSpecificationID'),
        techSpecificationName = request.data.get('techSpecificationName'),device_type = request.data.get('device_type'),
        gps=request.data.get('gps'),gsm=request.data.get('gsm'),wifi=request.data.get('wifi'),ble=request.data.get('ble'),
        zigbee=request.data.get('zigbee'),zigwave=request.data.get('zigbee'),rs_232=request.data.get('rs_232'),
        rs_485=request.data.get('rs_485'),rs_422=request.data.get('rs_422'),tcp=request.data.get('tcp'),mqtt=request.data.get('mqtt'),
        http=request.data.get('http'),symetric_key=request.data.get('symetric_key'),x509_Certificate=request.data.get('x509_Certificate'),
        ota=request.data.get('ota'),inputs=request.data.get('inputs'),outputs=request.data.get('outputs'),ethernet=request.data.get('ethernet'),
        analog_input=request.data.get('analog_input'),power_supply=request.data.get('power_supply'),other1=request.data.get('other1'),
        other2=request.data.get('other2'),other3=request.data.get('other3'),security_key=request.data.get('security_key'))
        return redirect('../hello')

def devicespec_details(request):
    return render(request,'newops/devicespecapi.html')

class VendorDetail(APIView):
   
    def post(self, request):
        
        
        Vendor.objects.create(vendor_name=request.data.get('vendor_name'),vendor_address=request.data.get('vendor_address'),
        vendor_city=request.data.get('vendor_city'),vendor_country=request.data.get('vendor_country'),zip_code=request.data.get('zip_code'),
        vendor_contact=request.data.get('vendor_contact'),vendor_email=request.data.get('vendor_email'),web=request.data.get('web'),
        vendor_VAT=request.data.get('vendor_VAT'),vendor_other1=request.data.get('vendor_other1'),vendor_other2=request.data.get('vendor_other2'),
        vendor_other3=request.data.get('vendor_other2'))
        return redirect('../hello')

def vendor_details(request):
    return render(request,'newops/vendorapi.html')


class IAMDetail(APIView):
   
    def post(self, request):
        
        
        Device_IAM_Mechanism.objects.create(IAM=request.data.get('IAM'))
        return redirect('../hello')

def IAM_details(request):
    return render(request,'newops/iamapi.html')

class DPSDetail(APIView):
    def post(self,request):
        DPS_Property.objects.create(dps_name=request.data.get('dps_name'),resourse_type=request.data.get('resourse_type'),
        location=request.data.get('location'),location_ID=request.data.get('location_ID'),resourse_ID=request.data.get('resourse_ID'),
        resourse_group=request.data.get('resourse_group'),resourse_group_id=request.data.get('resourse_group_id'),subscription=request.data.get('subscription'),
        subscription_id=request.data.get('subscription_id'))
        return redirect('../hello')
def DPS_details(request):
    return render(request,'newops/dpsapi.html')  


class usergroupDetail(APIView):
    def post(self,request):
        UserGroup.objects.create(usergroup=request.data.get('usergroup'),superadmin=request.data.get('superadmin'),
        admin=request.data.get('admin'),localadmin=request.data.get('localadmin'),manager=request.data.get('manager'),
        supervisor=request.data.get('supervisor'),operator=request.data.get('operator'),support=request.data.get('support'),
        staff=request.data.get('staff'),other1=request.data.get('other1'),other2=request.data.get('other2'))
        return redirect('../hello') 

def Usergroup_details(request):
    return render(request,'newops/usergroupapi.html')   


class IotDetail(APIView):
    def post(self,request):
        resourse_group_list = request.data.getlist('resourse_group')

        print(resourse_group_list)
        for i in range(len(resourse_group_list)):
            resourse_group_list[i] = DPS_Property.objects.filter(resourse_group=resourse_group_list[i]).first()
        
        IOT_Hub.objects.create(hub_name=request.data.get('hub_name'),hostname=request.data.get('hostname'),status=request.data.get('status'),
        current_location=request.data.get('current_location'),subscription=request.data.get('subscription'),resourse_group=resourse_group_list[0])
        return redirect('../hello') 
def IOT_details(request):
    return render(request,'newops/iotapi.html',{'dpsquery':DPS_Property.objects.all()}) 
   
class CADetail(APIView):
    def post(self,request):
        CA.objects.create(CAtype=request.data.get('CAtype'))
        return redirect('../hello')
def CA_details(request):
    return render(request,'newops/caapi.html') 


class UserTypeDetail(APIView):
    def post(self,request):
        Usertype.objects.create(user_type=request.data.get('user_type'))
        return redirect('../hello')
def Usertype_details(request):
    return render(request,'newops/usertypeapi.html') 


class PermissionDetail(APIView):
    def post(self,request):
        Permissions.objects.create(permission_name=request.data.get('permission_name'),add_permission=request.data.get('add_permission'),
        edit_permission=request.data.get('edit_permission'),modify_permission=request.data.get('modify_permission'),
        view_permission=request.data.get('view_permission'),log_permission=request.data.get('log_permission'),delete_permission=request.data.get('delete_permission'))
        return redirect('../hello')
def Permission_details(request):
    return render(request,'newops/permissionapi.html')  


class CustomerDetail(APIView):
    def post(self,request):
        app_list = request.data.getlist('application')
        print(app_list)
        for i in range(len(app_list)):
            app_list[i] = Application.objects.filter(app_name=app_list[i]).first()
        
        Customer.objects.create(company_name=request.data.get('company_name'),address=request.data.get('address'),city=request.data.get('city'),
        country=request.data.get('country'),zip_code=request.data.get('zip_code'),primary_contact_person=request.data.get('primary_contact_person'),
        designation=request.data.get('designation'),primary_email=request.data.get('primary_email'),secondary_contact_person=request.data.get('secondary_contact_person'),
        s_designation=request.data.get('s_designation'),secondary_email=request.data.get('secondary_email'),website=request.data.get('website'),
        gst=request.data.get('gst'),vat=request.data.get('vat'),installation_mode=request.data.get('installation_mode'),no_of_site=request.data.get('no_of_site'),
        site1=request.data.get('site1'),site2=request.data.get('site2'),site3=request.data.get('site3'),address_site1=request.data.get('address_site1'),
        address_site2=request.data.get('address_site2'),address_site3=request.data.get('address_site3'),city_site1=request.data.get('city_site1'),city_site2=request.data.get('city_site2'),
        city_site3=request.data.get('city_site3'),country_site1=request.data.get('country_site1'),country_site2=request.data.get('country_site2'),country_site3=request.data.get('country_site3'),
        application=app_list[0])
        return redirect('../hello') 
def Customer_details(request):
    return render(request,'newops/customerapi.html',{'appquery':Application.objects.all()}) 

class CertificateDetail(APIView):
    def post(self,request):
        ca_list = request.data.getlist('ca_name')
        device_list = request.data.getlist('assignedTo')
        for i in range(len(ca_list)):
            ca_list[i] = CA.objects.filter(CAtype=ca_list[i]).first()
        for i in range(len(device_list)):
            device_list[i] = Device.objects.filter(Firmware_version=device_list[i]).first()
        
        Certificate.objects.create(certificate_name=request.data.get('certificate_name'),certFile_type=request.data.get('certFile_type'),
        generatedOn=request.data.get('generatedOn'),validity=request.data.get('validity'),uploadedOn=request.data.get('uploadedOn'),assigned=request.data.get('assigned'),
        assignedDate=request.data.get('assignedDate'),assignedTo=device_list[0],ca_name=ca_list[0])
        return redirect('../hello') 
def Certificate_details(request):
    return render(request,'newops/certificateapi.html',{'caquery':CA.objects.all(),'devicequery':Device.objects.all()}) 

class DeviceDetail(APIView):
    def post(self,request):
        iothublist = request.data.getlist('iot_hub_name')
        dpslist = request.data.getlist('dps_property_ID')
        vendorlist = request.data.getlist('vendor')
        customerlist = request.data.getlist('sold_to_customer')
        applist = request.data.getlist('route_to_application')
        devicespeclist = request.data.getlist('device_Specification_ID')
        IAMlist = request.data.getlist('device_IAM_mechanism')
        for i in range(len(iothublist)):
            iothublist[i] = IOT_Hub.objects.get(hub_name=iothublist[i])
        for i in range(len(dpslist)):
            dpslist[i] = DPS_Property.objects.get(dps_name=dpslist[i])
        for i in range(len(vendorlist)):
            vendorlist[i] = Vendor.objects.get(vendor_name=vendorlist[i])
        for i in range(len(customerlist)):
            customerlist[i] = Customer.objects.get(company_name=customerlist[i])
        for i in range(len(applist)):
            applist[i] = Application.objects.get(app_name=applist[i])
        for i in range(len(devicespeclist)):
            devicespeclist[i] = DeviceSpecification.objects.get(device_type=devicespeclist[i])

        obj = Device.objects.create(device_type = request.data.get('device_type'),enrollment_type=request.data.get('enrollment_type'),
        device_registration_name=request.data.get('device_registration_name'),iot_hub_name=iothublist[0],dps_property_ID=dpslist[0],
        allocation_policy=request.data.get('allocation_policy'),secret_storage=request.data.get('secret_storage'),
        operation=request.data.get('operation'),vendor=vendorlist[0],make=request.data.get('make'),model=request.data.get('model'),
        serial_number=request.data.get('serial_number'),date_of_purchase=request.data.get('date_of_purchase'),
        warrenty_period=request.data.get('warrenty_period'),warrenty_expiry=request.data.get('warrenty_expiry'),
        Firmware_version=request.data.get('Firmware_version'),sold_to_customer=customerlist[0],route_to_application=applist[0],configured=request.data.get('configured'),
        device_Specification_ID=devicespeclist[0])


        for i in range(len(IAMlist)):
            
            obj.device_IAM_mechanism.add(Device_IAM_Mechanism.objects.filter(IAM=IAMlist[i]).first())
        obj.save()
        return redirect('../hello')

def devicedetails(request):
    return render(request,'newops/deviceapi.html',{'customerquery':Customer.objects.all(),'appquery':Application.objects.all(),'iotquery':IOT_Hub.objects.all(),'devicequery':Device.objects.all(),
    'vendorquery':Vendor.objects.all(),'IAMquery':Device_IAM_Mechanism.objects.all(),'dpsquery':DPS_Property.objects.all()})

