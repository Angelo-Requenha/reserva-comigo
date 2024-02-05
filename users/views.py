from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import ClienteForm, EstabelecimentoForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class register_cliente(CreateView):
    model = CustomUser
    form_class = ClienteForm
    template_name = 'registration/register_cliente.html'
    success_url = reverse_lazy('reserva_app:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('reserva_app:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
    

class register_estab(CreateView):
    model = CustomUser
    form_class = EstabelecimentoForm
    template_name = 'registration/register_estab.html'
    success_url = reverse_lazy('reserva_app:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('reserva_app:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.tipo = form.cleaned_data.get('tipo', 'E')
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm