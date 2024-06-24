
from django.forms import DateInput, FileInput, ModelForm, Select, TextInput, Textarea, TimeInput

from sports_app.models import Sports, Tournament, location


class location_Form(ModelForm):
    class Meta:
        model=location
        fields=['Lname']
        widgets = {

            'Lname': TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Add Location'})

        }
        
        
        
class sports_Form(ModelForm):
    class Meta:
        model=Sports
        fields=['sportsname']
        widgets = {

            'sportsname': TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Add Sports'})

        }
        
        
        



