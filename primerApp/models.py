from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class administrador(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=150)

class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, unique=True)
    rol = models.CharField(max_length=30)
    fechaIngreso = models.DateField()
    imgReferencia = models.ImageField(upload_to='static/img/equipo/',blank=True, null=True)
    bio = models.TextField()
    #lamina ejecutiva de la arquitectura del sistema
    #casos de uso de cada funcionalidad critica
    #1. arquitectura del sistema y semaforisacion de las funcionalidades criticas
    #aplicacion de las reglas owasp para cada funcinalidad

class claseGrupal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_Inicio = models.DateField(default="2024-01-01")
    fecha_Fin = models.DateField(default="2024-01-01")
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    max_participantes = models.PositiveIntegerField()
    entrenador = models.ForeignKey(
        equipo, 
        on_delete=models.CASCADE, 
        related_name="clases_grupales", 
        to_field="rut"  # Usamos el campo 'rut' para la relación
    )  
    lugar = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imgReferencia = models.ImageField(upload_to='static/img/clasesGrupales/',blank=True, null=True)
    archivar = models.BooleanField(default=False)

class solicitudCG(models.Model):
    CG = models.ForeignKey(claseGrupal, on_delete=models.CASCADE, related_name="solicitudes")
    nombreCompleto = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1)  # "M", "F" , "O"
    correoElectronico = models.EmailField()
    telefono = models.CharField(max_length=12)
    condicionMedica = models.TextField(blank=True)
    contactoEmergenciaNombre = models.CharField(max_length=100)
    contactoEmergenciaTelefono = models.CharField(max_length=12)
    acepta_reglamento = models.BooleanField(default=False)
    acepta_uso_imagen = models.BooleanField(default=False)
    estado = models.BooleanField(default=False)  # False para "pendiente", True para "aceptada"
    fechaSolicitud = models.DateTimeField(auto_now_add=True)

class solicitudEP(models.Model):
    pass

class cliente(models.Model):
    nombreCompleto = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, unique=True)

class integra(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name="clases")
    clase_grupal = models.ForeignKey(claseGrupal, on_delete=models.CASCADE, related_name="participantes")
    solicitud = models.OneToOneField(solicitudCG, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_union = models.DateTimeField(auto_now_add=True)


class entrenamientoPersonalizado(models.Model):
    pass

class producto(models.Model):
    nombre = models.CharField(max_length=100,default='pikochu')
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to="static/img/productos/", blank=True, null=True)
    disponible = models.BooleanField(default=True)

class renta(models.Model):
    pass
