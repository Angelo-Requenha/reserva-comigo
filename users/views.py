from django.views.generic.edit import CreateView
from .models import CustomUser, UserProfile
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
            return redirect('users:login')
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
            return redirect('users:login')
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):

        user = form.save(commit=False)
        user.tipo = form.cleaned_data.get('tipo', 'E')

        user.set_password(form.cleaned_data['password1'])
        user.save()

        UserProfile.objects.create(email=user)

        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('users:login')
    
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm


@login_required
def register_address(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user_profile = form.save(commit=False)

            # Chave da API do Google Places
            api_key = settings.GOOGLE_API_KEY
            gmaps = googlemaps.Client(key=api_key)

            # Construa o endereço completo
            full_address = f"{user_profile.endereco}, {user_profile.cidade}, {user_profile.estado}, {user_profile.pais}"

            # Faça uma solicitação à API Places para obter detalhes do lugar
            try:
                response = gmaps.places(query=full_address)

                # Extraia os detalhes do primeiro resultado (supondo que seja o mais relevante)
                result = response['results'][0]

                # Preencha os campos do formulário com os detalhes obtidos
                user_profile.endereco = result.get('formatted_address', '')
                user_profile.cidade = result.get('address_components', [])[0].get('long_name', '')
                user_profile.estado = result.get('address_components', [])[2].get('long_name', '')
                user_profile.pais = result.get('address_components', [])[3].get('long_name', '')
                user_profile.cep = result.get('address_components', [])[6].get('long_name', '')
                user_profile.longitude = result.get('geometry', {}).get('location', {}).get('lng', '')
                user_profile.latitude = result.get('geometry', {}).get('location', {}).get('lat', '')

                user_profile.has_profile = True
                user_profile.save()

                messages.success(request, 'Endereço registrado com sucesso!')

                return redirect('estab/profile')

            except Exception as e:
                messages.error(request, f'Erro ao obter detalhes do endereço: {e}')

    else:
        form = UserProfileForm()

    return render(request, 'estab_app/profile.html', {'form': form})
