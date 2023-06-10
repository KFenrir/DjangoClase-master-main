from django.shortcuts import render
from .models import Usuario, tipoUsuario

# Create your views here.


def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/index.html", context)


def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/user_list.html", context)


def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "pages/user_add.html", context)


def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)


def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "pages/user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "pages/user_list", context)


def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user}

        return render(request, "pages/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/user_list.html", context)

def main(request):
    context={}
    return render(request, "pages/main.html", context)

def login(request):
    context={}
    return render(request, "pages/login.html", context)

def registro(request):
    context={}
    return render(request, "pages/registro.html", context)

def gatos(request):
    context={}
    return render(request, "pages/gatos.hmtl", context)

def perros(request):
    context={}
    return render(request, "pages/perros.html", context)

def arnes_gatos(request):
    context={}
    return render(request, "pages/arnes_gatos.html", context)

def bandana_gatos(request):
    context={}
    return render(request, "pages/bandana_gatos.html", context)

def collar_gatos(request):
    context={}
    return render(request, "pages/collar_gatos.html", context)

def carrito(request):
    context={}
    return render(request, "pages/carrito.html", context)

def catalogo(request):
    context={}
    return render(request, "pages/catalogo.html", context)

def tallas(request):
    context={}
    return render(request, "pages/tallas.html", context)

def suscripciones(request):
    context={}
    return render(request, "pages/suscripciones.html", context)

def nosotros(request):
    context={}
    return render(request, "pages/nosotros.html", context)