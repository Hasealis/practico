from django.db import models

class TipoImpuesto(models.Model):
    cod_tipo = models.SmallIntegerField(primary_key=True)
    # Define otros campos necesarios para la tabla TIPO_IMPUESTO

class AuxiliarCuentaCont(models.Model):
    cue_cont = models.IntegerField(primary_key=True)
    # Define otros campos necesarios para la tabla auxiliar_cuent_cont

class Impuesto(models.Model):
    id_impuesto = models.AutoField(primary_key=True)  # Campo autoincrementable primario
    cod_empr = models.SmallIntegerField()
    cod_impu = models.SmallIntegerField()
    nom_impu = models.CharField(max_length=40, null=True, blank=True)
    cod_tipo = models.ForeignKey(TipoImpuesto, on_delete=models.CASCADE)  # Seleccionable de la tabla TipoImpuesto
    tip_fact = models.CharField(max_length=1, null=True, blank=True)
    val_impu = models.DecimalField(max_digits=28, decimal_places=6)
    por_impu = models.DecimalField(max_digits=5, decimal_places=2)
    bas_impu = models.IntegerField()
    val_base = models.DecimalField(max_digits=28, decimal_places=6)
    cue_impu = models.ForeignKey(AuxiliarCuentaCont, related_name='cue_impu_set', on_delete=models.CASCADE)  # Seleccionable de la tabla auxiliar_cuent_cont
    cue_cruz = models.ForeignKey(AuxiliarCuentaCont, related_name='cue_cruz_set', on_delete=models.CASCADE)  # Seleccionable de la tabla auxiliar_cuent_cont
    tip_impu = models.CharField(max_length=2, null=True, blank=True)
    res_ciud = models.CharField(max_length=1, null=True, blank=True)
    cod_terc = models.DecimalField(max_digits=13, decimal_places=0)
    cue_devo = models.ForeignKey(AuxiliarCuentaCont, related_name='cue_devo_set', on_delete=models.CASCADE)  # Seleccionable de la tabla auxiliar_cuent_cont
    man_desc = models.CharField(max_length=1, default='N')
    cod_rete = models.SmallIntegerField(null=True, blank=True, default=0)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_tipo', 'cod_impu'], name='unique_cod_empr_cod_tipo_cod_impu'),
            models.CheckConstraint(check=models.Q(cod_impu__gte=0), name='check_cod_impu_non_negative'),
            models.CheckConstraint(check=models.Q(por_impu__gte=0), name='check_por_impu_non_negative'),
            models.CheckConstraint(check=models.Q(bas_impu__gt=0), name='check_bas_impu_positive'),
            models.CheckConstraint(check=models.Q(val_base__gte=0), name='check_val_base_non_negative'),
            models.CheckConstraint(check=models.Q(tip_impu__in=['CE', 'TI', 'RT', 'RV', 'RC', 'IV', 'OT']), name='check_tip_impu_valid'),
            models.CheckConstraint(check=models.Q(res_ciud__in=['S', 'N']), name='check_res_ciud_valid'),
            models.CheckConstraint(check=models.Q(act_esta__in=['A', 'M']), name='check_act_esta_valid'),
            models.CheckConstraint(check=models.Q(tip_fact__in=['V', 'P', 'U', 'R']), name='check_tip_fact_valid'),
            models.CheckConstraint(check=models.Q(val_impu__gte=0), name='check_val_impu_non_negative')
        ]
