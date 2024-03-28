from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email-template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['marcelorobin@gmail.com','codigoparaprincipiantes@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')
        return redirect('index')






