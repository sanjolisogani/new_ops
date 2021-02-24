from django.db import models
import uuid  # for generating uuid
import datetime
from django.core.validators import MaxValueValidator, RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
COUNTRY = (("IN", "India"), ("US", "USA"), ("CA", "CANADA"),
           ("BE", "Belguim"), ("CZ", "Czechia"), ("DK", "Denmark"), ("DE",
                                                                     "Germany"), ("EE", "Estonia"), ("IE", "Ireland"),
           ("EL", "Greece"), ("ES", "Spain"), ("FR", "France"), ("HR",
                                                                 "Crotia"), ("IT", "Italy"), ("CY", "Cyprus"), ("LV", "Latvia"),
           ("LT", "Lithuania"), ("LU", "Luxembourg"), ("HU", "Hungary"), ("MT", "Malta"), ("NL",
                                                                                           "Netherlands"), ("AT", "Austria"), ("PL", "Poland"), ("PT", "Portugal"),
           ("RO", "Romania"), ("SL", "Slovenia"), ("SK", "Slovakia"), ("FI", "Finland"), ("SW", "Sweden"), ("TH", "Thailand"))
IAM = (("X.509 Certificate", "X.509 Certificate"), ("TPM", "TPM"),
       ("Symetric Key", "Symetric Key"), ("Password", "Password"))
SECRET_STORAGE = (("HSM", "HSM"), ("TSM", "TSM"), ("MEMORY", "MEMORY"))
OPERATION = (("Register", "Register"), ("Reregister",
                                        "Reregister"), ("Delete", "Delete"))
INSTALLATION_MODE = (("Edge", "Edge"), ("Cloud", "Cloud"),
                     ("Hybrid", "Hybrid"), ("Other", "Other"))
SECURITY_KEY_CHOICES = (("HSM", "HSM"), ("TPM", "TPM"))
COUNTRY = (("IN", "India"), ("US", "USA"), ("CA", "CANADA"),
           ("BE", "Belguim"), ("CZ", "Czechia"), ("DK", "Denmark"), ("DE",
                                                                     "Germany"), ("EE", "Estonia"), ("IE", "Ireland"),
           ("EL", "Greece"), ("ES", "Spain"), ("FR", "France"), ("HR",
                                                                 "Crotia"), ("IT", "Italy"), ("CY", "Cyprus"), ("LV", "Latvia"),
           ("LT", "Lithuania"), ("LU", "Luxembourg"), ("HU", "Hungary"), ("MT", "Malta"), ("NL",
                                                                                           "Netherlands"), ("AT", "Austria"), ("PL", "Poland"), ("PT", "Portugal"),
           ("RO", "Romania"), ("SL", "Slovenia"), ("SK", "Slovakia"), ("FI", "Finland"), ("SW", "Sweden"), ("TH", "Thailand"))
ALLOCATION_POLICY = (("1", "Lowest Latency"), ("2", "Weight Distributed"),
                     ("3", "Static Configuration"), ("4", "Custom(azure function)"))
DEVICE_TYPE = (("Edge", "Edge"), ("Hardware Gateway", "Hardware Gateway"), ("Software Gateway",
                                                                            "Software Gateway"), ("Embedded Device", "Embedded Device"), ("Other", "Other"))
ENROLLMENT_TYPE = (("Group", "Group"), ("Individual", "Individual"))
CONFI_TYPE = (("Yes", "Yes"), ("No", "No"))
WARRENTY_PERIOD = (("1", "1"), ("2", "2"), ("3", "3"))
APP_TYPE = (("Source", "Source"), ("End", "End"))
NO_OF_SITES = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
               ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"))
# base model
class BaseModel(models.Model):
    """Base ORM model"""
    # create uuid field
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # created and updated at date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # meta class
    class Meta:
        abstract = True

    # Time elapsed since creation
    def get_seconds_since_creation(self):
        """
        Find how much time has been elapsed since creation, in seconds.
        This function is timezone agnostic, meaning this will work even if
        you have specified a timezone.
        """
        return (datetime.datetime.utcnow() -
                self.created_at.replace(tzinfo=None)).seconds


