from django.db import models

class Yutuq(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField(auto_now_add=True)
    matn = models.TextField()
    rasm = models.FileField()

    def __str__(self):
        return f"{self.sarlavha} - {self.sana}"
