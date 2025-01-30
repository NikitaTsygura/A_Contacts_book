from django import forms
from models import Contact

class ContactsForms (forms.ModelForm):
    class Meta:
        model = Contact
        fiels = ['first_name', 'last_name', 'phone_number', 'email', 'photo']

