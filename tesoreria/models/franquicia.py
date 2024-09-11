from django.db import models

class Franquicia(models.Model):
    id_fran = models.AutoField(primary_key=True)  # Campo autoincrementable
    cod_empr = models.SmallIntegerField()
    cod_fran = models.SmallIntegerField()
    nom_fran = models.CharField(max_length=50)
    ref_fran = models.CharField(max_length=20) #Referencia Franquicia ejemplo VISA
    cod_banc = models.ForeignKey(
        'tesoreria.Banco',
        on_delete=models.CASCADE,
        db_column='cod_banc',
        to_field='cod_banc'
    )
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'franquicia'
        unique_together = (('cod_empr', 'cod_fran'),)
        constraints = [
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name='fr_check_act_esta'),
        ]
