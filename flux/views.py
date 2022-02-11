from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ticket import models
from django.shortcuts import get_object_or_404

import ticket

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'flux/home.html', context = {'tickets': tickets, 'reviews':reviews})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'flux/view_ticket.html', {'ticket': ticket})