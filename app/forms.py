from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.core.validators import validate_email, RegexValidator
# from django.core.exceptions import ValidationErro


# class UsercreateForm(UserCreationForm):
#     email = forms.EmailField(required=True,label='Email',error_messages={'This email already exist'})

#     class Meta:
#         Model = User
#         fields =('first_name','surname','username','email','password1','password2')

#     def save(self,commit=True):
#         user = super(UsercreateForm,self).save(commit=False)
#         user.email =self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
    
#     def clean_email(self):
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise forms.ValidationError(self.fields['email'].error_message['exists'])
#         return self.cleaned_data['email']

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'required': 'This email field is required', 'invalid': 'Enter a valid email address'})

    class Meta:
        model = User
        fields = ( 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password1'
        self.fields['password2'].widget.attrs['placeholder'] = 'password2'

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('This email already exists')
        return self.cleaned_data['email']
    




















# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']

#     email = forms.EmailField(help_text='Enter your email')
#     mobile_number = forms.CharField(
#         max_length=10,
#         validators=[RegexValidator(regex='^[0-9]{10}$', message='Enter a valid 10-digit mobile number.')],
#         help_text='Enter your 10-digit mobile number'
#     )
#     date_field = forms.DateField(help_text='Enter your date of birth')
#     gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get("email")
#         mobile_number = cleaned_data.get("mobile_number")

#         if not email and not mobile_number:
#             raise ValidationError("Please provide either email or mobile number.")

#         return cleaned_data
