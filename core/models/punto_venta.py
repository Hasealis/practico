from django.db import models

class PuntoVenta(models.Model):

    cod_empr = models.SmallIntegerField()   
    id_pvta = models.DecimalField(max_digits=30, decimal_places=0, primary_key=True) 
    cod_pvta = models.SmallIntegerField()
    nom_pvta = models.CharField(max_length=40, blank=True, null=True)
    ini_pvta = models.CharField(max_length=3, blank=True, null=True)
    cod_terc = models.DecimalField(max_digits=13, decimal_places=0)
    cod_pais = models.SmallIntegerField()
    cod_dpto = models.SmallIntegerField()
    cod_mpio = models.SmallIntegerField()
    dir_pvta = models.CharField(max_length=60, blank=True, null=True)
    tel_pvta = models.CharField(max_length=30, blank=True, null=True)    
    cod_ccos = models.SmallIntegerField()
    cod_refe = models.IntegerField()    
    man_ccos = models.CharField(max_length=1, blank=True, null=True)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'punto_venta'
        unique_together = ('cod_empr', 'cod_pvta')

    def __str__(self):
        return f'{self.cod_empr} - {self.cod_pvta}'

    def save(self, *args, **kwargs):        
        if self.cod_pvta < 0:
            raise ValueError("COD_PVTA must be greater than or equal to 0")
        
        super().save(*args, **kwargs)
