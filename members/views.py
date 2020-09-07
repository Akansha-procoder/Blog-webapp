from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import 	SignUpForm

class UserRegisterView(generic.CreateView):
	form_class=SignUpForm
	success_url = reverse_lazy('login')
	template_name ='registration/register.html'
#  	return render(request, 'home.html', {})
#def home(request):
class UserEditView(generic.UpdateView):
	form_class=SignUpForm
	success_url = reverse_lazy('home')
	template_name ='registration/edit_profile.html'

	def get_object(self):
		return self.request.user


