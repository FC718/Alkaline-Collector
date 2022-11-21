from django.forms import ModelForm
from .models import Juicing

class JuicingForm(ModelForm):
    class Meta:
        model = Juicing
        fields = ['date', 'meal']

        
