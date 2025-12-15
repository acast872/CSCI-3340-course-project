from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomSignUpForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff #Staff Only View
    
class UserListView(StaffRequiredMixin, ListView):
    model = User
    template_name = 'accounts/user_manage.html'
    context_object_name = 'users'
    paginate_by = 25