from django.db import models

class CajaCompensacion(models.Model):
    id_caja_compe = models.AutoField(primary_key=True)
    
    cod_caja_compe = models.IntegerField(
        default=0,
        help_text="Código interno asignado a la caja de compensación"
    )
    
    nit_caja = models.ForeignKey(
        'core.Tercero',
        on_delete=models.CASCADE,
        limit_choices_to={'estado_activo': True},  # Solo selecciona terceros activos
        help_text="NIT de la empresa de la caja de compensación"
    )
    
    desc_caja = models.CharField(
        max_length=50,
        default='0',
        help_text="Nombre de la caja de compensación"
    )
    
    codi_caja_compe = models.CharField(
        max_length=50,
        default='0',
        help_text="Código establecido para las entidades"
    )

    class Meta:
        db_table = 'aper_cajas_compensa'