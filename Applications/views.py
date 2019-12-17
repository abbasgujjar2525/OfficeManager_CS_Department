from django.shortcuts import render
from .choices import application_choices
from .models import Application
from django.contrib import messages
from django.shortcuts import render, redirect

def applications(request):
    context = {
        'application_choices': application_choices
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        title = request.POST['title']
        description = request.POST['description']

        applications = Application(first_name=first_name, last_name=last_name, username=username, title=title, description=description)
        applications.save()
        messages.success(request, "Your application has been submitted, An admin will come back to you soon.")

    return render(request, 'applications/application.html', context)