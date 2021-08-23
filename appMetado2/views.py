from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import message, send_mail

def home(request):
    if request.method=="POST":
        mail= request.POST.get('correo')
        subject=request.POST['asunto']
        message =request.POST['mensaje']+" | Rementente: "+ request.POST['correo']
        email_from=settings.EMAIL_HOST_USER
        recipent_list=[mail]
        send_mail(subject, message, email_from, recipent_list)

        return redirect('sucesso')

    return render(request,'home.html')

def sucesso(request):
    return render(request,'sucesso.html')
