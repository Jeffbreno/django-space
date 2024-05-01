from django.db import models


class Usuarios(models.Model):
    nome = ""

    def __str__(self):
        return self.nome

