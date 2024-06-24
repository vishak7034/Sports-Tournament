from django.shortcuts import redirect, render
from adminapp.forms import TournamentFormsss

from managerapp.models import My_Team
from sports_app.models import Organizer_Reg
from userapp.models import CreateTournament, join_tournament

# Create your views here.
def organizerindex(request):
    return render(request,'organizer/index.html')


def Addtournament(request):
    form = TournamentFormsss()
    user=Organizer_Reg.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = TournamentFormsss(request.POST,request.FILES)
        if form.is_valid():
            de = form.save(commit=False)
            de.organizer_id=user.id
            de.save()
            form.save()
            return redirect('organizer')

    return render(request,'organizer/tournament.html',{'form':form})



def edit_event(request,id):
    employee = CreateTournament.objects.get(id=id)
    form = TournamentFormsss(instance=employee)

    if request.method == 'POST':
        form = TournamentFormsss(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_event')

    return render(request,'organizer/edit.html',{'form':form})



def view_event(request):
    user=Organizer_Reg.objects.get(user_id=request.user.id)

    obj=CreateTournament.objects.filter(organizer_id=user.id)

    return render(request,'organizer/view_t.html',{'set':obj})


def delete(request,id):
    pro = CreateTournament.objects.get(id=id)

    if request.method == 'POST':
        pro.delete()
        return redirect('view_event')

    return render(request,'organizer/delete.html',{'pro':pro})

def jo_temas(request):
    user=Organizer_Reg.objects.get(user_id=request.user.id)

    obj=join_tournament.objects.filter(organizer_id=user.id)

    return render(request,'organizer/joindes_teams.html',{'set':obj})




def teamsj(request,id):
  

    obj=join_tournament.objects.filter(id=id)

    return render(request,'organizer/teams.html',{'set':obj})