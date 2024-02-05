from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import ClienteForm, EstabelecimentoForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

class register_cliente(CreateView):
    model = CustomUser
    form_class = ClienteForm
    template_name = 'registration/register_cliente.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('reserva_app:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reserva_app:home')
    

class register_estab(CreateView):
    model = CustomUser
    form_class = EstabelecimentoForm
    template_name = 'registration/register_estab.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('reserva_app:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.tipo = form.cleaned_data.get('tipo', 'E')
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reserva_app:home')
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
