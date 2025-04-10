from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre}({self.telefono})"
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
class Habilidad (models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre}"
class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    antiguedad = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    imagen = models.ImageField(upload_to="empleados/", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.antiguedad})"