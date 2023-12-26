from django.db import models


class Label(models.Model):
    lblWord = models.Label(max_length=200)

    def __str__(self):
        return self.lblWord


class txtSpeed(models.Model):
    btnSpdUp = models.Button()
    btnSpdDwn = models.Button()
    fldSpeed = models.TextField()

    def __str__(self):
        return self.fldSpeed

class InputBox(models.Model):
    txtMain = models.TextField()
    btnImport = models.Button()

    def __str__(self):
        return self.txtMain