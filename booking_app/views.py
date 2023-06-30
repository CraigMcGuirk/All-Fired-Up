from django.shortcuts import render
import random
import string
from booking_app.models import Reservation, Table


# Create your views here.


def index(request):
   
    return render(request, 'booking_app/index.html')


def menu(request):

    return render(request, 'booking_app/menu.html')


def reservations(request):
    reservation_id = id_generator()
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email_address')
        numpeople = request.POST.get('number_of_people')
        date = request.POST.get('date')
        time = request.POST.get('time')

        table = Table.objects.get(table_number=1)
        
        Reservation.objects.create(
            id= reservation_id,
            table_number=table, 
            first_name=fname, 
            last_name=lname, 
            email_address=email, 
            number_of_people=numpeople, 
            date=date, 
            time=time,
        )

    return render(request, 'booking_app/reservations.html')


def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
