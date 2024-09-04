from django.db import models

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    
    cod_califica = models.IntegerField(
        default=0,
        help_text="Código de la calificación"
    )
    
    descrip_califica = models.CharField(
        max_length=50,
        default='0',
        help_text="Descripción de la calificación"
    )

    class Meta:
        db_table = 'aper_calificacion'