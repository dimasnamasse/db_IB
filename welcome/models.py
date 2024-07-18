from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class User(AbstractBaseUser):

    middle_name = models.CharField(max_length=50, blank=True, null=True,verbose_name="Отчество")
    phone = models.CharField(max_length=50,verbose_name="Телефон")
    username=models.CharField(max_length=50,verbose_name="Имя пользователя")
    name=models.CharField(max_length=50,verbose_name="Имя")
    surname=models.CharField(max_length=50,verbose_name="Фамилия")
    email=models.CharField(max_length=50,verbose_name="Почта")
    date_joined = models.DateTimeField(verbose_name="Дата захода", default=timezone.now)
    is_superuser=models.BooleanField(verbose_name="Админ?")

    class Meta():
        verbose_name_plural="Пользователь"


class UserGroup(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="group",
        verbose_name="Группа"

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Пользователь"
    )
    class Meta():
        verbose_name_plural="Группа пользователей"


class Group(models.Model):

    name = models.CharField(max_length=50,verbose_name="Название")
    is_active=models.BooleanField(verbose_name="Актив/удален")
    class Meta():
        verbose_name_plural="Группа"
class ObjectInformatization(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    contact = models.CharField(max_length=255, blank=True, null=True,verbose_name="Контактное лицо")
    group=models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Группа"
    )

    organization= models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name="Организация"
    )
    class Meta():
        verbose_name_plural="Объект информатизации"
class Organization(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    address = models.CharField(max_length=255, blank=True, null=True,verbose_name="Адрес")
    group=models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Группа"
    )
    class Meta():
        verbose_name_plural="Организация"

class InformationSystem(models.Model):
    GIS=0
    ISPDn=1
    GIS_ISPDn=2
    types=[
        (GIS,"ГИС",ISPDn,"ИСПДН",GIS_ISPDn," ГИС+ИСПДн")
    ]
    type = models.CharField(max_length=10, choices=types,verbose_name="Тип")
    name = models.CharField(max_length=50,verbose_name="Название")
    address = models.CharField(max_length=255, blank=True, null=True,verbose_name="Адрес")
    clss = models.CharField(max_length=50, blank=True, null=True,verbose="Класс защищенности")
    clss_info = models.CharField(max_length=255, blank=True, null=True,verbose_name='Информация о классе')
    level = models.CharField(max_length=50, blank=True, null=True,verbose_name="Уровень защищенности")
    level_info = models.CharField(max_length=50, blank=True, null=True,verbose_name="Информация о уровне")
    contact = models.CharField(max_length=255, blank=True, null=True,verbose_name="Контактное лицо")


    object=models.ForeignKey(
        ObjectInformatization,
        on_delete=models.CASCADE,
        verbose_name="Обьект информатизации"
    )
    class Meta():
        verbose_name_plural="Информационная система"

class Place(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    is_active = models.BooleanField(verbose_name="Актив/Архив")
    adress = models.CharField(max_length=255, blank=True, null=True,verbose_name="Адрес")
    infosystem=models.ForeignKey(
        InformationSystem,
        on_delete=models.CASCADE,
        verbose_name="Информационная система"
    )
    class Meta():
        verbose_name_plural="Место"

class CheckList(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    is_check = models.BooleanField(verbose_name="Проверен/Нет")
    project=  models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект"
    )
    class Meta():
        verbose_name_plural="Чек-лист"

class Project(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    deadline = models.DateTimeField(auto_now_add=True,verbose_name="Срок завершения")
    is_check = models.BooleanField(verbose_name="Проверен/нет")
    is_finished = models.BooleanField(verbose_name="Действующий/Завершен")
    infosystem =models.ForeignKey(
        InformationSystem,
        on_delete=models.CASCADE,
        verbose_name="Информационная система"
    )
    group_rp=models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="rp",
        verbose_name="Руководители ИС"

    )
    group_work = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="work",
        verbose_name="Исполнители ИС"
    )
    class Meta():
        verbose_name_plural="Проект"