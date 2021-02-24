from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def coming_soon(request):
    return render(request, 'page-coming-soon.html')

def email(request):
    if request.method == 'POST':
        email = request.POST['email']
        send_mail(
            "testing" ,#subject 
            "You are getting this mail because you subscribed to our channel", #msg
            settings.EMAIL_HOST_USER, # from mail
            [email], #rec list
            fail_silently = False
        )
        print('Email sent')
        return render(request,'page-coming-soon.html')
    else :
        print("error")
        return render(request,'comingsoon/page-coming-soon.html')



