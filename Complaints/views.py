from django.shortcuts import render, redirect
from .choices import complaint_choices
from .models import Complaint
from django.contrib import messages


def complaints(request):
    context = {
        'complaint_choices': complaint_choices
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        title = request.POST['title']
        description = request.POST['description']

        complaints = Complaint(username=username, title=title, description=description,first_name=first_name,last_name=last_name)
        complaints.save()
        messages.success(request, "Your complaint has been submitted, An admin will come back to you soon.")
    return render(request, 'complaints/complaint.html', context)

