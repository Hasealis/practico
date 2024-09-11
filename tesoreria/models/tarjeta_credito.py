from django.db import models

class TarjetaCredito(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_banc = models.ForeignKey(
        'tesoreria.Banco',
        on_delete=models.CASCADE,
        db_column='cod_banc',
        to_field='cod_banc'
    )
    cod_tacr = models.SmallIntegerField()
    nom_tacr = models.CharField(max_length=40)
    cod_pais = models.ForeignKey(
        'core.Pais',
        on_delete=models.CASCADE,
        db_column='cod_pais'
    )
    #PONER RELACION A TABLA DE DEPARTAMENTO
    cod_dpto = models.IntegerField(
        # Departamento,
        # on_delete=models.CASCADE,
        db_column='cod_dpto'
    )
    cod_mpio = models.ForeignKey(
        'core.Ciudad',
        on_delete=models.CASCADE,
        db_column='cod_mpio'
    )
    dir_tacr = models.CharField(max_length=60)
    tel_tacr = models.CharField(max_length=30)
    aae_tacr = models.CharField(max_length=10)
    cod_imco = models.ForeignKey(
        'core.Impuesto',
        on_delete=models.CASCADE,
        db_column='cod_imco'
    )
    cod_imre = models.ForeignKey(
        'core.Impuesto',
        on_delete=models.CASCADE,
        related_name='cod_imre',
        db_column='cod_imre'
    )
    cod_imiv = models.ForeignKey(
        'core.Impuesto',
        on_delete=models.CASCADE,
        related_name='cod_imiv',
        db_column='cod_imiv'
    )
    cod_reiv = models.ForeignKey(
        'core.Impuesto',
        on_delete=models.CASCADE,
        related_name='cod_reiv',
        db_column='cod_reiv'
    )
    tip_tarc = models.CharField(max_length=1)
    ban_cons = models.SmallIntegerField()
    sba_cons = models.SmallIntegerField()
    cue_cons = models.DecimalField(max_digits=18, decimal_places=0)
    ind_edic = models.CharField(max_length=1)
    cod_reic = models.IntegerField()
    tip_liqu = models.CharField(max_length=1)
    val_comi = models.DecimalField(max_digits=28, decimal_places=6)
    rmt_comi = models.IntegerField()
    cla_tarc = models.CharField(max_length=1)
    rmt_publ = models.IntegerField()
    rmt_priv = models.IntegerField()
    rmt_conv = models.IntegerField()
    cco_cota = models.SmallIntegerField()
    ref_cota = models.IntegerField()
    act_inac = models.CharField(max_length=1)
    cod_fran = models.SmallIntegerField()
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'TarjetaCredito'
        unique_together = (('cod_empr', 'cod_tacr'),)
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_tacr'], name='unique_tarcr'),
            models.CheckConstraint(check=models.Q(act_esta__in=['A', 'M', 'B']), name='tc_check_act_esta'),
            models.CheckConstraint(check=models.Q(cod_tacr__gte=0), name='check_cod_tacr'),
            models.CheckConstraint(check=models.Q(tip_tarc__in=['I', 'T', 'D']), name='check_tip_tarc'),
            models.CheckConstraint(check=models.Q(ind_edic__in=['N', 'S']), name='check_ind_edic'),
        ]
