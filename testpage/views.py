from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import residents
# Create your views here.

indexcoulmns = {0:'ID',1:'DU No',2:'Resident Class',3:'Resident Name',4:'username',5:'FatherSpouse Name',6:'Date of Birth',7:'Blood Group',8:'E-mail Address',9:'IRWO PM Number',10:'Legacy Type',11:'Designation',12:'OrganisationDepartment',13:'Office Address',14:'Whatsapp No',15:'Mobile Phone',16:'Scheme Reg No',17:'Allotment Date'}
columns = ['ID','DU No','Resident Class','Resident Name','username','FatherSpouse Name','Date of Birth','Blood Group','E-mail Address','IRWO PM Number','Legacy Type','Designation','OrganisationDepartment','Office Address','Whatsapp No','Mobile Phone','Scheme Reg No','Allotment Date']
queryall = "`ID`,`DU No`,`Resident Class`,`Resident Name`,`username`,`FatherSpouse Name`,`Date of Birth`,`Blood Group`,`E-mail Address`,`IRWO PM Number`,`Legacy Type`,`Designation`,`OrganisationDepartment`,`Office Address`,`Whatsapp No`,`Mobile Phone`,`Scheme Reg No`,`Allotment Date"

def test(request):
    return render(request, 'test.html', {'type':'Test'})

def testinfo(request):
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')
    # return render(request, 'test.html', {'result':[password, password_confirmation]})
    if not password_confirmation == password:
        return HttpResponse('Passwords do not match.')
    else:
        return HttpResponse('Passwords match.')
