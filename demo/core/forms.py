from django import forms
from django.db.models import fields
from .models import Org,Emp

class OrgForm(forms.ModelForm):
    class Meta:
        model=Org
        fields=['name']

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name','org']