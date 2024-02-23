from django.test import TestCase
from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций выполненной работы
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="test", description="test", detailed_description="test" * 100
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей работы.

        :return:
        """

        job = Job.objects.get(description="test")

        detailed_description = "test" * 100
        self.assertEqual(job.summary(), detailed_description[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')