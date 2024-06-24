




from django.urls import path

from adminapp import views



urlpatterns = [
    path('organizer',views.organizerindex,name='organizer'),
    path('Addtournament',views.Addtournament,name='Addtournament'),
    path('view_event',views.view_event,name='view_event'),
    path('edit/<int:id>',views.edit_event,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('jo_temas',views.jo_temas,name='jo_temas'),
    path('teamsj/<int:id>',views.teamsj,name='teamsj'),



]
