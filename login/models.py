from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    # id = models.CharField(max_length=50, unique=True)
    pw = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class asdasd(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'aesd'
