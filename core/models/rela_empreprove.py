from django.db import models

class RelaEmpreprove(models.Model):
    id_relaemprprove = models.AutoField(primary_key=True)
    cod_empr = models.SmallIntegerField()
    rmt_remp = models.IntegerField()
    rmt_empr = models.IntegerField()
    cod_arbo = models.SmallIntegerField()
    ide_arbo = models.CharField(max_length=2)
    rmt_nive = models.IntegerField()
    cod_niv1 = models.IntegerField()
    cod_niv2 = models.IntegerField()
    cod_niv3 = models.IntegerField()
    cod_niv4 = models.IntegerField()
    cod_niv5 = models.IntegerField()
    cod_niv6 = models.IntegerField()
    cod_niv7 = models.IntegerField()
    cod_niv8 = models.IntegerField()
    cod_niv9 = models.IntegerField()
    cod_ni10 = models.IntegerField()
    cod_ni11 = models.IntegerField()
    cod_ni12 = models.IntegerField()
    cod_ni13 = models.IntegerField()
    cod_ni14 = models.IntegerField()
    cod_ni15 = models.IntegerField()
    cod_ni16 = models.IntegerField()
    cod_ni17 = models.IntegerField()
    cod_ni18 = models.IntegerField()
    cod_ni19 = models.IntegerField()
    cod_ni20 = models.IntegerField()
    cod_tipo = models.SmallIntegerField()
    man_impu = models.CharField(max_length=1)
    man_cont = models.CharField(max_length=1)
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)
    
    class Meta:
        unique_together = ('cod_empr', 'rmt_empr', 'rmt_nive', 'cod_tipo')
        constraints = [
            models.CheckConstraint(check=models.Q(man_impu__in=['N', 'S']), name='check_man_impu'),
            models.CheckConstraint(check=models.Q(man_cont__in=['N', 'S']), name='check_man_cont'),
            models.CheckConstraint(check=models.Q(act_esta__in=['M', 'A']), name='re_check_act_esta'),
            models.CheckConstraint(check=models.Q(cod_niv1__gte=0), name='check_cod_niv1'),
            models.CheckConstraint(check=models.Q(cod_niv2__gte=0), name='check_cod_niv2'),
            models.CheckConstraint(check=models.Q(cod_niv3__gte=0), name='check_cod_niv3'),
            models.CheckConstraint(check=models.Q(cod_niv4__gte=0), name='check_cod_niv4'),
            models.CheckConstraint(check=models.Q(cod_niv5__gte=0), name='check_cod_niv5'),
            models.CheckConstraint(check=models.Q(cod_niv6__gte=0), name='check_cod_niv6'),
            models.CheckConstraint(check=models.Q(cod_niv7__gte=0), name='check_cod_niv7'),
            models.CheckConstraint(check=models.Q(cod_niv8__gte=0), name='check_cod_niv8'),
            models.CheckConstraint(check=models.Q(cod_niv9__gte=0), name='check_cod_niv9'),
            models.CheckConstraint(check=models.Q(cod_ni10__gte=0), name='check_cod_ni10'),
            models.CheckConstraint(check=models.Q(cod_ni11__gte=0), name='check_cod_ni11'),
            models.CheckConstraint(check=models.Q(cod_ni12__gte=0), name='check_cod_ni12'),
            models.CheckConstraint(check=models.Q(cod_ni13__gte=0), name='check_cod_ni13'),
            models.CheckConstraint(check=models.Q(cod_ni14__gte=0), name='check_cod_ni14'),
            models.CheckConstraint(check=models.Q(cod_ni15__gte=0), name='check_cod_ni15'),
            models.CheckConstraint(check=models.Q(cod_ni16__gte=0), name='check_cod_ni16'),
            models.CheckConstraint(check=models.Q(cod_ni17__gte=0), name='check_cod_ni17'),
            models.CheckConstraint(check=models.Q(cod_ni18__gte=0), name='check_cod_ni18'),
            models.CheckConstraint(check=models.Q(cod_ni19__gte=0), name='check_cod_ni19'),
            models.CheckConstraint(check=models.Q(cod_ni20__gte=0), name='check_cod_ni20'),
        ]

    def __str__(self):
        return f"{self.cod_empr}-{self.rmt_empr}-{self.rmt_nive}-{self.cod_tipo}"
