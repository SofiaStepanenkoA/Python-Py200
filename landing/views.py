from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse
from .forms import TemplateForm

# Create your views here.
class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            data = {}
            data["Name"] = form.cleaned_data.get("Name")  # Получили очищенные данные
            data["Email"] = form.cleaned_data.get("Email")
            data["Subject"] = form.cleaned_data.get("Subject")
            data["Message"] = form.cleaned_data.get("Message")

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP
            data["ip"] = ip
            user_agent = request.META.get('HTTP_USER_AGENT')
            return JsonResponse(data,json_dumps_params={'ensure_ascii':False,'indent':4})
        return render(request, 'landing/index.html', context={"form": form})