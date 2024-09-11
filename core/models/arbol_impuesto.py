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
        db_table = 'arbol_impuesto'
        unique_together = (('cod_empr', 'cod_arbo', 'ide_arbo'),)
        constraints = [
            models.CheckConstraint(check=models.Q(cod_arbo__gte=0), name='check_cod_arbo'),
            models.CheckConstraint(check=models.Q(can_nive__gte=0), name='check_can_nive'),
            models.CheckConstraint(check=models.Q(cap_fija__in=['N', 'S']), name='check_cap_fija'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='ai_check_act_esta'),
        ]
