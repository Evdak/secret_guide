from django.db import models

# Create your models here.


class Kstati(models.Model):
    quest_name = models.CharField("Название квеста", max_length=100)
    question_number = models.IntegerField("Номер вопроса")
    text = models.TextField("Текст выплывающего окна")
    button = models.BooleanField("Добавить кнопку")
    button_name = models.CharField(
        "Название кнопки", max_length=100, null=True, blank=True)
    button_on_click = models.TextField(
        "Действие на кнопку", null=True, blank=True)

    class Meta:
        verbose_name = "Кстати"
        verbose_name_plural = "Кстати"

    def __str__(self) -> str:
        return f"{self.quest_name} {self.question_number}"
