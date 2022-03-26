from django.urls import path
from . import views


urlpatterns = [
    # Urls for User Pages
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('user/rules', views.user_rules, name="user-rules"),
    path('user/faq', views.faq, name="faq"),
    path('user/meals', views.meals, name="meals"),
    path('user/fee/structure', views.fee_structure, name="fee_structure"),
    path('user/room/', views.user_room, name="user_room"),
    path('testPage/', views.testPage, name="test-page"),
    path('account/', views.accountSettings, name="account"),
    path('hostel/apply/<str:pk>', views.hostelApply, name="hostel_apply"),
    path('hostel/applications/', views.hostelapps, name="hostelapps"),

    # Urls for Admin Pages
    path('users/all/', views.allUsers, name="all_users"),
    path('create/supervisory/', views.createHostel, name="create_hostel"),
    path('create/hostel/room', views.createRoom, name="create_room"),
    path('hostels/rooms', views.rooms, name="rooms"),
    path('update/room/<str:pk>/', views.updateRoom, name="update_room"),
    path('update/hostel/<str:pk>/', views.updateHostel, name="update_hostel"),
    path('', views.dashboard, name="dashboard"),
    path('hostels/', views.hostel, name="hostels"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('update_app/<str:pk>/', views.updateApp, name="update_hostel_app"),
    path('delete_hostel/<str:pk>/', views.deleteHostel, name="delete_hostel"),
    path('delete_hostel_app/<str:pk>/', views.delete_hostel_app, name="delete_hostel_app")
]


# 1 - Submit Email Form                         //PasswordResetView.as_view()
# 2 - Email Sent Success Message                //PasswordResetDoneView.as_view()
# 3 - Link to Password Reset form in email      //PasswordResetConfirmationView.as_view()
# 4 - Password Successfully Changed message     //PasswordResetCompleteView.as_view()

