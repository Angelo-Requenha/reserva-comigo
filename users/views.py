from django.views.generic.edit import CreateView
from .models import CustomUser, UserProfile, FotosEstab
from .forms import ClienteForm, EstabelecimentoForm, CustomAuthenticationForm, UserProfileForm, FotosEstabForm, EstabelecimentoProfileForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from estab_app.models import DiaMarcado
import calendar

class register_cliente(CreateView):
    model = CustomUser
    form_class = ClienteForm
    template_name = 'registration/register_cliente.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.user.tipo == 'C':
                return redirect('cliente_app:grupos')
            if self.request.user.tipo == 'E':
                return redirect('estab_app:notificacoes')
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
                return redirect('estab_app:notificacoes')
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
                return redirect('reserva_app:pagina_convidativa')
            if self.request.user.tipo == 'E':
                return redirect('estab_app:notificacoes')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):

        if self.request.user.tipo == 'C':
            return reverse_lazy('reserva_app:pagina_convidativa')
        elif self.request.user.tipo == 'E':
            return reverse_lazy('estab_app:notificacoes')
        else:
            return reverse_lazy('reserva_app:pagina_convidativa')


def generate_calendar(year, month, email):
    cal = calendar.HTMLCalendar().formatmonth(int(year), int(month))
    highlighted_days = []
    
    # Filtrando os dias marcados para o usuário com o email fornecido
    marked_days = DiaMarcado.objects.filter(ano=year, mes=month, email_usuario=email)
    
    # Adicionando os dias marcados à lista de dias destacados
    for marked_day in marked_days:
        highlighted_days.append(marked_day.dia)
    
    for day in highlighted_days:
        highlighted_day = f'<span><strong>{day}</strong></span>'
        cal = cal.replace(f'>{day}<', f'>{highlighted_day}<')
        
    return cal

@login_required
def register_profile(request):
    user_profile = request.user.userprofile
    user_fotos = get_object_or_404(FotosEstab, email=request.user)
    user = request.user  # Move a definição de user para fora do bloco else

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        photos_form = FotosEstabForm(request.POST, request.FILES, instance=user_fotos)
        register_form = EstabelecimentoProfileForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid() and photos_form.is_valid() and register_form.is_valid():
            profile_form.save()
            photos_form.save()
            register_form.save()

            user_profile.has_profile = True
            user_profile.save()

            user_fotos.has_fotos = True
            user_fotos.save()

            messages.success(request, 'Informações registradas com sucesso!')
            return redirect('estab_app:profile')
        else:
            messages.error(request, 'Por favor, corrija os erros nos formulários.')
    else:
        profile_form = UserProfileForm(instance=user_profile)
        photos_form = FotosEstabForm(instance=user_fotos)
        register_form = EstabelecimentoProfileForm(instance=request.user)
   
    context = {
        'profile_form': profile_form,
        'photos_form': photos_form,
        'register_form': register_form,
        'user': user
        }  

    return render(request, 'estab_app/profile.html', context)
