from django.shortcuts import render
from index.models import Contact
# Create your views here.
def home(request) :
    return render(request, 'home.html')
def about(request) :
    return render(request, 'about.html')
def projects(request) :
    return render(request, 'projects.html')
def contact(request) :
    if request.method=='POST':
      name=request.POST['name'] 
      email=request.POST['email']
      query=request.POST['query']
      print(name,email, query) 
      obj= Contact(name=name, email = email, query = query)
      obj.save()
    return render(request, 'contact.html')