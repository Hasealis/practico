from django.db import models

class CentroCosto(models.Model):
    cod_ccos = models.AutoField(primary_key=True)
    cod_empr = models.SmallIntegerField(help_text="Código de la empresa")
    ref_ccos = models.CharField(
        # max_length=10
    )
    nom_ccos = models.CharField(max_length=60, help_text="Nombre del centro de costo")
    dir_ccos = models.CharField(max_length=60, help_text="Dirección del centro de costo")
    tel_ccos = models.CharField(max_length=30, help_text="Teléfono del centro de costo")
    act_inac = models.CharField(max_length=1, choices=[('N', 'Inactivo'), ('S', 'Activo')], help_text="Activo o Inactivo")
    act_usua = models.CharField(max_length=8, help_text="Usuario que realizó la última modificación")
    act_hora = models.DateTimeField(help_text="Fecha y hora de la última modificación")
    act_esta = models.CharField(max_length=1, help_text="Estado de la actividad")

    class Meta:
        db_table = 'centro_costo'
        unique_together = ('cod_empr', 'ref_ccos')
        constraints = [
            models.CheckConstraint(check=models.Q(act_inac__in=['N', 'S']), name="GNC10CCOST"),
        ]
        indexes = [
            models.Index(fields=['cod_empr', 'cod_ccos'], name="GNP01CCOST"),
        ]

    def __str__(self):
        return self.nom_ccos



