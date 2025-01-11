from django.shortcuts import render
from.models import models

def index(request):
    return render(request, 'index.html')  # Рендерит твой index.html

def contact_list(request):
    contacts = Contact.object.all()
    return render(request, 'app/contact_list.html', {'contact': contacts})