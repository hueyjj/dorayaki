from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    
    def get(self, request):
        return Response()