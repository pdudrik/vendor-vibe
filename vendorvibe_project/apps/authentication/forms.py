from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Employee, Company


class EmployeeCreationForm(UserCreationForm):
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="-- Select Your Company Workspace --"
    )

    class Meta:
        model = Employee
        fields = ["username", "email", "company"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = Employee
        fields = ["username", "password"]