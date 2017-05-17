from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import tramite,detalle,noticia
import mimetypes
import os
import urllib

@user_passes_test(lambda user: not user.username, login_url='/tramites', redirect_field_name=None)
def index(request):

    return render(request, 'web/index.html', {'id': noticia.objects.last().id})


@login_required()
def tramites(request):
        user = request.user
        return render(request, 'web/tramites.html', {'tramites':user.tramites.all()})
@csrf_exempt
def registro(request):

    password = request.POST['password']
    email = request.POST['email']
    name = request.POST['name']
    lastname = request.POST['lastname']

    try:

        if User.objects.filter(email=email).exists():
            return HttpResponse("El usuario ya existe")

        user = User.objects.create_user(username=email,
                                     email=email,
                                     password=password,
                                     first_name=name,
                                     last_name=lastname)
        user.save()

        return HttpResponse("Usuario creado correctamente")

    except:
        print("error")
        return HttpResponse("Hubo un error al crear el usuario")
@csrf_exempt
def login(request):
    password = str(request.POST['password'])
    email = str(request.POST['email'])
    print (email,password)
    user = authenticate(username=email, password=password)
    if user is not None:
        print("User")
        # the password verified for the user
        if user.is_active:
            auth_login(request, user)
            return HttpResponse('true')
        else:
            return HttpResponse("La cuenta es valida, pero ha sido desactivada")
    else:
        # the authentication system was unable to verify the username and password
        return HttpResponse("El usuario y/o clave son incorrectos")
def logout(request):
    auth_logout(request)
    return redirect("/")
def documentos(request,filename):

    fp = open('media/documentos/'+filename, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat('media/documentos/'+filename).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response


def noticias(request):


    if not 'id' in request.GET:
        query = noticia.objects.latest('fecha')
    else:
        query = noticia.objects.get(id=request.GET['id'])


    return render(request, 'web/noticias.html',{'noticias':noticia.objects.all().order_by('-fecha'),
                                                'noticia': query})
# Create your views here.
