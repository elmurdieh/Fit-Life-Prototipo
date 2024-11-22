from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from primerApp.models import administrador, equipo, claseGrupal
from primerApp.forms import formAdministrador,formEquipo,formClaseGrupal, formProducto

def index(request):
    return render(request, 'primerApp/index.html')

def registrar(request):
    form = formAdministrador()
    
    if request.method == 'POST':
        form = formAdministrador(request.POST)
        if form.is_valid():
            administrador = form.save(commit=False)
            administrador.contraseña = make_password(form.cleaned_data['contraseña'])
            print("Contraseña encriptada:", administrador.contraseña)
            administrador.save()
            return redirect('/')
    
    data = {'form': form}
    return render(request, 'primerApp/registro.html', data)

def inicioSesion(request):
    if request.method == 'POST':
        if 'rut' in request.POST and 'contraseña' in request.POST:
            rut = request.POST['rut']
            contraseña = request.POST['contraseña']
            try:
                usuario = administrador.objects.get(rut=rut)
                if check_password(contraseña, usuario.contraseña):
                    request.session['usuario_id'] = usuario.id
                    return redirect(f'/administrar/{usuario.rut}/')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except administrador.DoesNotExist:
                messages.error(request, 'El RUT ingresado no está registrado')
        else:
            messages.error(request, 'Complete ambos campos')
    
    return render(request, 'primerApp/inicioSesion.html')


def ventanaAdministrador(request, rut):
    if not request.session.get('usuario_id'):
        return redirect('/inicio_de_Sesion/')

    try:
        usuario = administrador.objects.get(rut=rut)
        if request.session.get('usuario_id') != usuario.id:
            return redirect('/inicio_de_Sesion/')

        form_equipo = formEquipo()
        form_clase_grupal = formClaseGrupal()
        form_producto = formProducto()

        entrenadores = equipo.objects.filter(rol="entrenador")
        clasesGrupales = claseGrupal.objects.all()
        personal = equipo.objects.all()

        if request.method == 'POST':
            if 'submit_equipo' in request.POST:
                form_equipo = formEquipo(request.POST, request.FILES)
                if form_equipo.is_valid():
                    form_equipo.save()
                    print("Perfil del equipo creado exitosamente.")
                    return redirect(f'/administrar/{usuario.rut}/')
                else:
                    print("Error al crear el perfil del equipo. Verifique los datos.")
                    print(form_equipo.errors)
            elif 'submit_clase_grupal' in request.POST:
                form_clase_grupal = formClaseGrupal(request.POST)
                if form_clase_grupal.is_valid():
                    form_clase_grupal.save()
                    print("Clase grupal creada exitosamente.")
                    return redirect(f'/administrar/{usuario.rut}/')
                else:
                    print("Error al crear la clase grupal. Verifique los datos.")
                    print(form_clase_grupal.errors)
            elif 'submit_producto' in request.POST:
                form_producto = formProducto(request.POST)
                if form_producto.is_valid():
                    form_producto.save()
                    print("Producto creado exitosamente.")
                    return redirect(f'/administrar/{usuario.rut}/')
                else:
                    print("Error al crear el producto. Verifique los datos.")
                    print(form_producto.errors)

        # Datos que se pasarán al template
        data = {
            'usuario': usuario,
            'form_equipo': form_equipo,
            'form_clase_grupal': form_clase_grupal,
            'form_producto': form_producto,
            'entrenadores': entrenadores,
            'clasesGrupales': clasesGrupales,
            'personal' : personal,
        }
    except administrador.DoesNotExist:
        print("Usuario no encontrado.")  # Mensaje de error en consola
        return redirect('/inicio_de_Sesion/')

    return render(request, 'primerApp/administrador.html', data)
