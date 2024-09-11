from django.db import models

class BloqueoFecha(models.Model):
    cod_empr = models.SmallIntegerField()
    ano_bloq = models.SmallIntegerField()
    mes_bloq = models.SmallIntegerField()
    est_bloq = models.CharField(max_length=1)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'bloqueo_fecha'
        unique_together = ('cod_empr', 'ano_bloq', 'mes_bloq')
