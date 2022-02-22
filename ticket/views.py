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
    ticket = Ticket.objects.get(id=ticket_id)
    print(ticket.id , ticket.title)
    review = forms.CreateReview()
    if ticket.review_set.exists():
        return redirect('redirect_home')
    elif request.method == "POST" and not ticket.review_set.exists():
        review = forms.CreateReview(request.POST,request.FILES)
        review.instance.author = request.user
        review.instance.ticket = ticket
        if review.is_valid():
            review.save()
            return redirect('home')
    else:
        pass
        
    return render(request,'ticket/create_review_from_ticket.html',context={'review':review, 'ticket':ticket})

@login_required
def create_ticket_and_review(request):
    ticket = forms.CreateTicket()
    review = forms.CreateReview()
    if request.method == 'POST':
        ticket = forms.CreateTicket(request.POST,request.FILES)
        review = forms.CreateReview(request.POST)
        if ticket.is_valid():
            
            ticket.instance.author = request.user
            ticket.save(commit=False)
            ticket.save()
            if review.is_valid():
                review.instance.author = request.user
                review.instance.ticket = ticket.instance
                review.save()
                return redirect('home')
    return render(request,'ticket/ticket_and_review.html',context={'review':review, 'ticket':ticket})

@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'ticket/follow_users_form.html', context={'form': form})

# blog/views.py

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_ticket_form = forms.CreateTicket(instance=ticket)
    delete_ticket_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket_form' in request.POST:
            edit_ticket_form = forms.CreateTicket(request.POST, instance=ticket)
            if edit_ticket_form.is_valid():
                edit_ticket_form.save(commit=False)
                edit_ticket_form.instance.author = request.user
                edit_ticket_form.save()
                return redirect('home')
        if 'delete_ticket_form' in request.POST:
            delete_ticket_form = forms.DeleteTicketForm(request.POST)
            print('delete?')
            if delete_ticket_form.is_valid():
                print('DELET DU TICKET EST VALIDE')
                ticket.delete()
                return redirect('home')
    context = {
        'edit_ticket_form': edit_ticket_form,
        'delete_ticket_form': delete_ticket_form,
    }
    return render(request, 'ticket/edit_ticket.html', context=context)