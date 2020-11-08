from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def contact(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['from_email']

        send_mail(
            from_email,  # from
            message,  # message
            subject,  # subject

            [settings.EMAIL_HOST_USER, ],  # to email
        )

    return render(request, 'contact/contact.html')
