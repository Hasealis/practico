from django.db import models

class Ciudad(models.Model):
    cod_pais = models.SmallIntegerField(
        help_text="Código del país"
    )
    
    cod_dpto = models.SmallIntegerField(
        help_text="Código del departamento"
    )
    
    cod_mpio = models.SmallIntegerField(
        help_text="Código del municipio"
    )
    
    nom_mpio = models.CharField(
        max_length=30, 
        null=True, 
        help_text="Nombre del municipio"
    )
    
    ind_mpio = models.IntegerField(
        help_text="Indicador del municipio"
    )
    
    cod_iata = models.CharField(
        max_length=5, 
        null=True, 
        help_text="Código IATA"
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
    
    des_lati = models.DecimalField(
        max_digits=28, 
        decimal_places=9, 
        null=True, 
        help_text="Latitud del municipio"
    )
    
    des_long = models.DecimalField(
        max_digits=28, 
        decimal_places=9, 
        null=True, 
        help_text="Longitud del municipio"
    )
    
    class Meta:
        db_table = 'ciudad'
        unique_together = ['cod_pais', 'cod_dpto', 'cod_mpio']
        constraints = [
            models.CheckConstraint(check=models.Q(cod_dpto__gte=0), name='GNC01CIUDAD'),
            models.CheckConstraint(check=models.Q(cod_mpio__gte=0), name='GNC02CIUDAD'),
            models.CheckConstraint(check=models.Q(ind_mpio__gte=0), name='GNC03CIUDAD')
        ]
        indexes = [
            models.Index(fields=['cod_pais', 'cod_dpto', 'cod_mpio'], name='GNP01CIUDAD')
        ]
    
    def __str__(self):
        return self.nom_mpio if self.nom_mpio else f"Municipio {self.cod_mpio}"

class Pais(models.Model):
    cod_pais = models.SmallIntegerField(primary_key=True)
    # Otros campos de la tabla pais según sea necesario

    class Meta:
        db_table = 'pais'
