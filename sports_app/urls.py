from django.urls import path
from sports_app import views


urlpatterns = [
        path('',views.index,name='index'),
        path('login/',views.loginview,name='login'),
        path('reg/',views.reg,name='reg'),
        path('Organizer_Reg',views.Organizer_Register,name='Organizer_Reg'),
        path('Manager_Reg',views.Manager_Register,name='Manager_Reg'),

        path('admin',views.adminindex,name='admin'),
        path('location',views.addlocation,name='location'),
        path('Addsports',views.Addsports,name='Addsports'),
        path('organiserrveri',views.organiserrveri,name='organiserrveri'),
        path('managerveri',views.managerveri,name='managerveri'),
        path('manager_view',views.manager_view,name='manager_view'),
        path('organiser_view',views.organiser_view,name='organiser_view'),
        path('user_view',views.user_view,name='user_view'),

        path('userverify',views.userverify,name='userverify'),
        path('approve/<int:id>',views.approve,name='approve'),
        path('reject/<int:id>',views.reject,name='reject'),





]
