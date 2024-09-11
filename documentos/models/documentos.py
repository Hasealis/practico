from django.db import models

class documentos(models.Model):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'documentos'