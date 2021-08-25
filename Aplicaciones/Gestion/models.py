from django.db import models

class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '{0}'.format(self.nombre)

class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=15)
    apellidoMaterno = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    sexos = [
        ('F','femenino'),
        ('M','masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0} {1},{2}"
        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombre)

    def __str__(self):
        return self.nombreCompleto()
    
class Telefono(models.Model):
    persona = models.ForeignKey(Persona,null=False, blank=False, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return '{0} ({1})'.format(self.telefono,self.persona)

class Email(models.Model):
    persona = models.ForeignKey(Persona,null=False, blank=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=91)

    def __str__(self):
        return '{0} ({1})'.format(self.email,self.persona)