from django.db import models

class Producto(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=255
    )
    referencia = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'core_producto'
    