# User model table
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """A ORM model for Managing User and Authentication"""

    # mobile field
    #mobile = models.BigIntegerField(unique=True,null =True)
    email =  models.EmailField(max_length = 254,unique=True,null = True,blank=True) 
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    user_timezone = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,choices=COUNTRY,null=True,blank=False)
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    user_group = models.ForeignKey('UserGroup',on_delete=models.CASCADE,null=True,blank=True)
    permission_id = models.ForeignKey('Permissions',on_delete=models.CASCADE,null=True,blank=True)
    asset_group = models.ForeignKey('AssetGroup',on_delete=models.CASCADE,null=True,blank=True)
    last_login = models.DateTimeField(null=True,blank=True)
    last_password_change = models.DateTimeField(null=True,blank=True)
    next_password_change = models.DateTimeField(null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    
    # create objs for management
    objects = UserManager()

    # SET email field as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # create a meta class
    class Meta:
        db_table= 'user'

class DeviceSpecification(BaseModel):
    techSpecificationID = models.BigIntegerField(default=1)
    techSpecificationName = models.CharField(
        max_length=100, null=True, blank=True)
    device_type = models.CharField(
        max_length=100, choices=DEVICE_TYPE, null=True, blank=False, default=None)
    gps = models.BooleanField(default=False)
    gsm = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    ble = models.BooleanField(default=False)
    zigbee = models.BooleanField(default=False)
    zigwave = models.BooleanField(default=False)
    rs_232 = models.BooleanField(default=False)
    rs_485 = models.BooleanField(default=False)
    rs_422 = models.BooleanField(default=False)
    tcp = models.BooleanField(default=False)
    mqtt = models.BooleanField(default=False)
    http = models.BooleanField(default=False)
    symetric_key = models.BooleanField(default=False)
    x509_Certificate = models.BooleanField(default=False)
    ota = models.BooleanField(default=False)
    inputs = models.BooleanField(default=False)
    outputs = models.BooleanField(default=False)
    ethernet = models.BooleanField(default=False)
    analog_input = models.BooleanField(default=False)
    power_supply = models.FloatField()
    other1 = models.CharField(max_length=100, null=True, blank=True)
    other2 = models.CharField(max_length=100, null=True, blank=True)
    other3 = models.CharField(max_length=100, null=True, blank=True)
    security_key = models.CharField(
        max_length=100, choices=SECURITY_KEY_CHOICES, null=True, blank=False, default=None)

    def __str__(self):
        return self.techSpecificationName


class Vendor(BaseModel):
    #vendorID = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)
    vendor_address = models.CharField(max_length=100, null=True, blank=True)
    vendor_city = models.CharField(max_length=100, null=True, blank=True)
    vendor_country = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999)])
    vendor_contact = models.CharField(max_length=10, validators=[
                                      RegexValidator(r'^\d{1,10}$')])
    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    web = models.URLField(max_length=100, null=True, blank=True)
    vendor_VAT = models.CharField(max_length=100, null=True, blank=True)
    vendor_other1 = models.CharField(max_length=100, null=True, blank=True)
    vendor_other2 = models.CharField(max_length=100, null=True, blank=True)
    vendor_other3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.vendor_name


class Device_IAM_Mechanism(BaseModel):

    IAM = models.CharField(max_length=100, choices=IAM,
                           null=True, blank=False, default=None)

    def __str__(self):
        return self.IAM


class DPS_Property(BaseModel):
    #dps_ID = models.BigIntegerField()
    dps_name = models.CharField(max_length=100, null=True, blank=True)
    resourse_type = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)
    location_ID = models.CharField(max_length=100, null=True, blank=True)
    resourse_ID = models.CharField(max_length=100, null=True, blank=True)
    resourse_group = models.CharField(max_length=100, null=True, blank=True)
    resourse_group_id = models.CharField(max_length=100, null=True, blank=True)
    subscription = models.CharField(max_length=100, null=True, blank=True)
    subscription_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.dps_name

# class DeviceType(BaseModel):
    # SIR


