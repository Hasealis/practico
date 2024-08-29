from django.db import models

class Tercero(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    primer_nombre = models.CharField(
        max_length=255
    )
    segundo_nombre = models.CharField(
        max_length = 15,
        null=True
    )
    tipo_de_documento = models.CharField(
        max_length = 1
    )
    numero_identificacion = models.BigIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'core_tercero'
        unique_together = ['tipo_de_documento', 'numero_identificacion']
    
