from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ticket import models
from itertools import chain
from django.db.models import CharField, Value

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

@login_required
def no_more_critic(request):
    return render(request, 'flux/no_more_critic.html')

""""
@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request.user)
    
"""
@login_required
def home(request):
    tickets = models.Ticket.objects.filter(author__in=request.user.follows.all())
    reviews = models.Review.objects.filter(author__in=request.user.follows.all())
    context = {
         'tickets': tickets, 
         'reviews':reviews,
    }
    return render(request, 'flux/home.html', context=context)


@login_required
def my_posts(request):
    """ display the tickets and reviews of the connected user only """
    reviews = models.Review.objects.filter(author =request.user).order_by('-time_created')
    tickets = models.Ticket.objects.filter(author =request.user).order_by('-time_created')
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {}
    context ['posts'] = posts
    # return render(request, 'base_app/test.html', context=context)
    return render(request, 'flux/my_posts.html', context=context)


