class cuenta_bancaria(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_banc = models.ForeignKey(banco, on_delete=models.CASCADE, to_field='cod_banc', related_name='cuentas')
    cod_sban = models.ForeignKey(SUCURSAL_BANCO, on_delete=models.CASCADE, to_field='cod_sban', related_name='cuentas')
    cod_cueb = models.DecimalField(max_digits=18, decimal_places=0)
    cod_mone = models.ForeignKey(MONEDA, on_delete=models.CASCADE, to_field='cod_mone', related_name='cuentas')
    des_cueb = models.CharField(max_length=60)
    tip_cuen = models.CharField(max_length=1)
    cue_naci = models.CharField(max_length=1)
    rmt_cuen = models.IntegerField()
    man_sobr = models.CharField(max_length=1)
    cup_sobr = models.DecimalField(max_digits=28, decimal_places=6)
    act_inac = models.CharField(max_length=1)
    res_cuen = models.CharField(max_length=1)
    tip_caja = models.CharField(max_length=1)
    mas_ctab = models.CharField(max_length=1)
    cod_terc = models.ForeignKey(TERCERO, on_delete=models.CASCADE, to_field='cod_terc', related_name='cuentas')
    cod_ccos = models.ForeignKey(CENTRO_COSTO, on_delete=models.CASCADE, to_field='cod_ccos', related_name='cuentas')
    cod_refe = models.ForeignKey(REFERENCIADO, on_delete=models.CASCADE, to_field='cod_refe', related_name='cuentas')
    cue_sate = models.CharField(max_length=1)
    cue_cont = models.ForeignKey(AUXILIAR_CUENT_CONT, on_delete=models.CASCADE, to_field='cue_cont', related_name='cuentas')
    sal_cueb = models.DecimalField(max_digits=28, decimal_places=6, default=0)
    val_pago = models.DecimalField(max_digits=28, decimal_places=6, default=0)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_banc', 'cod_sban', 'cod_cueb'], name='unique_cod_empr_cod_banc_cod_sban_cod_cueb'),
            models.CheckConstraint(check=models.Q(cod_cueb__gte=0), name='check_cod_cueb'),
            models.CheckConstraint(check=models.Q(tip_cuen__in=['A', 'C', 'I', 'F', 'N']), name='check_tip_cuen'),
            models.CheckConstraint(check=models.Q(cue_naci__in=['N', 'S']), name='check_cue_naci'),
            models.CheckConstraint(check=models.Q(man_sobr__in=['N', 'S']), name='check_man_sobr'),
            models.CheckConstraint(check=models.Q(cup_sobr__gte=0), name='check_cup_sobr'),
            models.CheckConstraint(check=models.Q(act_inac__in=['I', 'A']), name='check_act_inac'),
            models.CheckConstraint(check=models.Q(res_cuen__in=['S', 'N']), name='check_res_cuen')
        ]
        indexes = [
            models.Index(fields=['cod_empr', 'cod_banc', 'cod_sban', 'cod_cueb']),
        ]

    def __str__(self):
        return f'Cuenta {self.cod_cueb} - Sucursal {self.cod_sban}'
