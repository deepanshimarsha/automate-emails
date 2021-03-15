from django.shortcuts import render
from config.settings import EMAIL_HOST_USER
from subscribe import forms
from django.core.mail import send_mail


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Dont Mind This Mail'
        message = 'Experimenting with my new django mini project. Thank you!'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form': sub})