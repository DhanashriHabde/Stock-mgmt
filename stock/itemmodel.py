from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    total=models.DecimalField(max_digits=20, decimal_places=2)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
