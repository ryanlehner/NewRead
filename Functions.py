from django.db import models


class Reporter(models.Model):
    InputText = models.TextField(max_length=200)

    def __str__(self):
        return self.InputText


class Article(models.Model):
    btnSpdUp = models.Button()
    btnSpdDwn = models.Button()
    fldSpeed = models.TextField(max_length=50)
    lblWord = models.Label()

    def __str__(self):
        return self.fldSpeed
