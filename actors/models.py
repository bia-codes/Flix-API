from django.db import models

# cadastro da tupla de choices(lista de escolha de nacionalidade), bpc: caixa alta, lado esquerdo oq mostra no BD, lado direito oq mostra pro usuário (p/display)
NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
)


class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(max_length=100, null=True, blank=True)
    nationality = models.CharField(
        max_length=200,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
