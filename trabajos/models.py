from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Jurado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class TrabajoDeGrado(models.Model):
    nombre = models.CharField(max_length=255)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)
    profesores = models.ManyToManyField(Profesor, blank=True)
    jurados = models.ManyToManyField(Jurado, blank=True)
    asesores = models.ManyToManyField(Asesor, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    vigente = models.BooleanField(default=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)  # Para investigación formativa
    actividades = models.ManyToManyField('Actividad', blank=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.nombre
    
class Evaluacion(models.Model):
    trabajo = models.ForeignKey(TrabajoDeGrado, on_delete=models.CASCADE)
    jurados = models.ForeignKey(Jurado, on_delete=models.CASCADE, null=True, blank=True)
    calificacion = models.FloatField()

    def __str__(self):
        return f"{self.trabajo} - {self.jurados}: {self.calificacion}"
