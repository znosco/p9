from django.forms import ModelForm,ChoiceField,RadioSelect,BooleanField,HiddenInput,Form
from ticket.models import Ticket, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateTicket(ModelForm):
    edit_ticket_form = BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description':'Description',
            'image': 'Image',
        }


class CreateReview(ModelForm):
    CHOICES = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = ChoiceField(choices=CHOICES, widget=RadioSelect())

    class Meta:
        model = Review
        fields = ['rating', 'headline', 'description']
        exclude = ['ticket', 'author', 'time_created']
        
class FollowUsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['follows']
        
class DeleteTicketForm(Form):
    delete_ticket_form = BooleanField(widget=HiddenInput, initial=True)