from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    cat_emp = (
        ('Govt. Employee', 'Govt. Employee'),
        ('Un-Employed', 'Un-Employed'),
        ('Private Job', 'Private Job'),
    )

    cat_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    # Basic Info
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    age = models.CharField(max_length=5, null=True)
    gender = models.ImageField(max_length=200, null=True, choices=cat_gender)
    cnic = models.CharField(max_length=200, null=True)
    cnic_img = models.ImageField(null=True)

    # Academic Info
    qualification = models.CharField(max_length=100, null=True)
    qualification_img = models.ImageField(null=True)
    qualification_year = models.CharField(max_length=100, null=True)
    qualification_institute = models.CharField(max_length=100, null=True)

    # Employement Info
    emp_status = models.CharField(max_length=200, null=True, choices=cat_emp)
    emp_designation = models.CharField(max_length=200, null=True, blank=True)
    emp_bps = models.CharField(max_length=200, null=True, blank=True)
    emp_home_address = models.CharField(max_length=200, null=True)
    emp_institute_address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Hostel(models.Model):
    hostelName = models.CharField(max_length=200, null=True)
    hostelRooms = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.hostelName


class Rooms(models.Model):
    rHostelName = models.ForeignKey(Hostel, null=True, on_delete=models.SET_NULL)
    roomName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.roomName


class HostelApply(models.Model):
    status_category = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
    )

    fee_category = (
        ('Paid', 'Paid'),
        ('UnPaid', 'UnPaid'),
    )

    mess_category = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    hostel = models.ForeignKey(Hostel, null=True, on_delete=models.SET_NULL)
    rooms = models.OneToOneField(Rooms, null=True, on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_due = models.CharField(max_length=200, null=True)
    challan_no = models.CharField(max_length=1000, null=True)
    upload_challan = models.ImageField(null=True)
    app_status = models.CharField(max_length=200, null=True, choices=status_category, blank=True)
    mess = models.CharField(max_length=200, null=True, choices=mess_category)
    ac = models.CharField(max_length=200, null=True, choices=mess_category)
    feeStatus = models.CharField(max_length=200, null=True, choices=fee_category, default="UnPaid")
    duration = models.CharField(max_length=1000, null=True)
    note = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.hostel.hostelName + " Hostel Room Request"

