from django.shortcuts import render , HttpResponse
from datetime import datetime
from domain.models import Contact
# Create your views here.
def index(request):
    return render (request, "index.html")
def about(request):
    return render (request, "about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sugs = request.POST.get('sugs')
        phone = request.POST.get('phone')
        contact =  Contact(name = name, email=email, sugs=sugs, phone=phone, date = datetime.today )
        contact.save
    return render (request, "contact.html")