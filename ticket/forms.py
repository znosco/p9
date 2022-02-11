from django.forms import ModelForm
from ticket.models import Ticket, Review

class CreateTicket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description':'Description',
            'image': 'Image',
        }


class CreateReviewFromTicket(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'description']
        labels = {
            'headline': 'Titre',
            'description':'Description'
        }