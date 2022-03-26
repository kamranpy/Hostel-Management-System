from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class SettingForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name',
                  'phone',
                  'email',
                  'profile_pic',
                  'qualification',
                  'qualification_img',
                  'qualification_year',
                  'qualification_institute',
                  'age',
                  'emp_status',
                  'emp_designation',
                  'emp_bps',
                  'emp_home_address',
                  'emp_institute_address',
                  'cnic',
                  'cnic_img',
                  'gender')
        # fields = '__all__' to show all fields

        labels = {
                  'name': 'Full Name',
                  'phone': 'Contact No.',
                  'email': 'Email-ID',
                  'profile_pic': 'Recent Picture',
                  'qualification': 'Last Academic Degree Name',
                  'qualification_img': 'Upload Degree',
                  'qualification_year': 'Passing Year',
                  'qualification_Institute': 'University / College / School Name',
                  'age': 'Age',
                  'emp_status': 'Employement Status',
                  'emp_designation': 'Designation',
                  'emp_bps': 'Basic Pay Scale (If Govt. Employee)',
                  'emp_home_address': 'Home Address',
                  'emp_institute_address': 'Institute Address',
                  'cnic': 'CNIC',
                  'cnic_img': 'Upload CNIC',
                  'gender': 'Gender',
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class HostelForm(ModelForm):
    class Meta:
        model = Hostel
        fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'


# For Admin's / Warden's End
class HostelUpdateForm(forms.ModelForm):
    class Meta:
        model = HostelApply
        fields = ('customer',
                  'hostel',
                  'rooms',
                  'app_status',
                  'challan_no',
                  'upload_challan',
                  'feeStatus',
                  'mess',
                  'ac',
                  'duration',
                  'date_due',
                  'note')

        labels = {
            'customer': 'Student Name',
            'hostel': 'Hostel Name',
            'rooms': 'Allocated Room',
            'app_status': 'Application Status',
            'challan_no': 'Challan No.',
            'upload_challan': 'Upload Challan',
            'feeStatus': 'Fee Status',
            'mess': 'Would you like to apply for Hostel Mess?',
            'ac': 'Do you want an AC / Heater / Aircooler Room?',
            'duration': 'Degree Duration',
            'date_due': 'Due Date',
            'note': 'Remarks / Notes'
        }

    def __init__(self, *args, **kwargs):  # This will allow us to change properties of text boxes
        super(HostelUpdateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True
        self.fields["rooms"].queryset = Rooms.objects.filter(rHostelName=self.instance.hostel.id)


# For User's End
class HostelApplyForm(forms.ModelForm):
    class Meta:
        model = HostelApply
        fields = ('customer',
                  'hostel',
                  'duration',
                  'challan_no',
                  'mess',
                  'ac',
                  'upload_challan',
                  'note')

        labels = {
            'customer': 'Student Name',
            'hostel': 'Hostel Name',
            'duration': 'Degree Duration',
            'mess': 'Would you like to apply for Hostel Mess?',
            'ac': 'Do you want an AC / Heater / Aircooler Room?',
            'challan_no': 'Challan No.',
            'upload_challan': 'Upload Challan',
            'note': 'Remarks / Notes'
        }

    def __init__(self, *args, **kwargs):
        super(HostelApplyForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True
