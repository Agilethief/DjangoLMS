from django.db import models


# Create your models here.
class User(models.Model):
    user_name_preferred = models.CharField(max_length=100)
    user_name_first = models.CharField(max_length=100)
    user_name_last = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(
        max_length=100
    )  # This should be hashed. TODO: Implement hashing.
    user_created_date = models.DateTimeField(auto_now_add=True)
    user_last_logged_in = models.DateTimeField(auto_now_add=True)
    user_is_active = models.BooleanField(
        default=True
    )  # This is used to deactivate a user.
    user_permissions = models.CharField(max_length=100)  # Student, teacher, admin
    user_SISID = models.CharField(
        max_length=100, default="0"
    )  # This is the student information system ID.

    def __str__(self):
        return self.user_name

    def user_full_name(self):
        return f"{self.user_name_first} {self.user_name_last}"

    def user_name(self):
        return f"{self.user_name_preferred}"
