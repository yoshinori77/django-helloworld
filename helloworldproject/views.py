from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworld(request):
    return HttpResponse('helloworld')

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
    