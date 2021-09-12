from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404

from django.http import  HttpResponse, request
from django.shortcuts import render 
from django.http import HttpResponseRedirect

from .models import CarBooking
# from .forms import CarBookingForm
from django.views import View
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.views.generic.base import TemplateView


# def CarBooking(request):
#     if request.method == 'GET':
#         form = CarBookingForm()
#     else:
#         form = CarBookingForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             email = form.cleaned_data['email']
#             description = form.cleaned_data['description']
#             name = form.cleaned_data['name']
#             pickup_location = form.cleaned_data['pickup_location']
#             number = form.cleaned_data['number']
#             try:
#                 send_mail(subject, name, pickup_location, number, subject, description, email, ['alamin4936412gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('thanks')
#     return render(request, "car.html", {'form': form})
    

# class CarBooked(View):
#     form_class = CarBookingForm
#     template_name = 'car.html'
#     def get(self, request, *args, **kwargs):
        
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         subject = request.POST.get('subject')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         number = request.POST.get('number')
#         pickup_location = request.POST.get('pickup_location')
#         description = request.POST.get('description')
#         # print(name, email, number, pickup_location, description)
      
#         send_mail(
#             subject,
#             email,
#             name,
#             number,
#             pickup_location,
#             description,
#             ['alamin493641@gmail.com'],
            
#         )

#         return render(request, self.template_name, {'form': form})

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
            message = 'Userame '+ username + "number " + number +"pickup " + pickup + ""
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email])
           
        except:
            message.error(request, 'Feedback Saved but not send to admin.')
    context = {
        'status': status
    }
    return render(request, 'car.html', context)