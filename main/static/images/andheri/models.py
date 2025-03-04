from django.db import models

class Payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"
