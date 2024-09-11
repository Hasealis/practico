from django.db import models

class AuxiliarCuentCont(models.Model):
    id_cuen = models.IntegerField(primary_key=True)  # Asegúrate de que este campo sea una clave primaria en la tabla auxiliar_cuent_cont

    class Meta:
        db_table = 'auxiliar_cuent_cont'

class ConceptoPago(models.Model):
    id_conpago = models.AutoField(primary_key=True)  # Campo autoincrementable primario
    cod_empr = models.SmallIntegerField()
    cod_conp = models.IntegerField()
    nom_conp = models.CharField(max_length=40)
    des_conp = models.CharField(max_length=240)
    id_cuen = models.ForeignKey(AuxiliarCuentCont, on_delete=models.CASCADE, db_column='ID_CUEN', to_field='id_cuen')
    est_acti = models.CharField(max_length=1)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'concepto_pago'
        unique_together = (('cod_empr', 'cod_conp'),)
        constraints = [
            models.CheckConstraint(check=models.Q(cod_conp__gte=0), name='check_cod_conp'),
            models.CheckConstraint(check=models.Q(est_acti__in=['I', 'A']), name='check_est_acti'),
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name='cp_check_act_esta'),
        ]
