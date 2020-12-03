from django import forms
from .models import info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class datauser(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name',]
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                }

class data(UserCreationForm):
    password1=forms.CharField(label="Enter your password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Enter your password again",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields =['username','first_name','last_name','email'] 
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                }

class newform(forms.ModelForm):
    article_no=forms.CharField(label="enter article no (1/2)",widget=forms.TextInput(attrs={'class':'form-control'}))
    image_name=forms.CharField(label="enter image name",widget=forms.TextInput(attrs={'class':'form-control'}))
    catgory=forms.CharField(label="enter catagory",widget=forms.TextInput(attrs={'class':'form-control'}))
    heading=forms.CharField(label="enter headlines",widget=forms.TextInput(attrs={'class':'form-control'}))
    article=forms.CharField(label="enter article here",widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model=info
        fields=['image']


class logindata(AuthenticationForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class passform(PasswordChangeForm):
    old_password=forms.CharField(label="Oldpassword",widget=forms.TextInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label="Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
   

