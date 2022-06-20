from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.

def kakao_login(request):
    app_rest_api_key = os.environ.get("d34ab279891fc22ce5db471d7d35e4a8")
    redirect_uri = main_domain + "users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'d34ab279891fc22ce5db471d7d35e4a8'}&redirect_uri={'http://127.0.0.1:8000/accounts/kakao/login/callback/'}&response_type=code"
    )


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)

