# для хранения представлений текущего приложения
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения vomen")
def categories(request):
    return HttpResponse("<h1> статья по категориям </h1>")
def categories1(request):
    return HttpResponse("<h1> новая статья по  категориям запроса </h1>")