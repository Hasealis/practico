from django.db import models

class banco(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_banc = models.SmallIntegerField()
    cod_comp = models.SmallIntegerField()
    nit_banc = models.ForeignKey(tercero, on_delete=models.CASCADE)  # Relación con la tabla Tercero
    nom_banc = models.CharField(max_length=40)
    tip_banc = models.CharField(max_length=1)
    por_cotr = models.CharField(max_length=1)
    val_cotr = models.DecimalField(max_digits=28, decimal_places=6)
    dig_conc = models.SmallIntegerField()
    cod_achs = models.CharField(max_length=9)
    cod_form = models.SmallIntegerField(null=True, blank=True)
    cod_asib = models.CharField(max_length=1, default='0')
    ref_banc = models.CharField(max_length=12)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_banc'], name='unique_cod_empr_cod_banc'),
            models.CheckConstraint(check=models.Q(tip_banc__in=['O', 'P']), name='check_tip_banc'),
            models.CheckConstraint(check=models.Q(por_cotr__in=['V', 'P']), name='check_por_cotr'),
            models.CheckConstraint(check=models.Q(val_cotr__gte=0), name='check_val_cotr'),
            models.CheckConstraint(check=models.Q(dig_conc__gt=0), name='check_dig_conc'),
        ]
