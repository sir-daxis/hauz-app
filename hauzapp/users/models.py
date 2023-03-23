from django.db import models
from django.contrib.auth.models import User

class UserCategories(models.Model):
    title_of_user = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title_of_user}'


class UserCat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_cat = models.ForeignKey(UserCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.user_cat.title_of_user}'
