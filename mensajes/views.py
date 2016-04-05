from django.shortcuts import render
from django.http import HttpResponse
from .models import mensaje
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def enviar(request):

    try:
        asunto = request.POST['asunto'];
        email = request.POST['email'];
        texto = request.POST['texto'];
        titulo = request.POST['titulo'];

        mensaje.objects.create(titulo=titulo,email=email,asunto=asunto,texto=texto);

        return HttpResponse("Mensaje enviado")

    except:
        return HttpResponse("Hubo un error al enviar el mensaje")
