from django.db import models

class GNRefer(models.Model):
    cod_empr = models.SmallIntegerField()
    id_ccos = models.ForeignKey(CentroCosto, on_delete=models.CASCADE)
    cod_refe = models.IntegerField()
    nom_refe = models.CharField(max_length=40, null=True, blank=True)
    act_inac = models.CharField(max_length=1, null=True, blank=True)
    ref_cost = models.CharField(max_length=1, null=True, blank=True)
    des_refe = models.CharField(max_length=240, null=True, blank=True)
    ref_refe = models.CharField(max_length=30, null=True, blank=True)    
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        constraints = [
           
            models.CheckConstraint(check=models.Q(cod_refe__gte=0), name="gnc21refer"),
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name="gnc22refer"),
            models.CheckConstraint(check=models.Q(act_inac__in=['N', 'S']), name="gnc23refer"),
        ]
        primary_key = models.CompositeKey("cod_empr","cod_ccos", "cod_refe")  # Necesitas usar una librería como django-compositekey para soportar claves compuestas
        db_table = 'GN_REFER'
