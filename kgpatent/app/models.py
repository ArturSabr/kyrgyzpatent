from django.db import models


class Mark(models.Model):
    registration_id = models.IntegerField(verbose_name="Номер регистрации")
    date_of_submission = models.DateField(verbose_name="Дата подвчи", auto_now_add=True)
    img = models.ImageField(upload_to='img',verbose_name="Картинка")
    num = models.IntegerField(verbose_name="Номер Марки")

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class Code(models.Model):
    code = models.IntegerField(verbose_name="Код")
    description = models.TextField(verbose_name="Описание", max_length=1500)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name="Номер Марки",related_name = "code")

    class Meta:
        verbose_name = "Код"
        verbose_name_plural = "Коды"


class Applicant(models.Model):
    title = models.CharField(verbose_name="ФИО", max_length=255)
    adress = models.CharField(max_length=255, verbose_name="Адрес")
    country = models.CharField(max_length=255, verbose_name="Страна")
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name="Номер Марки",related_name = "applicant")

    class Meta:
        verbose_name = "Заявитель"
        verbose_name_plural = "Заявители"


class Patent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    adress = models.CharField(max_length=255, verbose_name="Адрес")
    tel = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Почта")
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name="Номер Марки",related_name = "patent")

    class Meta:
        verbose_name = "Патент"
        verbose_name_plural = "Патенты"
