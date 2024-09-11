from django.db import models


class Zona(models.Model):
    id_zona = models.DecimalField(max_digits=30, decimal_places=0, primary_key=True)
    cod_zona = models.CharField(max_length=2)
    cod_bode = models.ForeignKey(bodega, on_delete=models.CASCADE, to_field='cod_bode')
    nom_zona = models.CharField(max_length=50)
    tip_zona = models.CharField(max_length=1)
    act_usua = models.CharField(max_length=50, null=True, blank=True)
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        db_table = 'zona'
