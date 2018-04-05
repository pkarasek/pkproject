from django import forms
from django.contrib.auth.models import User

class CompanyNameForm(forms.Form):
    company_name = forms.CharField(label = 'company_name', max_length = 100)
    company_contact = forms.CharField(label = 'company_contact', max_length = 100)

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active')
