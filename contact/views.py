from django.shortcuts import  render, get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect

from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from .models import CarBooking
from .form import SomeForm
from django.contrib.auth.decorators import login_required

class LoginView(TemplateView):
    template_name = "login.html"

@login_required(redirect_field_name='bookinglist')
def BookingList(request):
    list = CarBooking.objects.all()

    return render(request, 'list.html', {'lists':list }) 

@login_required(redirect_field_name='bookingview')
def BookingView(request, id=None):
    print(id)
    obj = get_list_or_404(CarBooking, id=id)

    context = {
        'objects': obj,
    }
    template = 'views.html'
    return render(request, template, context)

def car(request):
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
        try:
            subject = subject
            message = 'Userame '+ username + " number " + number +"pickup " + pickup + ""
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email])
           
        except:
            # print('email not send')
            message.error(request, 'Feedback Saved but not send to admin.')
    context = {
        'status': status
    }
    return render(request, 'car.html', context)



def admin(request):
    if request.method == 'POST':
        username = request.POST('username')
        print(username)
        password = request.POST('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list/')
            
        else:
            pass
            # return an 'invalid login' error message.
            
    return render(request, 'admin.html')

