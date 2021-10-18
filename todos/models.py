from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    title = models.CharField(max_length=50,blank=False)
    desc = models.CharField(max_length=50,blank=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"

        
    def __str__(self):
        return self.title
