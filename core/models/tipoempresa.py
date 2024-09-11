from django.db import models

class TipoEmpresa(models.Model):
    id_tipempre = models.AutoField(primary_key=True)
    cod_tipempre = models.CharField(max_length=20, unique=True)  # Ajusta el tamaño según lo necesites
    nom_tipempre = models.CharField(max_length=100, blank=True, null=True)  # Ajusta el tamaño según lo necesites
    act_usua = models.CharField(max_length=8)
    act_hora = models.DateTimeField()
    act_esta = models.CharField(max_length=1)

    class Meta:
        db_table = 'tipo_empresa'

    def __str__(self):
        return self.nom_tipempre if self.nom_tipempre else f'Tipo Empresa {self.id_tipempre}'
