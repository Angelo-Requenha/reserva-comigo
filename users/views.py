from django.views.generic.edit import CreateView
from .models import CustomUser, UserProfile, FotosEstab
from .forms import ClienteForm, EstabelecimentoForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, reverse
import googlemaps
from django.conf import settings
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class register_cliente(CreateView):
    model = CustomUser
    form_class = ClienteForm
    template_name = 'registration/register_cliente.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.tipo == 'C':
                return redirect('cliente_app:grupos')
            if self.request.user.tipo == 'E':
                return redirect('estab_app:profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('users:login')
    

class register_estab(CreateView):
    model = CustomUser
    form_class = EstabelecimentoForm
    template_name = 'registration/register_estab.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.tipo == 'C':
                return redirect('cliente_app:grupos')
            if self.request.user.tipo == 'E':
                return redirect('estab_app:profile')
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):

        user = form.save(commit=False)
        user.tipo = form.cleaned_data.get('tipo', 'E')

        user.set_password(form.cleaned_data['password1'])
        user.save()

        UserProfile.objects.create(email=user)
        FotosEstab.objects.create(email=user)

        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('users:login')
    
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.tipo == 'C':
                return redirect('cliente_app:grupos')
            if self.request.user.tipo == 'E':
                return redirect('estab_app:profile')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):

        if self.request.user.tipo == 'C':
            return reverse_lazy('cliente_app:grupos')
        elif self.request.user.tipo == 'E':
            return reverse_lazy('estab_app:profile')
        else:
            return reverse_lazy('cliente_app:grupos')

@login_required
def register_address(request):
    user_profile = request.user.userprofile  

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            form.save()

            user_profile.has_profile = True
            user_profile.save()

            messages.success(request, 'Endereço registrado com sucesso!')
            return redirect('estab_app:profile')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'estab_app/profile.html', {'form': form})