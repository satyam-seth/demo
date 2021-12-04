from django.shortcuts import render
from .models import Org,Emp
from .forms import OrgForm,EmpForm

# Create your views here.

def org(request):
    orgs=Org.objects.all()
    org_form=OrgForm()
    if request.method=='POST':
        org_data=OrgForm(request.POST)
        if org_data.is_valid():
            name=org_data.cleaned_data['name']
            Org(name=name).save()
    return render(request,'core/org.html',{'orgs':orgs,'org_form':org_form})

def emp(request):
    emps=Emp.objects.all()
    emp_form=EmpForm()
    if request.method=='POST':
        emp_data=EmpForm(request.POST)
        if emp_data.is_valid():
            name=emp_data.cleaned_data['name']
            org=emp_data.cleaned_data['org']
            Emp(name=name,org=org).save()
    return render(request,'core/emp.html',{'emps':emps,'emp_form':emp_form})