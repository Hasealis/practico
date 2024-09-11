from django.db import models

class RelacionNivel(models.Model):
    id_relanive = models.BigAutoField
    cod_empr = models.SmallIntegerField()
    rmt_aniv = models.IntegerField()
    cod_arbo = models.ForeignKey(
        'core.ArbolImpuesto',
        on_delete=models.CASCADE
    )
    ide_arbo = models.CharField(max_length=2, null=True, blank=True)
    num_nive = models.SmallIntegerField()
    cod_nive = models.ForeignKey(
        'core.NivelImpuesto',
        on_delete=models.CASCADE
    )
    rmt_ante = models.IntegerField()
    abs_inde = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    act_usua = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    act_hora = models.DateTimeField()
    act_esta = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='rn_check_act_esta')
        ]
