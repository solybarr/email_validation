from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Email

def index(request):
    context = {
        "emails" : Email.objects.all()
    }
    return render(request, "emails/index.html", context)
    #return HttpResponse(Email.objects.validate(request.POST['email']))

def add(request):
    if (Email.objects.validate(request.POST['email'])):
        Email.objects.create(email=request.POST['email'])
        email=request.POST['email']
        messages.success(request, "The email you entered (%s) is VALID!" % email)
        return redirect('/')
    else:
        #flash message goes here
        messages.error(request, 'Invalid Email!')
        return redirect('/')



def destroy(request, id):
    #We are not confirming the delete this time just deleting
    Email.objects.filter(id=id).delete()
    messages.success(request, "Email was removed from the DB")
    return redirect('/')
