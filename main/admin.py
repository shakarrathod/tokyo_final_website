from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'category', 'course', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('category', 'course', 'created_at')





# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name", "phone", "email", "course", "fees", "status", "payment_id", "created_at") 
#     search_fields = ("first_name", "last_name", "phone", "email", "payment_id")
#     list_filter = ("status", "course", "created_at")



from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'course', 'fees', 'status', 'payment_id')
    search_fields = ('first_name', 'last_name', 'email', 'course')



from .models import RazorpaySettings



@admin.register(RazorpaySettings)
class RazorpaySettingsAdmin(admin.ModelAdmin):
    list_display = ("key_id", "updated_at")