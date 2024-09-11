from django.db import models

class ArbolImpuesto(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_arbo = models.SmallIntegerField()
    ide_arbo = models.CharField(max_length=2)
    nom_arbo = models.CharField(max_length=40, null=True, blank=True)
    can_nive = models.SmallIntegerField()
    cap_fija = models.CharField(max_length=1, null=True, blank=True)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_arbo', 'ide_arbo'], name='unique_arbol')
        ]

class NivelImpuesto(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_arbo = models.SmallIntegerField()
    ide_arbo = models.CharField(max_length=2)
    num_nive = models.SmallIntegerField()
    cod_nive = models.IntegerField()
    nom_nive = models.CharField(max_length=40, null=True, blank=True)
    nro_nodo = models.IntegerField(default=0, null=True, blank=True)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_arbo', 'ide_arbo', 'num_nive', 'cod_nive'], name='unique_nivel'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='check_act_esta')
        ]

class RelacionNivel(models.Model):
    id_relanive = models.AutoField(primary_key=True)
    cod_empr = models.SmallIntegerField()
    rmt_aniv = models.IntegerField()
    cod_arbo = models.ForeignKey(ArbolImpuesto, on_delete=models.CASCADE)
    ide_arbo = models.CharField(max_length=2, null=True, blank=True)
    num_nive = models.SmallIntegerField()
    cod_nive = models.ForeignKey(NivelImpuesto, on_delete=models.CASCADE)
    rmt_ante = models.IntegerField()
    abs_inde = models.IntegerField(default=0, null=True, blank=True)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='check_act_esta')
        ]
