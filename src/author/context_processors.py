from django.http import HttpRequest
from author.models import Author


def author(request: HttpRequest) -> dict:
    """
    Контекстный процессор для информации об авторе
    """
    return {"author": Author.objects.last()}