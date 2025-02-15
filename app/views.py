from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactsForms

def index(request):
    return render(request, 'index.html')  # Рендерит твой index.html

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contact': contacts})

def add_contactt(request):
    if request.method == "Post":
        form = ContactsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')

    else:
        form = ContactsForms()
        return render(request, 'contact_form.html', {'form': form})