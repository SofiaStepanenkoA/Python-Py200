from django.shortcuts import render
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm,CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView

class MyTemplView(TemplateView):
    template_name = 'app/template_form.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get(
                "my_text")  # Получили очищенные данные
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")

            return JsonResponse(form.cleaned_data)
        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
class TemplView(View):
    def get(self, request):
        return render(request, 'app/template_form.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_password = form.cleaned_data.get("my_password")
            my_email = form.cleaned_data.get("my_email")
            my_date = form.cleaned_data.get("my_date")
            Robot_check = form.cleaned_data.get("Robot_check")
            politics_check = form.cleaned_data.get("politics_check")
            return JsonResponse(form.cleaned_data)
        return render(request, 'app/template_form.html', context={"form": form})
class MyFormView(FormView):
    template_name = 'app/template_form.html'
    form_class = TemplateForm
    success_url = '/'

    def form_valid(self, form):
        return JsonResponse(form.cleaned_data)


class MyLoginView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True  # Данный флаг не позволит авторизированному
    # пользователю зайти на страницу с авторизацией и сразу его перенаправит на
    # ссылку редиректа. По умолчанию redirect_authenticated_user = False
def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    # if request.method == "POST":
    #     received_data = request.POST  # Приняли данные в словарь
    #     print(received_data)
    #
    #     # как пример получение данных по ключу `my_text`
    #     # my_text = received_data.get('my_text')
    #     data={}
    #     data['my_text'] = received_data.get('my_text')
    #     data['my_password'] = received_data.get('my_password')
    #     data['my_email'] = received_data.get('my_email')
    #     data['my_select'] = received_data.get('my_select')
    #     data['my_textarea'] = received_data.get('my_textarea')
    #     data['my_date'] = received_data.get('my_date')
    #     data['Robot_check'] = received_data.get('Robot_check')
    #     data['politics_check'] = received_data.get('politics_check')
    #     return JsonResponse(data,json_dumps_params={'ensure_ascii':False,'indent':4})
    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_password = form.cleaned_data.get("my_password")
            my_email = form.cleaned_data.get("my_email")
            my_date = form.cleaned_data.get("my_date")
            Robot_check = form.cleaned_data.get("Robot_check")
            politics_check = form.cleaned_data.get("politics_check")
            # TODO Получите остальные данные из формы и сделайте необходимые обработки (если они нужны)
            return JsonResponse(form.cleaned_data)
            # TODO Верните HttpRequest или JsonResponse с данными

        return render(request, 'app/template_form.html', context={"form": form})
        # TODO Проведите здесь получение и обработку данных если это необходимо

        # TODO Верните HttpRequest или JsonResponse с данными


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Возвращает сохраненного пользователя из данных формы
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("app:user_profile")

        return render(request, 'app/register.html', context={"form": form})


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')

def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})

