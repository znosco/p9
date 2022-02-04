from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . import forms
from ticket.models import Ticket

User = get_user_model()

@login_required
def create_ticket(request):
    ticket = forms.CreateTicket()
    if request.method == 'POST':
        ticket = forms.CreateTicket(request.POST,request.FILES)
        if ticket.is_valid():
            pass
        
        
        
        
        context = {
            'ticket':ticket,
        }
        
        
        
        
        return render(request,'ticket.html',context=context)
    
    