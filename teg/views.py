from django.shortcuts import render_to_response, render
from teg.models import usuario
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def call_index (request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def register (request):
    c = {}
    c.update(csrf(request))
    return render_to_response('register.html', c)

@csrf_exempt
def data_register(request):
    c = {}
    c.update(request)
    if request.POST['apodo'] and request.POST['nombre'] and request.POST['apellido'] and request.POST['email'] and request.POST['pass']:
        p1 = request.POST['pass']
        p2 = request.POST['passconf']
        if (p1 == p2):
            newusr = usuario.crear_usuario(request.POST['nombre'],
                                           request.POST['apellido'],
                                           request.POST['apodo'],
                                           request.POST['email'],
                                           request.POST['pass'])

            newusr.save()
            # return HttpResponseRedirect(reverse('register-ok.html'))
            return render_to_response('register-ok.html', {})

    return render_to_response('register-error.html', {})

#HttpResponseRedirect(reverse(