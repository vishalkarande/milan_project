from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class claim_policy(forms.ModelForm):
    #category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.policy_claim
        fields=['mobile_no','place','date','policy_name','discr']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }