from django.urls import path

from managerapp import views


urlpatterns = [
        path('manager',views.managerindex,name='manager'),
        path('view_request',views.view_request,name='view_request'),
        
        path('add_my_team',views.add_my_team.as_view(),name='add_my_team'),
        path('My_Team',views.My_TeamR,name='My_Team'),
        path('Remove/<int:id>',views.Remove,name='Remove'),

        path('reject/<int:id>',views.reject,name='reject'),
        path('view_tour',views.view_tour,name='view_tour'),
        path('joint/<int:id>',views.join,name='joint'),
        path('joinedT',views.joinedT,name='joinedT'),

]
