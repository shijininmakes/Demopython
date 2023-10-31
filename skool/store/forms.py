from django import forms
from .models import Order,Department, Course, Material
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'),('other','other')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=10)
    mail_id = forms.EmailField()
    address = forms.CharField(max_length=200)
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label='Select a department',
        required=True
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label='Select a course',
        required=False
    )

    purpose = forms.ChoiceField(
        choices=[('For Enquiry', 'For Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')],
        required=True
    )

    materials_provide = forms.ModelMultipleChoiceField(
    queryset = Material.objects.all(),
    widget = forms.CheckboxSelectMultiple,
    required = False)

    class Meta:
        model = Order
        fields = ['name', 'dob', 'mail_id', 'age', 'gender', 'phone_number', 'address', 'purpose']

