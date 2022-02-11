from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . import forms
from ticket.models import Ticket, Review
from django.shortcuts import get_object_or_404, redirect, render



@login_required
def create_ticket(request):
    ticket = forms.CreateTicket()
    if request.method == 'POST':
        ticket = forms.CreateTicket(request.POST,request.FILES)
        if ticket.is_valid():
            ticket.save(commit=False)
            ticket.instance.author = request.user
            ticket.save()
            
            return redirect('home')

    return render(request,'ticket/create_ticket.html',context={'ticket':ticket})
    

@login_required
def create_review_from_ticket(request, ticket_id):
    review = forms.CreateReviewFromTicket()
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        review = forms.CreateTicket(request.POST,request.FILES)
        if review.is_valid():
            #review.instance.ticket = ticket
            review.save(commit=False)
            review.instance.author = request.user
            review.save()
            return redirect('home')

    return render(request,'ticket/create_review_from_ticket.html',context={'review':review})
    