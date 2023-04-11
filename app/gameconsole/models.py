from django.db import models
from consolemaker.models import ConsoleMaker


class GameConsole(models.Model):
    name = models.CharField(max_length=250)
    maker_of_console = models.ForeignKey(
        ConsoleMaker,
        on_delete=models.CASCADE,
        related_name="consoles_from_brand",
        null=True,
        blank=True,
        default=None,
    )
    name_code = models.CharField(max_length=15, default="CODE")

    def __str__(self):
        return self.name
