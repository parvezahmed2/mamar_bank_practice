from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake 
    


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLgoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    







def send_transaction_email(user, subject, template):
     
    message = render_to_string(template,{
            'user' : user,
             
        })
    send_email = EmailMultiAlternatives( subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()



def pass_change2(request):
     if request.user.is_authenticated:

          if request.method == 'POST':
               form = SetPasswordForm(user=request.user, data = request.POST)
               if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user) # password update 
                    return redirect('profile')
          else:
               form = SetPasswordForm(user=request.user)
               mail_subject ="Password Change  Message "
               message = render_to_string('accounts/pass_change_email.html',{
                    'user' : request.user,
                     
                })

               to_email = request.user.email
               send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
               send_email.attach_alternative(message, "text/html")
               send_email.send()
          return render(request, 'accounts/passchange.html', {'form': form})
     else:
          return redirect('login')
