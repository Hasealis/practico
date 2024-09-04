from django.db import models

class ActividadEconomica(models.Model):
    id = models.AutoField(primary_key=True)
    agrup_tari = models.IntegerField(null=True, blank=True)
    codigo_actividad_economica_219 = models.CharField(max_length=50, null=True, blank=True)
    codigo_actividad_economica_decl = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=700, null=True, blank=True)
    tarifa_por_mil = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    # ciudad = models.ForeignKey(
    #     'Ciudad',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    ciudad = models.IntegerField()
    # cuenta_ica = models.ForeignKey(
    #     'core.CuentaICA',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    cuenta_ica = models.IntegerField()

    class Meta:
        db_table = 'core_actividadeconomica'
        verbose_name = 'Actividad Económica'
        verbose_name_plural = 'Actividades Económicas'

    def __str__(self):
        return f"{self.descripcion or 'Actividad Económica sin descripción'}"