from django.db import models

class tipo_impuesto(models.Model):
    id_tipimpu = models.AutoField(primary_key=True)  # Campo autoincrementable primario
    cod_empr = models.SmallIntegerField()
    cod_tipo = models.SmallIntegerField()
    nom_tipo = models.CharField(max_length=60, null=True, blank=True)
    ini_tipo = models.CharField(max_length=10, null=True, blank=True)
    tip_oper = models.CharField(max_length=1, null=True, blank=True)
    tip_imp = models.CharField(max_length=2, null=True, blank=True)
    dig_redo = models.SmallIntegerField()
    act_inac = models.CharField(max_length=1, null=True, blank=True)
    man_base = models.CharField(max_length=1, null=True, blank=True)
    man_gara = models.CharField(max_length=1, null=True, blank=True)
    cod_imba = models.SmallIntegerField()
    imp_mava = models.CharField(max_length=1, null=True, blank=True)
    mod_base = models.CharField(max_length=1, null=True, blank=True)
    mod_afec = models.CharField(max_length=1, null=True, blank=True)
    bas_livb = models.CharField(max_length=1, null=True, blank=True)
    cal_imp = models.CharField(max_length=1, null=True, blank=True)
    pri_pres = models.SmallIntegerField()
    man_cont = models.CharField(max_length=1, null=True, blank=True)
    man_teri = models.CharField(max_length=1, null=True, blank=True)
    man_cdev = models.CharField(max_length=1, null=True, blank=True)
    man_desc = models.CharField(max_length=1, null=True, blank=True)
    des_ivmv = models.CharField(max_length=1)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_tipo'], name='unique_cod_empr_cod_tipo')
        ]
