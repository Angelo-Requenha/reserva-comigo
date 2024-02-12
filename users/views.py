from django.views.generic.edit import CreateView
from .models import CustomUser, UserProfile
from .forms import ClienteForm, EstabelecimentoForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, reverse
from googlemaps import Client
from django.conf import settings
from django.http import JsonResponse
from reserva_projeto.mixins import(
	AjaxFormMixin, 
	FormErrors,
	RedirectParams,
	)

result = "Error"
message = "Houve um erro, tente novamente"

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



def profile_view(request):
	'''
	function view to allow users to update their profile
	'''
	user = request.user
	up = user.userprofile

	form = UserProfileForm(instance = up) 

	if request.headers.get('x-requested-with') == 'XMLHttpRequest':
		form = UserProfileForm(data = request.POST, instance = up)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Seu perfil foi atualizado!"
		else:
			message = FormErrors(form)
		data = {'result': result, 'message': message}
		return JsonResponse(data)

	else:

		context = {'form': form}
		context['google_api_key'] = settings.GOOGLE_API_KEY
		context['base_country'] = settings.BASE_COUNTRY

		return render(request, 'estab_app:profile.html', context)