class IOT_Hub (BaseModel):
    #hub_id = models.CharField(max_length=100)
    hub_name = models.CharField(max_length=100, null=True, blank=True)
    hostname = models.URLField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)
    current_location = models.CharField(max_length=100, null=True, blank=True)
    subscription = models.BooleanField(default=False)
    #subscription_id = uuid
    # pricing_and_scale =
    resourse_group = models.ForeignKey(
        DPS_Property, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.hub_name

class Customer (BaseModel):
    #customer_id = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)
    zip_code = models.CharField(max_length=6, validators=[
                                RegexValidator(r'^\d{1,6}$')])
    primary_contact_person = models.CharField(max_length=10, validators=[
                                              RegexValidator(r'^\d{1,10}$')], null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    primary_email = models.EmailField(max_length=100, null=True, blank=True)
    secondary_contact_person = models.CharField(max_length=10, validators=[
                                                RegexValidator(r'^\d{1,10}$')], null=True, blank=True)
    s_designation = models.CharField(max_length=100, null=True, blank=True)
    secondary_email = models.EmailField(max_length=100, null=True, blank=True)

    website = models.URLField(max_length=100, null=True, blank=True)
    gst = models.CharField(max_length=100, null=True, blank=True)
    vat = models.CharField(max_length=100, null=True, blank=True)
    application = models.ForeignKey(
        'Application', on_delete=models.CASCADE, default='')
    installation_mode = models.CharField(
        max_length=100, null=True, blank=False, default=None, choices=INSTALLATION_MODE)
    no_of_site = models.CharField(
        max_length=100, null=True, blank=False, default=None, choices=NO_OF_SITES)
    site1 = models.CharField(max_length=100, null=True, blank=True)
    address_site1 = models.CharField(max_length=100, null=True, blank=True)
    city_site1 = models.CharField(max_length=100, null=True, blank=True)
    country_site1 = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)
    site2 = models.CharField(max_length=100, null=True, blank=True)
    address_site2 = models.CharField(max_length=100, null=True, blank=True)
    city_site2 = models.CharField(max_length=100, null=True, blank=True)
    country_site2 = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)
    site3 = models.CharField(max_length=100, null=True, blank=True)
    address_site3 = models.CharField(max_length=100, null=True, blank=True)
    city_site3 = models.CharField(max_length=100, null=True, blank=True)
    country_site3 = models.CharField(
        max_length=100, choices=COUNTRY, null=True, blank=False, default=None)

    def __str__(self):
        return self.company_name


class Application(BaseModel):
    #app_id = models.BigIntegerField()
    app_name = models.CharField(max_length=100, null=True, blank=True)
    app_type = models.CharField(
        max_length=100, choices=APP_TYPE, null=True, blank=False, default=None)
    app_function = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.app_name


class Pages(BaseModel):
    #page_id = models.BigIntegerField(unique=True)
    page_name = models.CharField(max_length=100, null=True, blank=True)
    page_description = models.CharField(max_length=100, null=True, blank=True)
    app_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.page_name


class UserGroup (BaseModel):  # minimum parameters, private parameters
    usergroup = models.CharField(max_length=100, null=True, blank=True)
    superadmin = models.CharField(max_length=100, null=True, blank=True)
    admin = models.CharField(max_length=100, null=True, blank=True)
    localadmin = models.CharField(max_length=100, null=True, blank=True)
    manager = models.CharField(max_length=100, null=True, blank=True)
    supervisor = models.CharField(max_length=100, null=True, blank=True)
    operator = models.CharField(max_length=100, null=True, blank=True)
    support = models.CharField(max_length=100, null=True, blank=True)
    staff = models.CharField(max_length=100, null=True, blank=True)
    other1 = models.CharField(max_length=100, null=True, blank=True)
    other2 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.usergroup


class Permissions(BaseModel):
    TYPE = (('True', 'True'), ('False', 'False'))
    #permission_id = models.CharField(max_length=100)
    permission_name = models.CharField(
        max_length=100, null=True, blank=True, unique=True)

    add_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)
    edit_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)
    modify_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)
    view_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)
    log_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)
    delete_permission = models.CharField(
        max_length=100, choices=TYPE, null=True, blank=False, default=None)

    def __str__(self):
        return self.permission_name


