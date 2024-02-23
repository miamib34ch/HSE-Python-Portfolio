from django.db import models
from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе
    """

    resume_url = models.URLField(verbose_name="Ссылка на резюме")
    github_url = models.URLField(verbose_name="Ссылка GitHub")
    email = models.EmailField(verbose_name="Email автора")

    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "автор" (id={self.pk})'