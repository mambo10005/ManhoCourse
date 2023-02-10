from django.http import HttpResponse


def index(request):
    return HttpResponse("홈페이지 입니다.")