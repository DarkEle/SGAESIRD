from django.db import models
from django.utils import timezone

# Create your models here.


class Universidades(models.Model):
	nombre=models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	OPCIONES_ROL = (
        ('A','Administrador'),
        ('E','Empaque'),
        ('E','Reemplazo'),
    )
	OPCIONES_ACTIVIDAD = (
		('A','Activo'),
		('V','Vacaciones'),
		('S','Suspendido'),
		('E','Eliminado')
	)
	id_Usuario = models.AutoField(primary_key=True, help_text="ID")
	rut = models.IntegerField()
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	rol = models.CharField(max_length=1, choices=OPCIONES_ROL)
	fecha_ingreso = models.DateTimeField(default=timezone.now)
	carrera = models.CharField(max_length=200)
	universidad = models.ForeignKey(Universidades, on_delete=models.CASCADE)
	activo = models.CharField(max_length=1, choices=OPCIONES_ACTIVIDAD)
	telefono = models.CharField(max_length=12)
	cant_turnos_disponibles = models.IntegerField()

	def __str__(self):
		return self.nombre + " " + self.apellido


class Categoria_anotaciones(models.Model):
	id_Categoria_anotaciones = models.AutoField(primary_key=True, help_text="ID")
	nombre_anotacion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre_anotacion

class Anotaciones(models.Model):
	id_Anotaciones = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateTimeField(default=timezone.now)
	categoria_anotaciones = models.ForeignKey(Categoria_anotaciones, on_delete=models.CASCADE)
	turnos_restados = models.IntegerField()
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	def __str__(self):
		return self.fecha + " " + self.categoria_anotaciones + " " + self.usuario

class Turnos(models.Model):
	id_Turnos = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	hora_inicio = models.TimeField()
	hora_final = models.TimeField()
	usuario = models.ManyToManyField(Usuario, blank=True)
	def __str__(self):
		return self.fecha + " " + self.hora_inicio + " " + self.hora_final

class Finanzas(models.Model):
	id_Finanzas = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	comentario = models.TextField()
	cantidad = models.IntegerField()
	total = models.IntegerField()
	responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	def __str__(self):
		return self.fecha.strftime("%d/%m/%Y") + " " + self.comentario + " " + str(self.cantidad)

class Anuncios(models.Model):
	id_Anuncios = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	usuario = models.ForeignKey(Usuario, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.fecha + " " + self.titulo

class Comentarios(models.Model):
	id_Comentarios = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	contenido = models.TextField()
	anuncio = models.ForeignKey(Anuncios, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.fecha + " " + self.anuncio

class Lista_de_Espera(models.Model):
	id_Lista_de_Espera = models.AutoField(primary_key=True, help_text="ID")
	fecha_ingreso = models.DateTimeField(default=timezone.now)
	rut = models.IntegerField()
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	carrera = models.CharField(max_length=200)
	universidad = models.ForeignKey(Universidades, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=12)
	def __str__(self):
		return self.nombre + " " + self.apellido