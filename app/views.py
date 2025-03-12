from django.shortcuts import render

# Create your views here.
# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm
from django.http import HttpResponse

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']
            from_email = 'esurupraveen2004@gmail.com'

            # Send the email
            send_mail(subject, message, from_email, [recipient])

            return HttpResponse("Email sent successfully!")
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})
