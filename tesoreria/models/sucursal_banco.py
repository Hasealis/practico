from django.db import models

class SucursalBanco(models.Model):
    cod_sban = models.BigIntegerField(
        primary_key=True
    )
    cod_empr = models.SmallIntegerField()
    cod_banc = models.ForeignKey(
        'tesoreria.Banco',
        on_delete=models.CASCADE,
        to_field='cod_banc',
        related_name='sucursales'
    )
    nom_sban = models.CharField(max_length=40)
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
    dir_sban = models.CharField(max_length=40)
    tel_sban = models.CharField(max_length=30)    
    dir_mail = models.CharField(max_length=120)
    ctc_sban = models.CharField(max_length=40)    
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_banc', 'cod_sban'], name='unique_cod_empr_cod_banc_cod_sban'),
            models.CheckConstraint(check=models.Q(cod_sban__gte=0), name='check_cod_sban'),
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name='su_check_act_esta'),
        ]
        indexes = [
            models.Index(fields=['cod_empr', 'cod_banc', 'cod_sban']),
        ]

    def __str__(self):
        return f'{self.nom_sban} ({self.cod_sban})'
