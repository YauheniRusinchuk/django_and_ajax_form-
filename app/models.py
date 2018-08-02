from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.text    
