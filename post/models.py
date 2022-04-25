from django.db import models


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

