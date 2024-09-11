from django.db import models

class Referenciado(models.Model):
    cod_refe = models.BigIntegerField(
        primary_key= True
    )
    cod_empr = models.BigIntegerField()
    cod_ccos = models.ForeignKey(
        'core.CentroCosto',
        on_delete=models.CASCADE
    )
    nom_refe = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    act_inac = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    ref_cost = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    des_refe = models.CharField(
        max_length=240,
        null=True,
        blank=True
    )
    ref_refe = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )    
    act_usua = models.CharField(
        max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(cod_refe__gte=0), name="gnc21refer"),
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name="gnc22refer"),
            models.CheckConstraint(check=models.Q(act_inac__in=['N', 'S']), name="gnc23refer"),
        ]
        unique_together = (('cod_empr', 'cod_ccos'),)
        db_table = 'referenciado'
