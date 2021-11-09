from django.shortcuts import  render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from .models import CarBooking
# from .form import SomeForm
from django.contrib.auth.decorators import login_required


def Home(request):
    
    return render(request, 'home.html', {})

def AdLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/list/')
            ...
        else:
            messages.success(request, ('the login error try again login'))
            return redirect('adminsign')
    else:    
        return render(request, 'adlogin.html', {})

def MLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/list/')
            ...
        else:
            messages.success(request, ('the login error try again login'))
            return redirect('msign')
    else:    
        return render(request, 'manager.html', {})

@login_required(redirect_field_name='bookinglist')
def BookingList(request):
    list = CarBooking.objects.all()

    return render(request, 'list.html', {'lists':list }) 

@login_required(redirect_field_name='bookingview')
def BookingView(request, id=None):
    # list = CarBooking.objects.all()
    # print('fff', list)
    id = get_list_or_404(CarBooking, id=id)
    
    return render(request, 'views.html', {'objects':id})

@login_required(redirect_field_name='bookingview')
def AdminView(request, id=None):
    data={}

    if request.method == 'POST' and "GET":
        id = get_list_or_404(CarBooking, id=id)
       
        print('obj', id)
        return JsonResponse(data)
        

    template = 'adview.html'
    return render(request, template, context)
@login_required(redirect_field_name='bookinglist')
def AdminViewList(request):
    list = CarBooking.objects.all()

    return render(request, 'list.html', {'lists':list }) 

def Booking(request):
    status = CarBooking.objects.all()
    if request.method == 'POST':
        subject = request.POST["subject"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        pickup = request.POST["pickup"]
        message = request.POST["message"]
        print(subject)

        obj = CarBooking.objects.create(subject=subject, username=username, 
                                email=email, number=number,
                                  pickup=pickup, message=message)
        obj.save()

        # return HttpResponseRedirect('{num}'.format(num=obj.slug))
        # try:
        #     subject = subject
        #     message = 'Userame '+ username + " number " + number +"pickup " + pickup + ""
        #     email_from = settings.EMAIL_HOST_USER
        #     send_mail(subject, message, email_from, [email])
           
        # except:
        #     # print('email not send')
        #     message.error(request, 'Feedback Saved but not send to admin.')
        return HttpResponseRedirect('/list/')
    context = {
        'status': status
    }
    return render(request, 'car.html', context)




