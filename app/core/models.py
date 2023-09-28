from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    # it is necessary this method for the name of the person (nome) to appear in admin panel
    def __str__(self):
        return self.nome
