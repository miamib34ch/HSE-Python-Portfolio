from django.apps import AppConfig


class AuthorConfig(AppConfig):
    """
    Конфигурация приложения.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "author"
    verbose_name = "Автор"
