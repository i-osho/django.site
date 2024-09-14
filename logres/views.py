from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
import datetime


indexcoulmns = {0:'ID',1:'DU No',2:'Resident Class',3:'Resident Name',4:'username',5: 'Father Spouse Name',6:'Date of Birth',7:'Blood Group',8:'E-mail Address',9:'IRWO PM Number',10:'Legacy Type',11:'Designation',12:'Organisation Department',13:'Office Address',14:'Whatsapp No',15:'Mobile Phone',16:'Scheme Reg No',17:'Allotment Date'}
columns = ('ID','DU No','Resident Class','Resident Name','username', 'Father Spouse Name','Date of Birth','Blood Group','E-mail Address','IRWO PM Number','Legacy Type','Designation','Organisation Department','Office Address','Whatsapp No','Mobile Phone','Scheme Reg No','Allotment Date')

USERNAME,PASSWORD, USERID = None, None, None
ADMINU, ADMINP = None, None
def get_data(USERNAME, PASSWORD, USERID=None):
    with connection.cursor() as cursor:
        if USERID != None:
            if USERID.isdigit():
                cursor.execute("SELECT * FROM residents WHERE `ID` = %s", [USERID])
            else:
                cursor.execute("SELECT * FROM residents WHERE `DU No` = %s", [USERID])
            records = cursor.fetchone()
        else:
            cursor.execute("SELECT * FROM residents WHERE `Mobile Phone` = %s AND `username` = %s", [PASSWORD, USERNAME])
            records = cursor.fetchone()
        if cursor.rowcount == 0:
            return False
        else: 
            return records

# Create your views here.

def home(request):
    global USERNAME, PASSWORD, USERID
    if (USERNAME is None and PASSWORD is None):
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
    if get_data(USERNAME,PASSWORD, USERID) is False:
        messages.error(request, 'Invalid credentials')
        USERNAME, PASSWORD = None, None
        return redirect('login')
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12: greet = 'Good morning '
    elif 12 <= currentTime.hour < 18: greet = 'Good afternoon '
    else: greet = 'Good evening '
    return render(request, 'home.html', {'type':'Home', 'name':greet+str(USERNAME)})

def index(request):
    return render(request, 'index.html', {'type':'Home'})

def login(request):
    return render(request, 'login.html', {'type':'Resident Login'})

def userdata(request):
    global USERNAME, PASSWORD, USERID
    records = get_data(USERNAME, PASSWORD, USERID)
    column_value_pairs = zip(columns, records)
    TYPE = "Resident's Data" if USERID == None else f"Resident's Data with ID/DU No {USERID}"
    return render(request, 'userdata.html', {'column_value_pairs': column_value_pairs, 'type':TYPE})

def editdata(request):
    global USERNAME, PASSWORD, USERID
    records = get_data(USERNAME, PASSWORD, USERID)
    column_value_pairs = zip(columns, records)
    TYPE = "Edit Data" if USERID == None else f"Editing Resident's Data with ID/DU No {USERID}"
    return render(request, 'editdata.html', {'column_value_pairs': column_value_pairs, 'type':TYPE})

def success(request):
    global USERNAME, PASSWORD, USERID
    canDelete = request.POST.get('delete')
    if canDelete:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM residents WHERE `ID` = %s", [USERID])
    else:
        ID = request.POST.get('ID')
        DU_No = request.POST.get('DU No')
        Resident_Class = request.POST.get('Resident Class')
        Resident_Name = request.POST.get('Resident Name')
        username = request.POST.get('username')
        Father_Spouse_Name = request.POST.get( 'Father Spouse Name')
        Date_of_Birth = request.POST.get('Date of Birth')
        Blood_Group = request.POST.get('Blood Group')
        Email_Address = request.POST.get('E-mail Address')
        IRWO_PM_Number = request.POST.get('IRWO PM Number')
        Legacy_Type = request.POST.get('Legacy Type')
        Designation = request.POST.get('Designation')
        Organisation_Department = request.POST.get('Organisation Department')
        Office_Address = request.POST.get('Office Address')
        Whatsapp_No = request.POST.get('Whatsapp No')
        Mobile_Phone = request.POST.get('Mobile Phone')
        Scheme_Reg_No = request.POST.get('Scheme Reg No')
        Allotment_Date = request.POST.get('Allotment Date')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE residents SET `DU No` = %s, `Resident Class` = %s, `Resident Name` = %s, `username` = %s, `Father Spouse Name` = %s, `Date of Birth` = %s, `Blood Group` = %s, `E-mail Address` = %s, `IRWO PM Number` = %s, `Legacy Type` = %s, `Designation` = %s, `Organisation Department` = %s, `Office Address` = %s, `Whatsapp No` = %s, `Mobile Phone` = %s, `Scheme Reg No` = %s, `Allotment Date` = %s WHERE `ID` = %s", [DU_No, Resident_Class, Resident_Name, username, Father_Spouse_Name, Date_of_Birth, Blood_Group, Email_Address, IRWO_PM_Number, Legacy_Type, Designation, Organisation_Department, Office_Address, Whatsapp_No, Mobile_Phone, Scheme_Reg_No, Allotment_Date, ID])
    USERNAME, PASSWORD, USERID = None, None, None
    return render(request, 'success.html', {'type':'Success'})

def logout(request):
    global USERNAME, PASSWORD
    global ADMINU, ADMINP, USERID
    USERNAME, PASSWORD, ADMINU, ADMINP, USERID = None, None, None, None, None
    return redirect('index')

def adminlogin(request):
    return render(request, 'adminlogin.html', {'type':'Admin Login'})

def getid(request):
    global ADMINU, ADMINP, USERID
    if (ADMINU is None and ADMINP is None):
        ADMINU = request.POST.get('adminuser')
        ADMINP = request.POST.get('adminpass')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM admin_users WHERE `adminpass` = %s AND `adminuser` = %s", [ADMINP, ADMINU])
        if cursor.rowcount == 0:
            messages.error(request, 'Invalid credentials')
            ADMINU, ADMINP = None, None
            return redirect('adminlogin')
    USERID = None
    return render(request, 'getid.html', {'type':'Search ID/DU No'})

def adminhome(request):
    global USERID
    if USERID is None:
        USERID = request.POST.get('userID')
    if get_data(None, None, USERID) is False:
        messages.error(request, 'Invalid ID/DU No')
        USERID = None
        return redirect('getid')
    return render(request, 'adminhome.html', {'type':'Admin Panel', 'USERID':USERID})

def deletedata(request):
    global USERID
    return render (request, 'deletedata.html', {'type':'Delete Data', 'USERID':USERID})

