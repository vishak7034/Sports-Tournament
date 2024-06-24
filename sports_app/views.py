from django.shortcuts import render
from django.shortcuts import render,redirect
from sports_app.forms import location_Form, sports_Form
from sports_app.models import Manager_Reg, Organizer_Reg, UserType, user_reg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def loginview(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('admin')
                elif UserType.objects.get(user_id=user.id).type =="user":
                    return redirect('user')
                elif UserType.objects.get(user_id=user.id).type =="manager":
                    return redirect('manager')  
                elif UserType.objects.get(user_id=user.id).type =="organizer":
                    return redirect('organizer')  
             
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})
    
    return render(request,'login.html')

def Manager_Register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['number']

        address = request.POST['address']
        if User.objects.filter(email=email):
            return render(request, 'reg.html', {'message': "already added the email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
            user.save()
            st = Manager_Reg()
            st.user = user
            st.address= address
            st.phone_number=phone_number
            st.count=0
            st.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ="manager"
            usertype.save()
            return render(request, 'reg.html', {'message': "successfully added"})
    return render(request,'manager_reg.html')

def Organizer_Register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['number']

        address = request.POST['address']
        if User.objects.filter(email=email):
            return render(request, 'reg.html', {'message': "already added the email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
            user.save()
            stu = Organizer_Reg()
            stu.user = user
            stu.address= address
            stu.phone_number=phone_number
            stu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "organizer"
            usertype.save()
            return render(request, 'reg.html', {'message': "successfully added"})
    return render(request,'organizer.html')


def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['number']

        address = request.POST['address']
        if User.objects.filter(email=email):
            return render(request, 'reg.html', {'message': "already added the email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
            user.save()
            stu = user_reg()
            stu.user = user
            stu.address= address
            stu.phone_number=phone_number
            stu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return render(request, 'reg.html', {'message': "successfully added"})
    return render(request,'reg.html')


def adminindex(request):
    return render(request,'admin/index.html')



def addlocation(request):
    form = location_Form()
    if request.method == 'POST':
        form = location_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')

    return render(request,'admin/location.html',{'form':form})



def Addsports(request):
    form = sports_Form()
    if request.method == 'POST':
        form = sports_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')

    return render(request,'admin/sports.html',{'form':form})





def userverify(request):
    shop = user_reg.objects.filter(user__last_name='0')
  
    return render(request,'admin/approve.html',{'shop':shop})

def user_view(request):
    shop3 = user_reg.objects.all()
  
    return render(request,'admin/user_view.html',{'shop3':shop3})
def managerveri(request):
    shop = Manager_Reg.objects.filter(user__last_name='0')
  
    return render(request,'admin/manager_a.html',{'shop':shop})

def manager_view(request):
    shop1 = Manager_Reg.objects.all()
  
    return render(request,'admin/manager_view.html',{'shop1':shop1})

def organiserrveri(request):
    shop = Organizer_Reg.objects.filter(user__last_name='0')
  
    return render(request,'admin/organizer.html',{'shop':shop})

def organiser_view(request):
    shop2 = Organizer_Reg.objects.all()
  
    return render(request,'admin/organiser_view.html',{'shop2':shop2})

def approve(request,id):
    user = User.objects.get(pk=id)
    user.last_name='1'
    user.save()
    messages.success(request, 'Approved')

    return redirect('userverify')

def reject(request,id):
    User.objects.get(pk=id).delete()

    messages.success(request, 'Rejected')

    return redirect('userverify')



