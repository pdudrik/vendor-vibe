from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import EmployeeCreationForm, LoginForm


def login_view(request):
    return render(request, "authentication/login.html")


class RegisterView(CreateView):
    form_class = EmployeeCreationForm
    template_name = "authentication/register.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    

class LoginUserView(LoginView):
    authentication_form = LoginForm
    template_name = "authentication/login.html"
