from django.db import models

class NivelImpuesto(models.Model):
    cod_empr = models.SmallIntegerField()
    #cod_arbo = models.ForeignKey
    id_arbol = models.CharField(max_length=2)
    num_nive = models.SmallIntegerField()
    cod_nive = models.IntegerField()
    nom_nive = models.CharField(max_length=40, null=True, blank=True)
    nro_nodo = models.IntegerField(default=0, null=True, blank=True)
    act_usua = models.CharField(max_length=8, null=True, blank=True)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, null=True, blank=True)

    id_nivimpu = models.AutoField(primary_key=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(cod_nive__gte=0), name='cod_nive_positive'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='act_esta_valid'),
        ]
        indexes = [
            models.Index(fields=['cod_empr',
                                #   'cod_arbo',
                                  'id_arbol', 'num_nive', 'cod_nive']),
        ]
