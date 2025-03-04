from django.db import models
from django.core.validators import RegexValidator

class Enquiry(models.Model):
    CATEGORY_CHOICES = [
        ('it', 'IT Courses'),
        ('professional', 'Professional Courses'),
    ]

    COURSE_CHOICES = [
        ('data_science', 'Data Science & Business Analytics'),
        ('cyber_security', 'Cyber Security & Ethical Hacking'),
        ('cloud_devops', 'Cloud & DevOps'),
        ('chess_analytics', 'Chess Analytics'),
        ('event_management', 'Event Management'),
        ('nail_artistry', 'Nail Artistry'),
        ('makeup_artistry', 'Makeup Artistry'),
        ('spoken_english', 'Spoken English'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(regex=r'^[6-9]\d{9}$', message="Enter a valid 10-digit Indian phone number.")]
    )
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    message = models.TextField()
    source_page = models.CharField(max_length=20, default="Unknown")  # Add default value

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course} ({self.source_page})"
    


    
# from django.db import models

# class Payment(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     gender = models.CharField(max_length=10)
#     aadhar = models.CharField(max_length=12)
#     address = models.TextField()
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zip_code = models.CharField(max_length=10)
#     course = models.CharField(max_length=100)
#     fees = models.IntegerField()
#     razorpay_order_id = models.CharField(max_length=100, unique=True)
#     payment_id = models.CharField(max_length=100, blank=True, null=True)
#     status = models.CharField(max_length=20, default="Pending")

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.course} ({self.status})"



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
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course} ({self.status})"





class RazorpaySettings(models.Model):
    key_id = models.CharField(max_length=100)
    key_secret = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Razorpay Settings"

    def save(self, *args, **kwargs):
        # Enforce that only one RazorpaySettings instance exists.
        if not self.pk and RazorpaySettings.objects.exists():
            raise Exception("Only one RazorpaySettings instance is allowed.")
        super().save(*args, **kwargs)