from django.shortcuts import redirect, render
from django.views import View
from managerapp.models import My_Team
from sports_app.models import Manager_Reg, user_reg
from django.views.generic import TemplateView
from django.contrib.auth.models import User


from userapp.models import CreateTournament, join_tournament,send_request
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'user/user_index.html')






def view_tour(request):

    set=CreateTournament.objects.all()
    return render(request,'user/view_t.html',{'set':set})


def join(request,id):
    user=user_reg.objects.get(user_id=request.user.id)
    if join_tournament.objects.filter(user_id=user.id,Tournament_id=id):
         messages.success(request, 'Aleady joined')

         return redirect('view_tour')
    else:
        se = join_tournament()

        se.status='join'
        se.Tournament_id=id
    
        se.user_id=user.id
        se.payment='notpaid'
        se.save()
        msg=messages.success(request, 'joined')

    
    return redirect('user')
def joinedT(request):
    user=user_reg.objects.get(user_id=request.user.id)

    set=join_tournament.objects.filter(user_id=user.id)
  
    
    return render(request,'user/joined_t.html',{'set':set})


# def payment(request,id):
#     obj=Schedule_tournament.objects.get(id=id)

#     return render(request,'user/payment.html',{'set':obj})






def mytour(request):
    user=user_reg.objects.get(user_id=request.user.id)
    obj=CreateTournament.objects.filter(user_id=user.id)



    return render(request,'user/joindes_teams.html',{'set':obj})

# def teamsj(request,id):
  

#     obj=Schedule_tournament.objects.filter(Tournament_id=id)

#     return render(request,'user/teams.html',{'set':obj})


# def Customize(request,id):
  
#     return render(request,'user/schedule.html',{'obj':shop})

# class teamsj(TemplateView):
#     template_name='user/teams.html'
#     def get_context_data(self, **kwargs):
#         id = self.request.GET['id']

#         obj=Schedule_tournament.objects.filter(Tournament_id=id)
#         sac=coustamize.objects.filter(Tournament_id=id)

#         context={
#             'set':obj,
#             'sac':sac
#         }
        
#         return context



# class Customize(TemplateView):
#     template_name='user/customize.html'
#     def get_context_data(self,**kwargs,):
#         id = self.request.GET['id1']
#         id5 = self.request.GET['id5']

#         user=User.objects.get(id=id)
#         name=user.first_name
        
#         obj = Schedule_tournament.objects.exclude(user_id=id)
#         context={
#             'obj':obj,
#             'name':name,
#             'tour':id5

#         }
        
#         return context
    
#     def post(self, request, *args, **kwargs):
#         id3 = self.request.GET['id1']
#         team1 = request.POST['team1']
#         date = request.POST['date']
#         time = request.POST['time']
#         tour = request.POST['tour']
#         team = request.POST['team']

 
#         userre=User.objects.get(id=id3)
#         fname=userre.first_name
#         print(fname)
#         set=coustamize()
#         set.Tournament_id=tour
#         set.team1=fname
#         set.team2=team
#         set.time=time
#         set.date=date
#         set.save()
#         return render(request, 'user/user_index.html', {'message': " Account Rejected"})
    
    
    
def managerlist(request):

    obj=Manager_Reg.objects.all()

    return render(request,'user/managerlist.html',{'set':obj})


    
def send_request_user(request,id):
    user=user_reg.objects.get(user_id=request.user.id)

    if send_request.objects.filter(user_id=user.id):
        messages.success(request, 'Already Requested')

        return redirect('managerlist')
    else:
        set=send_request()
        set.manager_id=id
        set.user_id=user.id
        set.status='Requested'
        set.save()
        messages.success(request, 'requested')
        return redirect('managerlist')
class payment(TemplateView):
    template_name='user/payment.html'
    def post(self, request,*args,**kwargs):
        id=self.request.GET['id']
        ob=join_tournament.objects.get(id=id)
        ob.payment='paid'
        ob.save()
        messages.success(request, 'Successfull')
        return redirect('joinedT')
        

def ourT(request):
    try:
        user=user_reg.objects.get(user_id=request.user.id)

        obj=My_Team.objects.get(user_id=user.id)
        manager=obj.manager_id
        bb=join_tournament.objects.filter(manager_id=manager)
    

        return render(request,'user/joined_t.html',{'bb':bb})
    except:
        return render(request,'user/joined_t.html')




        
        
     
   
   
