from django.db import models

class PAIS(models.Model):
    cod_pais = models.SmallIntegerField(primary_key=True)
    nom_pais = models.CharField(max_length=50)  # Suponiendo que hay un nombre para el país

    def __str__(self):
        return self.nom_pais

class DEPARTAMENTO(models.Model):
    cod_dpto = models.SmallIntegerField(primary_key=True)
    cod_pais = models.ForeignKey(PAIS, on_delete=models.CASCADE, to_field='cod_pais', related_name='departamentos')
    nom_dpto = models.CharField(max_length=50)  # Suponiendo que hay un nombre para el departamento

    def __str__(self):
        return self.nom_dpto

class CIUDAD(models.Model):
    cod_mpio = models.SmallIntegerField(primary_key=True)
    cod_dpto = models.ForeignKey(DEPARTAMENTO, on_delete=models.CASCADE, to_field='cod_dpto', related_name='ciudad')
    nom_mpio = models.CharField(max_length=50)  # Suponiendo que hay un nombre para la ciudad

    def __str__(self):
        return self.nom_mpio

class banco(models.Model):
    cod_empr = models.SmallIntegerField()
    cod_banc = models.SmallIntegerField()
    # Otros campos necesarios para banco

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cod_empr', 'cod_banc'], name='unique_cod_empr_cod_banc')
        ]

    def __str__(self):
        return f'Banco {self.cod_banc} - Empresa {self.cod_empr}'

class sucursal_banco(models.Model):
    id_sucurbanco = models.AutoField(primary_key=True)
    cod_empr = models.SmallIntegerField()
    cod_banc = models.ForeignKey(banco, on_delete=models.CASCADE, to_field='cod_banc', related_name='sucursales')
    cod_sban = models.SmallIntegerField()
    nom_sban = models.CharField(max_length=40)
    cod_pais = models.ForeignKey(PAIS, on_delete=models.CASCADE, to_field='cod_pais', related_name='sucursales')
    cod_dpto = models.ForeignKey(DEPARTAMENTO, on_delete=models.CASCADE, to_field='cod_dpto', related_name='sucursales')
    cod_mpio = models.ForeignKey(CIUDAD, on_delete=models.CASCADE, to_field='cod_mpio', related_name='sucursales')
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
            models.CheckConstraint(check=models.Q(act_esta__in=['B', 'M', 'A']), name='check_act_esta'),
        ]
        indexes = [
            models.Index(fields=['cod_empr', 'cod_banc', 'cod_sban']),
        ]

    def __str__(self):
        return f'{self.nom_sban} ({self.cod_sban})'
