from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)


class Baza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    test_count = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)

    # def update_test_count(self):
    #     self.test_count = self.test_set.count()
    #     self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.category.count = self.category.baza_set.count()
        self.category.save()


class Test(models.Model):
    baza = models.ForeignKey(Baza, on_delete=models.CASCADE)
    savol = models.TextField()
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200, null=True, blank=True)
    togri = models.CharField(max_length=1, help_text='Masalan: a')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.baza.update_test_count()

