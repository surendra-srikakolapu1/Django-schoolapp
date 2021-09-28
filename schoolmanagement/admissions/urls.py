from django.urls import path

from .views import *

from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('register', register,name='register'),
    path('logout', logout,name='logout'),
     path('forgot-password/', ForgotPassword,name='forgot-password'),
     path('change-password/<token>/', ChangePassword,name='change-password'),


    path('newadm/', addadmission),
    path('delete/<int:id>', deletestudent),
    path('update/<int:id>', updatestudent),


    path('newfee/', addfee),
    path('delete-fee/<int:id>', deletefee),
    path('update-fee/<int:id>', updatefee),

    path('newteacher/', addteacher),
    path('delete-teacher/<int:id>', deleteteacher),
    path('update-teacher/<int:id>', updateteacher),

    path('id_generator/', id_generator),
    path('id_card/', id_card),
    path('detail/<int:id>/', detail , name="detail"),
    path('delete-id_card/<int:id>', deleteid_card),

    path('contact/', Contact),

]
