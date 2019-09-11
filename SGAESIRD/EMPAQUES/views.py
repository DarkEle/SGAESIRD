from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView

from .models import Usuario

from .forms import SignUpForm



# Create your views here.
def home(request):
	return render(request, 'home.html', {})

class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm
	
    def form_valid(self, form):
        '''
        En esta parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
