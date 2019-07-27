from django import forms
from onlineapp.models import *

# class addcolleges(forms.ModelForm):
#     class Meta:
#         model=College
#         exclude=['id']
#         widgets={
#             'name':forms.TextInput(attrs={'class':'input is-rounded per','placeholder':'Enter name'}),
#             'location':forms.TextInput(attrs={'class':'input is-rounded per','placeholder':'Enter location'}),
#             'acronym': forms.TextInput(attrs={'class':'input is-rounded per','placeholder': 'Enter acronym'}),
#             'contact': forms.EmailInput(attrs={'class':'input is-rounded per','placeholder': 'Enter email'})
#         }
# class addstudent(forms.ModelForm):
#     class Meta:
#         model=Student
#         exclude=['dob','college','id']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter name'}),
#             'email': forms.EmailInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter email'}),
#             'db_folder': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter db_folder'}),
#             #'dropped_out': forms.RadioSelect
#         }
#
# class addmarks(forms.ModelForm):
#     class Meta:
#         model=MockTest1
#         exclude=['total','student','id']
#         widgets = {
#             'problem1': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter problem1 marks'}),
#             'problem2': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter problem2 marks'}),
#             'problem3': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter problem3 marks'}),
#             'problem4': forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter problem4 marks'})
#         }

class loginform(forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input is-rounded per','placeholder':'Enter name'}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'input is-rounded per','placeholder':'Enter password'}))

class signupform(forms.Form):
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter first name'}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter last name'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter name'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'input is-rounded per', 'placeholder': 'Enter password'}))