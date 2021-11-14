from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    send_mail(
        "Hello",  # This is the subject
        "Hello this is roboty.",  # This is the body
        "zutest620@gmail.com",  # This is the sender
        ["keiifer1997@gmail.com"],  # This is the recipient list
        fail_silently=False,
    )
    return render(request, "Email/index.html")
