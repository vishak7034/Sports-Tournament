



from django.forms import DateInput, FileInput, ModelForm, Select, TextInput, Textarea, TimeInput

from userapp.models import CreateTournament


class TournamentFormsss(ModelForm):
    class Meta:
        model=CreateTournament
        fields =['sports','location','Eventname','date','time','fee','image','description']
        widgets = {
            'sports': Select(
                attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
         'Eventname': TextInput(
                attrs={'class': 'form-control','placeholder': 'Event Name'}),
         'location': TextInput(
                attrs={'class': 'form-control','placeholder': 'location'}),
          'fee': TextInput(
                attrs={'class': 'form-control','placeholder': 'fee'}),
         'date': DateInput(format=('%Y-%m-%d'),
                                       attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}), 
           
         'image': FileInput(attrs={'class':'form-control'}),
         'time': TimeInput(format='%H:%M',attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'time'}),
         'description': Textarea(
                attrs={'class': 'form-control'}),


        }
        
        

        
        
        


        