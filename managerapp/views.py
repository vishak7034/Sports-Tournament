from django.shortcuts import redirect, render
from managerapp.models import My_Team
from sports_app.models import Manager_Reg, user_reg
from sports_app.views import Manager_Register
from django.contrib import messages
from django.views import View

from userapp.models import CreateTournament, join_tournament, send_request

# Create your views here.



def managerindex(request):
    return render(request,'manager/index.html')



def view_request(request):
    user=Manager_Reg.objects.get(user_id=request.user.id)

    shop = send_request.objects.filter(manager_id=user.id,status='requested')
  
    return render(request,'manager/request.html',{'shop':shop})

class add_my_team(View):
    def dispatch(self, request, *args, **kwargs):
        user=Manager_Reg.objects.get(user_id=request.user.id)
        id = self.request.GET['id1']
        id2 = self.request.GET['id5']
        add=Manager_Reg.objects.get(user_id=request.user.id)
        count=add.count
        print("cgcgh",count)
        if count>=16:
            messages.success(request, '16 members added ')
            return redirect('view_request')
        else:
            my=My_Team()
        
            myg=send_request.objects.get(id=id)

            my.user_id=id2
            myg.status='added'
            my.manager_id=user.id
            my.save()
            myg.save()
            uu=Manager_Reg.objects.get(id=id2)
            uu.count=(uu.count)+1
            uu.save()
        
            messages.success(request, 'Added my Team')
            return redirect('view_request')
  

def My_TeamR(request):
    user=Manager_Reg.objects.get(user_id=request.user.id)

    shop = My_Team.objects.filter(manager_id=user.id)
  
    return render(request,'manager/myteam.html',{'shop':shop})


def Remove(request,id):
    My_Team.objects.get(id=id).delete()

    return redirect('My_Team')


def reject(request,id):
    my=send_request.objects.get(id=id)
    my.status='reject'
    my.save()

    return redirect('view_request')



def view_tour(request):

    set=CreateTournament.objects.all()
    return render(request,'manager/view_t.html',{'set':set})


def join(request,id):
    s=CreateTournament.objects.get(id=id)
    org=s.organizer_id
    user=Manager_Reg.objects.get(user_id=request.user.id)
    if join_tournament.objects.filter(manager_id=user.id,Tournament_id=id):
         messages.success(request, 'Aleady joined')

         return redirect('view_tour')
    else:
        se = join_tournament()

        se.status='join'
        se.Tournament_id=id
        se.organizer_id=org
        se.manager_id=user.id
        se.payment='notpaid'
        se.save()
        msg=messages.success(request, 'joined')

    
    return redirect('view_tour')
def joinedT(request):
    user=Manager_Reg.objects.get(user_id=request.user.id)

    set=join_tournament.objects.filter(manager_id=user.id)
  
    
    return render(request,'manager/joined_t.html',{'set':set})