class Usertype(BaseModel):
    UserType = (('Staff', 'Staff'), ('Vendor', 'Vendor'),
                ('Customer', 'Customer'))
    user_type = models.CharField(
        max_length=100, null=True, blank=False, default=None, choices=UserType)

    def __str__(self):
        return self.user_type


class Certificate(BaseModel):
    certificate_name = models.CharField(max_length=100, null=True, blank=True)
    # certificate_type =
    certFile_type = models.BooleanField(default=False)
    #certificate_file = models.FielField()
    generatedOn = models.DateTimeField(null=True, blank=True)
    validity = models.DurationField(null=True, blank=True)
    ca_name = models.ForeignKey(
        'CA', on_delete=models.CASCADE, null=True, blank=False, default='')
   # uploadedBy = models.ForeignKey('User',on_delete=models.CASCADE,null=True,blank=True)
    uploadedOn = models.DateTimeField(null=True, blank=True)
    assigned = models.BooleanField(default=False)
    assignedTo = models.ForeignKey(
        'Device', on_delete=models.CASCADE, null=True, blank=False, default='')
    #assignedBy = models.ForeignKey('User',on_delete=models.CASCADE)
    assignedDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.certificate_name


class CA (BaseModel):
    TYPE_SELECT = (
        ('Self', 'Self'),
        ('CA', 'CA'),
    )
    #CAtype = models.BooleanField(default=False)
    CAtype = models.CharField(
        max_length=100, choices=TYPE_SELECT, blank=False, default=None)

    def __str__(self):
        return self.CAtype


class AssetGroup(BaseModel):
    # SIR
    list1 = []
    assestname = models.CharField(max_length=100, null=True, blank=True)
    Customer_ID = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=False, default='')
    appname = models.ManyToManyField(Application)
    pagename = models.ManyToManyField(Pages)
    devicename = models.ManyToManyField('Device')

    def __str__(self):
        return self.assestname
    # def __str__(self):
    #     app=", ".join(obj.app_name for obj in self.appname.all())
    #     page = ", ".join(obj.page_name for obj in self.pagename.all())
    #     device = ", ".join(obj.device_type for obj in self.devicename.all())
    #     return app+" "+page+" "+device


class Device(BaseModel):

    device_type = models.CharField(
        max_length=100, choices=DEVICE_TYPE, null=True, blank=False, default=None)
    enrollment_type = models.CharField(
        max_length=100, choices=ENROLLMENT_TYPE, null=True, blank=False, default=None)
    device_registration_name = models.CharField(
        max_length=100, null=True, blank=True)

    iot_hub_name = models.ForeignKey(
        IOT_Hub, on_delete=models.CASCADE, null=True, blank=False, default='')
    dps_property_ID = models.ForeignKey(
        DPS_Property, on_delete=models.CASCADE, null=True, blank=False, default='')
    allocation_policy = models.CharField(
        max_length=100, choices=ALLOCATION_POLICY, null=True, blank=False, default=None)
    #device_IAM_mechanism = models.CharField(max_length=100,choices=IAM,null=True,blank=False,default=None)
    device_IAM_mechanism = models.ManyToManyField(Device_IAM_Mechanism)
    secret_storage = models.CharField(
        max_length=100, choices=SECRET_STORAGE, null=True, blank=False, default=None)
    operation = models.CharField(
        max_length=100, choices=OPERATION, null=True, blank=False, default=None)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, null=True, blank=False, default='')
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    date_of_purchase = models.DateField(null=True, blank=True)
    warrenty_period = models.CharField(
        max_length=100, choices=WARRENTY_PERIOD, null=True, blank=False, default=None)

    warrenty_expiry = models.DateField(null=True, blank=True)
    Firmware_version = models.CharField(max_length=100, null=True, blank=True)
    sold_to_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=False, default='')
    # communicate_to =
    route_to_application = models.ForeignKey(
        Application, on_delete=models.CASCADE, null=True, blank=False, default='')
    configured = models.CharField(
        max_length=100, choices=CONFI_TYPE, null=True, blank=False, default=None)
    # configuration_template =
    device_Specification_ID = models.ForeignKey(
        DeviceSpecification, on_delete=models.CASCADE, null=True, blank=False, default='')

    def __str__(self):
        return self.device_registration_name

