from django.db import models

class RelaEmpreClien(models.Model):
    id_relaemprclien = models.AutoField(primary_key=True)
    cod_empr = models.SmallIntegerField()
    rmt_remc = models.IntegerField()
    rmt_empr = models.IntegerField()
    cod_arbo = models.SmallIntegerField()
    ide_arbo = models.CharField(max_length=2)
    rmt_nive = models.IntegerField()
    cod_niv1 = models.IntegerField(default=0)
    cod_niv2 = models.IntegerField(default=0)
    cod_niv3 = models.IntegerField(default=0)
    cod_niv4 = models.IntegerField(default=0)
    cod_niv5 = models.IntegerField(default=0)
    cod_niv6 = models.IntegerField(default=0)
    cod_niv7 = models.IntegerField(default=0)
    cod_niv8 = models.IntegerField(default=0)
    cod_niv9 = models.IntegerField(default=0)
    cod_ni10 = models.IntegerField(default=0)
    cod_ni11 = models.IntegerField(default=0)
    cod_ni12 = models.IntegerField(default=0)
    cod_ni13 = models.IntegerField(default=0)
    cod_ni14 = models.IntegerField(default=0)
    cod_ni15 = models.IntegerField(default=0)
    cod_ni16 = models.IntegerField(default=0)
    cod_ni17 = models.IntegerField(default=0)
    cod_ni18 = models.IntegerField(default=0)
    cod_ni19 = models.IntegerField(default=0)
    cod_ni20 = models.IntegerField(default=0)
    cod_tipo = models.SmallIntegerField()
    man_imp = models.CharField(max_length=1, choices=[('N', 'No'), ('S', 'Sí')])
    man_cont = models.CharField(max_length=1, choices=[('N', 'No'), ('S', 'Sí')])
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1, choices=[('M', 'Modificado'), ('A', 'Activo')])

    class Meta:
        unique_together = (('cod_empr', 'rmt_empr', 'rmt_nive', 'cod_tipo'),)
        indexes = [
            models.Index(fields=['cod_empr', 'rmt_remc', 'rmt_empr', 'rmt_nive', 'cod_tipo']),
        ]

    def __str__(self):
        return f"RELAEMPRECLIEN {self.id_relaempreclien}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if not (self.man_imp in ['N', 'S']):
            raise ValidationError('man_imp must be "N" or "S"')

        if not (self.man_cont in ['N', 'S']):
            raise ValidationError('man_cont must be "N" or "S"')

        if not (self.act_esta in ['M', 'A']):
            raise ValidationError('act_esta must be "M" or "A"')
