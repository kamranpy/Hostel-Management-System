from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from.models import *
from .filters import OrderFilter
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.


# View for Registration Page
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created successfully for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'supervisory/register.html', context)


# View for Login Page
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, 'supervisory/login.html', context)


# View for Logout Page
def logoutUser(request):
    logout(request)
    return redirect('login')


# View for Admin Dashboard Page
@login_required(login_url='login')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    applications = HostelApply.objects.all()
    rooms = Rooms.objects.all()

    last_five_apps = HostelApply.objects.all().order_by('-id')[:5]
    last_five_users = Customer.objects.all().order_by('-id')[:5]

    total_customers = customers.count()
    total_apps = applications.count()
    total_rooms = rooms.count()
    approved = applications.filter(app_status='Approved').count()
    empty_rooms = total_rooms - approved

    context = {'customers': customers,
               'applications': applications,
               'total_apps': total_apps,
               'approved': approved,
               'total_customers': total_customers,
               'last_five_apps': last_five_apps,
               'last_five_users': last_five_users,
               'total_rooms':total_rooms,
               'empty_rooms':empty_rooms}

    return render(request, 'supervisory/dashboard.html', context)


# View for User Dashboard Page
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    applications = request.user.customer.hostelapply_set.all()

    context = {'applications': applications}
    return render(request, 'supervisory/user.html', context)


# View for Account Settings
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def accountSettings(request):
    customer = request.user.customer
    form = SettingForm(instance=customer)

    if request.method == 'POST':
        form = SettingForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'supervisory/account_settings.html', context)


# Views for User Accounts Information on Admin End
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    applications = customer.hostelapply_set.all()
    total_apps = applications.count()

    myFilter = OrderFilter(request.GET, queryset=applications)
    applications = myFilter.qs

    context = {'customer': customer, 'applications': applications, 'total_apps': total_apps,
               'myFilter': myFilter}

    return render(request, 'supervisory/customer.html', context)


# View for Testing Purpose
def testPage(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/test.html', context)


# Admin View for Viewing all User accounts
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def allUsers(request):
    customers = Customer.objects.all()

    context = {'customers': customers}

    return render(request, 'supervisory/all_users.html', context)


# View for Creating Hostels for Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createHostel(request):

    form = HostelForm()

    if request.method == 'POST':
        form = HostelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hostels')

    context = {'form': form}
    return render(request, 'supervisory/create_hostel.html', context)


# View for Creating Hostels for Admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createRoom(request):

    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hostels/rooms')

    context = {'form': form}
    return render(request, 'supervisory/create_room.html', context)


# View for Creating / Viewing Hostels
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def hostel(request):
    hostels = Hostel.objects.all()

    return render(request, 'supervisory/hostels.html', {'hostels':hostels})


# View for Updating Hostel Information
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateHostel(request, pk):
    hostel = Hostel.objects.get(id=pk)
    form = HostelForm(instance=hostel)

    if request.method == 'POST':
        form = HostelForm(request.POST, instance=hostel)
        if form.is_valid():
            form.save()
            return redirect('/hostels')

    context = {'form': form}
    return render(request, 'supervisory/create_hostel.html', context)


# Views for Deleting Hostel from Admin's End
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteHostel(request, pk):
    hostel = Hostel.objects.get(id=pk)
    if request.method == 'POST':
        hostel.delete()
        return redirect('/hostels')

    context = {'hostel': hostel}
    return render(request, 'supervisory/delete_hostel.html', context)


# View for Creating / Viewing Rooms
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def rooms(request):
    rooms = Rooms.objects.all()

    return render(request, 'supervisory/rooms.html', {'rooms':rooms})


# View for Updating Hostel Information
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/hostels/rooms')

    context = {'form': form}
    return render(request, 'supervisory/create_room.html', context)


# Admin View for Viewing all applications
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def hostelapps(request):
    applications = HostelApply.objects.all()

    context = {'applications': applications}

    return render(request, 'supervisory/hostelapps.html', context)


# Views for Updaing Applications from Admin's End
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateApp(request, pk):
    applications = HostelApply.objects.get(id=pk)
    form = HostelUpdateForm(instance=applications)

    total_fee = 31000

    if applications.mess == 'Yes' and applications.ac == 'Yes':
        total_fee = total_fee + 7000

    elif applications.mess =='Yes':
        total_fee = total_fee + 2000

    elif applications.ac =='Yes':
        total_fee = total_fee + 5000

    if request.method == 'POST':
        form = HostelUpdateForm(request.POST, request.FILES, instance=applications)
        if form.is_valid():
            form.save()
            return redirect('/hostel/applications')

    context = {'form': form, 'total_fee':total_fee}
    return render(request, 'supervisory/update_hostel_app.html', context)


# View for a User to Apply for Hostel Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def hostelApply(request, pk):
    customer = Customer.objects.get(id=pk)

    form = HostelApplyForm(initial={'customer': customer})
    if request.method == 'POST':
        form = HostelApplyForm(request.POST, request.FILES)
        form.initial['customer'] = request.user.customer
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'supervisory/hostel_apply.html', context)


# View for User's Allocated Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_room(request):
    rooms = request.user.customer.hostelapply_set.all().filter(app_status='Approved')

    context = {'rooms': rooms}
    return render(request, 'supervisory/user_room.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_rules(request):
    return render(request, 'supervisory/user_rules.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def faq(request):
    return render(request, 'supervisory/faq.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def meals(request):
    return render(request, 'supervisory/meals.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def fee_structure(request):
    return render(request, 'supervisory/fee_structure.html')


# Views for Deleting Applications from Admin's End
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_hostel_app(request, pk):
    application = HostelApply.objects.get(id=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('/hostel/applications')

    context = {'application': application}
    return render(request, 'supervisory/delete_hostel_app.html', context)

