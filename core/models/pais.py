from django.db import models

class Pais(models.Model):
    cod_pais = models.SmallIntegerField(primary_key=True)
    
    nom_pais = models.CharField(
        max_length=40, 
        null=True, 
        help_text="Nombre del país"
    )
    
    abr_pais = models.CharField(
        max_length=8, 
        null=True, 
        help_text="Abreviatura del país"
    )
    
    ind_pais = models.IntegerField(
        help_text="Indicador del país"
    )
    
    cod_mone = models.SmallIntegerField(
        help_text="Código de la moneda"
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
        db_table = 'pais'
        constraints = [
            models.CheckConstraint(check=models.Q(cod_pais__gte=0), name='GNC01PAISE'),
            models.CheckConstraint(check=models.Q(ind_pais__gte=0), name='GNC02PAISE'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='GNC03PAISE')
        ]
