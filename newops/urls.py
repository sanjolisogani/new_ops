from django.contrib import admin
from django.conf.urls import url
from . import views

from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomEmailValidationOnForgotPassword
from .models import *
from django.urls import re_path
from django.urls import path,include

urlpatterns = [
  url(r'^signup/$', views.signup_view, name='signup'),
  url(r'^login/$', views.login_view, name='login'),
  url(r'^hello/$', views.hello, name='hello'),

  path('reset_password/',auth_views.PasswordResetView.as_view(form_class=CustomEmailValidationOnForgotPassword),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('applicationapi/',details,name="applicationdetail"),
    path('applicationapi/applicationapipost',ApplicationDetail.as_view(),name="postapi"),

    path('assestgroupapi/',assestdetails,name="assestdetail"),
    path('assestgroupapi/assestapipost',AssestDetail.as_view(),name="postassestapi"),

    path('devicespecapi/',devicespec_details,name="devicespecdetail"),
    path('devicespecapi/devicespecpost',DeviceSpecDetail.as_view(),name="postdeviceapi"),
    path('vendorapi/',vendor_details,name="vendordetail"),
    path('vendorapi/vendorpost',VendorDetail.as_view(),name="postvendorapi"),
    path('iamapi/',IAM_details,name="iamdetail"),
    path('iamapi/iampost',IAMDetail.as_view(),name="postiamapi"),
    path('dpsapi/',DPS_details,name="dpsdetail"),
    path('dpsapi/dpspost',DPSDetail.as_view(),name="postdpsapi"),
    path('usergroupapi/',Usergroup_details,name="usergroupdetail"),
    path('usergroupapi/usergrouppost',usergroupDetail.as_view(),name="postusergroupapi"),
    path('iotapi/',IOT_details,name="iotdetail"),
    path('iotapi/iotpost',IotDetail.as_view(),name="postiotapi"),
    path('caapi/',CA_details,name="cadetail"),
    path('caapi/capost',CADetail.as_view(),name="postcaapi"),
    path('usertypeapi/',Usertype_details,name="usertypedetail"),
     path('usertypeapi/usertypepost',UserTypeDetail.as_view(),name="postusertypeapi"),
    path('permissionapi/',Permission_details,name="permissiondetail"),
     path('permissionapi/permissionpost',PermissionDetail.as_view(),name="postpermissionapi"),
    path('customerapi/',Customer_details,name="customerdetail"),
     path('customerapi/customerpost',CustomerDetail.as_view(),name="postcustomerapi"),
    path('certificateapi/',Certificate_details,name="certificatedetail"),
     path('certificateapi/certificatepost',CertificateDetail.as_view(),name="postcertificateapi"),
     path('deviceapi/',devicedetails,name="devicedetail"),
     path('deviceapi/devicepost',DeviceDetail.as_view(),name="postdeviceapi"),
]