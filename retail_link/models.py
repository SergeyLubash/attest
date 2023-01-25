from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Контакты:
           Email;
           Страна;
           Город;
           Улица;
           Номер дома;
    """
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField()
    country = models.CharField(verbose_name='Страна', max_length=30, blank=True)
    city = models.CharField(verbose_name='Город', max_length=30, blank=True)
    street = models.CharField(verbose_name='Улица', max_length=30, blank=True)
    house = models.CharField(verbose_name='Номер дома', max_length=5, blank=True)

    def __str__(self):
        return self.country


class Product(models.Model):
    """
    Продукты:
         Название;
         Модель;
         Дата выхода продукта на рынок;
    """
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    product_title = models.CharField(verbose_name='Название продукта', max_length=255, blank=True)
    product_model = models.CharField(verbose_name='Модель продукта', max_length=100, blank=True)
    date_out = models.DateField(verbose_name='Дата выхода продукта на рынок')
    quantity = models.IntegerField(verbose_name='Количество', blank=True)

    def __str__(self):
        return self.product_title


class Subject_net(models.Model):
    """
    Участник торговой сети:
        Название;
        Контакты;
        Продукты;
        Время создания (заполняется автоматически при создании).
        """
    class Meta:
        verbose_name = 'Субъект сети'
        verbose_name_plural = 'Субъекты сети'

    title = models.CharField(verbose_name='Название субъекта', max_length=255, unique=True)
    contacts = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.CASCADE)
    created_date = models.DateField(verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        if not self.id:  # Когда объект только создается, у него еще нет id
            self.created = timezone.now()  # проставляем дату создания
        self.updated = timezone.now()  # проставляем дату обновления
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Provider(models.Model):
    """
    Поставщик:

    """

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    subjects = models.ForeignKey(Subject_net, related_name='subjects', verbose_name='Субъект сети', on_delete=models.CASCADE)
    providers = models.ForeignKey(Subject_net, related_name='providers', verbose_name='Поставщик', on_delete=models.CASCADE)
    arrears = models.FloatField(verbose_name='Задолженность', blank=True)

    def __str__(self):
        return self.providers
