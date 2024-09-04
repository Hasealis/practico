from django.db import models

class Tercero(models.Model):
    id = models.AutoField(primary_key=True)
    
    # Información del documento
    tipo_de_documento = models.CharField(max_length=1)
    numero_identificacion = models.BigIntegerField()
    digi_verifica = models.CharField(max_length=1, null=True, blank=True)
    
    # Información personal
    tipo_persona = models.BigIntegerField()
    nombre_tercero = models.CharField(max_length=255)
    primer_nombre = models.CharField(max_length=255)
    segundo_nombre = models.CharField(max_length=15, null=True)
    primer_apellido = models.CharField(max_length=255)
    segundo_apellido = models.CharField(max_length=15, null=True)
    
    # Información de contacto
    direc_tercero = models.CharField(max_length=255)
    direc_secundaria = models.CharField(max_length=255, null=True)
    tele_tercero = models.CharField(max_length=255)
    celu_tercero = models.CharField(max_length=15, null=True)
    mail_tercero = models.CharField(max_length=255)
    
    # Información adicional
    man_sucursal = models.BooleanField()
    tipo_tercero = models.CharField(max_length=255)
    
    # Ubicación
    pais_tercero = models.BigIntegerField()
    depart_tercero = models.BigIntegerField()
    ciudad_tercero = models.BigIntegerField()

    def __str__(self):
        return self.nombre_tercero

    class Meta:
        db_table = 'core_tercero'
        unique_together = ['tipo_de_documento', 'numero_identificacion']