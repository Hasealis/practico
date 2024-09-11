from django.db import models

class Moneda(models.Model):
    cod_mone = models.SmallIntegerField(primary_key=True)
    
    nom_mone = models.CharField(
        max_length=40, 
        null=True, 
        help_text="Nombre de la moneda"
    )
    
    ini_mone = models.CharField(
        max_length=3, 
        null=True, 
        unique=True, 
        help_text="Iniciales de la moneda"
    )
    
    num_deci = models.SmallIntegerField(
        help_text="Número de decimales"
    )
    
    act_usua = models.CharField(
        max_length=8, 
        null=True, 
        help_text="Último usuario que realizó modificaciones"
    )
    
    act_hora = models.DateTimeField(
        help_text="Fecha y hora de la última modificación"
    )
    
    act_esta = models.CharField(
        max_length=1, 
        null=True, 
        choices=[('M', 'Modificado'), ('A', 'Activo')],
        help_text="Estado de la actividad (M = Modificado, A = Activo)"
    )

    class Meta:
        db_table = 'moneda'
        constraints = [
            models.CheckConstraint(check=models.Q(cod_mone__gte=0), name='GNC01MONED'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='GNC02MONED')
        ]
        indexes = [
            models.Index(fields=['ini_mone'], name='GNU01MONED')
        ]
