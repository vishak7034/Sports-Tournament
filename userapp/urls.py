
from django.urls import path
from userapp import views
# from userapp.views import teamsj

urlpatterns = [
        path('user',views.index,name='user'),
        path('ourT',views.ourT,name='ourT'),
        # path('joint/<int:id>',views.join,name='joint'),
        # path('joinedT',views.joinedT,name='joinedT'),
        # path('payment/<int:id>',views.payment,name='payment'),

        # path('payment_status',views.payment_status,name='payment_status'),
        path('payment',views.payment.as_view(),name='payment'),
        # path('payment_add',views.payment_add.as_view(),name='payment_add'),

        path('managerlist',views.managerlist,name='managerlist'),

        path('send_request/<int:id>',views.send_request_user,name='send_request')





]
