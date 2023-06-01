from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.


def home(request):
    # return HttpResponse("This is my homepage(/)")
    context = {'name': 'Aditya', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("This is my about page(/about)")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("This is my projects page(/projects)")
    return render(request, 'projects.html')


def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        concern = request.POST['concern']
        #print(firstname, lastname, email, city, state, pincode, concern)
        contact = Contact(firstname=firstname, lastname=lastname, email=email,
                      city=city, state=state, pincode=pincode, concern=concern)
        contact.save()
        print("The data has been written to the db")

    # return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.html')
