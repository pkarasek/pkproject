from django import forms

class CompanyNameForm(forms.Form):
    company_name = forms.CharField(label = 'company_name', max_length = 100)
    company_contact = forms.CharField(label = 'company_contact', max_length = 100)
