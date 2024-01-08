from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

  
        
class Edit_Registration(UserChangeForm):
    first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password=forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden'}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
        
        
        
    def __init__(self, *args, **kwargs):
        super(Edit_Registration, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['username'].label=''
        self.fields['username'].help_text=''
        
        
        
        
 

        