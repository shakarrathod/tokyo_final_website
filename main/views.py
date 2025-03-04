from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')
def makeup(request):
    return render(request, 'makeup.html')

def technical_courses(request):
    return render(request, 'technical_courses.html')

def centers(request):
    return render(request, 'centers.html')

def data_science_business_analytics(request):
    return render(request, 'dscience_banalytics.html')

def cyber_security_and_ethical_hacking(request):
    return render(request, 'cyber_security.html')
def cloud_and_devops(request):
    return render(request, 'cloud_and_devops.html')

def chess_analytics(request):
    return render(request, 'chess_analytics.html')

def event_management(request):
    return render(request, 'event_management.html')
def spoken_english(request):
    return render(request, 'spoken_english.html')
def nail_artistry(request):
    return render(request, 'nail_artistry.html')

def admissions(request):
    return render(request, 'admissions.html')

def data_science_billings(request):
    return render(request, 'data_science_billings.html')

def achievements(request):
    return render(request, 'achievements.html')

def contact(request):
    return render(request, 'contact.html')


def cyber_security_importance_need_and_advantages(request):
    return render(request, 'cyber_security_blog.html')

def blogs(request):
    return render(request, 'blogs.html')

def why_become_a_data_scientist(request):
    return render(request, 'why_datascientist_blog.html')

def importance_of_data_science_simple_guide_in_6_step(request):
    return render(request, 'importance_of_datascientist_blog.html')

def understanding_data_science_a_guide_for_beginners(request):
    return render(request, 'understand_datascientist_blog.html')

def understanding_what_is_cyber_security(request):
    return render(request, 'what_is_cybersecurity_blog.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def faq(request):
    return render(request, 'faq.html')

# def enquire_now(request):
#     return render(request, 'enquire_now.html')

def blog(request):
    return render(request, 'blog.html')
def mumbai_landing_page(request):
    return render(request, 'mumbai_landing_page.html')

def indiranagar(request):
    return render(request, 'indiranagar.html')


from django.shortcuts import render
from django.http import JsonResponse
from .forms import EnquiryForm

def enquire_now(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.source_page = request.POST.get('source_page', 'Unknown')
            enquiry.save()
            return JsonResponse({'status': 'success', 'message': 'Your enquiry has been submitted successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    return render(request, 'enquire_now.html')

def contact(request):
    return render(request, 'contact.html')


def kudlu_center_benglore(request):
    return render(request, 'kudlu.html')

def murugeshpalya_center_benglore(request):
    return render(request, 'murugeshpalya.html')

def andheri_mumbai(request):
    return render(request, 'andheri.html')

def Vijay_Nagar_Square_indore(request):
    return render(request, 'vijaynagar.html')

def Sholinganallur_chennai(request):
    return render(request, 'sholinganagar.html')

def Kodambakkam_chennai(request):
    return render(request, 'kodambakkam.html')





# import json
# import razorpay
# from django.conf import settings
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Payment
# from .forms import PaymentForm
# from io import BytesIO
# from reportlab.pdfgen import canvas

# # Initialize Razorpay Client
# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# def payment_form(request):
#     form = PaymentForm()
#     return render(request, "payment_form.html", {"form": form})

# def create_order(request):
#     if request.method == "POST":
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             # Multiply fees by 100 to convert INR to paisa
#             amount = int(form.cleaned_data["fees"]) * 100  
#             data = {
#                 "amount": amount,
#                 "currency": "INR",
#                 "payment_capture": "1"
#             }
#             order = razorpay_client.order.create(data)

#             # Save Payment instance with order details (but without payment_id)
#             payment = form.save(commit=False)
#             payment.razorpay_order_id = order["id"]
#             payment.status = "Pending"
#             payment.save()

#             return JsonResponse({
#                 "order_id": order["id"],
#                 "amount": amount,
#                 "key": settings.RAZORPAY_KEY_ID
#             })
#         else:
#             return JsonResponse({"error": "Invalid form data"}, status=400)
#     return JsonResponse({"error": "Invalid request"}, status=400)

# @csrf_exempt
# def verify_payment(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         order_id = data.get("order_id")
#         payment_id = data.get("payment_id")
#         signature = data.get("signature")
#         try:
#             # Verify the payment signature
#             razorpay_client.utility.verify_payment_signature({
#                 "razorpay_order_id": order_id,
#                 "razorpay_payment_id": payment_id,
#                 "razorpay_signature": signature
#             })

#             # Update Payment instance with payment_id and status
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#             payment.payment_id = payment_id
#             payment.status = "Completed"
#             payment.save()

#             return JsonResponse({"success": True, "payment_id": payment.payment_id})
#         except razorpay.errors.SignatureVerificationError:
#             return JsonResponse({"error": "Payment verification failed"}, status=400)

# def payment_success(request, payment_id):
#     payment = get_object_or_404(Payment, payment_id=payment_id)
#     context = {
#         "first_name": payment.first_name,
#         "last_name": payment.last_name,
#         "phone": payment.phone,
#         "email": payment.email,
#         "gender": payment.gender,
#         "aadhar": payment.aadhar,
#         "address": payment.address,
#         "state": payment.state,
#         "city": payment.city,
#         "zip": payment.zip_code,
#         "course": payment.course,
#         "fee": payment.fees,
#         "payment_id": payment.payment_id,
#         "payment_status": payment.status,
#     }
#     return render(request, "payment_success.html", context)

# def generate_pdf(request, payment_id):
#     payment = get_object_or_404(Payment, payment_id=payment_id)
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer)

#     p.drawString(100, 800, "Payment Receipt")
#     p.drawString(100, 780, f"Name: {payment.first_name} {payment.last_name}")
#     p.drawString(100, 760, f"Phone: {payment.phone}")
#     p.drawString(100, 740, f"Email: {payment.email}")
#     p.drawString(100, 720, f"Gender: {payment.gender}")
#     p.drawString(100, 700, f"Aadhar: {payment.aadhar}")
#     p.drawString(100, 680, f"Address: {payment.address}, {payment.city}, {payment.state} - {payment.zip_code}")
#     p.drawString(100, 660, f"Course: {payment.course}")
#     p.drawString(100, 640, f"Amount Paid: ₹{payment.fees}")
#     p.drawString(100, 620, f"Payment ID: {payment.payment_id}")
#     p.drawString(100, 600, f"Status: {payment.status}")

#     p.showPage()
#     p.save()

#     buffer.seek(0)
#     return HttpResponse(buffer, content_type="application/pdf")


import json
import razorpay
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment, RazorpaySettings
from .forms import PaymentForm

def get_razorpay_client():
    """
    Fetch the latest Razorpay API keys from the DB and return a new client.
    Raises an exception if the keys are not configured.
    """
    settings_obj = RazorpaySettings.objects.first()
    if not settings_obj:
        raise Exception("Razorpay API keys are not configured in the admin panel.")
    client = razorpay.Client(auth=(settings_obj.key_id, settings_obj.key_secret))
    return client, settings_obj.key_id

def payment_form(request):
    form = PaymentForm()
    return render(request, "payment_form.html", {"form": form})

def create_order(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                # Convert fee to paisa.
                amount = int(form.cleaned_data["fees"]) * 100  
            except (ValueError, TypeError):
                return JsonResponse({"error": "Invalid fee amount"}, status=400)
            
            data = {
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1"
            }
            try:
                razorpay_client, key_id = get_razorpay_client()
                order = razorpay_client.order.create(data)
            except Exception as e:
                return JsonResponse({"error": f"Razorpay order creation failed: {str(e)}"}, status=400)
            
            # Save Payment with the Razorpay order ID.
            payment = form.save(commit=False)
            payment.razorpay_order_id = order["id"]
            payment.status = "Pending"
            payment.save()
            
            return JsonResponse({
                "order_id": order["id"],
                "amount": amount,
                "key": key_id  # Pass dynamic key to the front end.
            })
        else:
            return JsonResponse({"error": form.errors.as_json()}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        order_id = data.get("order_id")
        payment_id = data.get("payment_id")
        signature = data.get("signature")
        try:
            razorpay_client, _ = get_razorpay_client()
            # Verify the Razorpay signature.
            razorpay_client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })
            payment = Payment.objects.get(razorpay_order_id=order_id)
            payment.payment_id = payment_id
            payment.status = "Completed"
            payment.save()
            return JsonResponse({"success": True, "payment_id": payment.payment_id})
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({"error": "Payment verification failed"}, status=400)
        except Payment.DoesNotExist:
            return JsonResponse({"error": "Payment record not found"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def payment_success(request, payment_id):
    payment = get_object_or_404(Payment, payment_id=payment_id)
    context = {
        "first_name": payment.first_name,
        "last_name": payment.last_name,
        "phone": payment.phone,
        "email": payment.email,
        "gender": payment.gender,
        "aadhar": payment.aadhar,
        "address": payment.address,
        "state": payment.state,
        "city": payment.city,
        "zip_code": payment.zip_code,
        "course": payment.course,
        "fees": payment.fees,
        "payment_id": payment.payment_id,
        "payment_status": payment.status,
    }
    return render(request, "payment_success.html", context)


from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit

from main.models import Payment  # Update this with your actual app name

def generate_pdf(request, payment_id):
    payment = get_object_or_404(Payment, payment_id=payment_id)
    
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    width, height = A4

    # Page Title
    p.setFont("Helvetica-Bold", 22)
    p.setFillColor(colors.darkblue)
    p.drawCentredString(width / 2, height - 70, "Payment Receipt")

    # Separator Line
    p.setStrokeColor(colors.grey)
    p.line(50, height - 85, width - 50, height - 85)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    x_offset = 80
    y_offset = height - 120
    line_height = 22

    # Function to Wrap Long Text
    def draw_wrapped_text(p, text, x, y, max_width=400):
        lines = simpleSplit(text, "Helvetica", 12, max_width)
        for line in lines:
            p.drawString(x, y, line)
            y -= line_height
        return y

    # Section Headers
    p.setFont("Helvetica-Bold", 14)
    p.setFillColor(colors.darkred)
    p.drawString(x_offset, y_offset, "Student Details:")
    y_offset -= 25

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    details = [
        ("Name:", f"{payment.first_name} {payment.last_name}"),
        ("Phone:", payment.phone),
        ("Email:", payment.email),
        ("Gender:", payment.gender),
        ("Aadhar:", payment.aadhar),
    ]

    for label, value in details:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(x_offset, y_offset, label)
        p.setFont("Helvetica", 12)
        p.drawString(x_offset + 120, y_offset, value)
        y_offset -= line_height

    # Address (wrapped text)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(x_offset, y_offset, "Address:")
    p.setFont("Helvetica", 12)
    y_offset = draw_wrapped_text(
        p, f"{payment.address}, {payment.city}, {payment.state} - {payment.zip_code}", 
        x_offset + 120, y_offset
    )

    y_offset -= 30  # Extra spacing

    # Payment Details Section (Removed Background Color)
    p.setFont("Helvetica-Bold", 14)
    p.setFillColor(colors.darkred)
    p.drawString(x_offset, y_offset, "Payment Details:")
    y_offset -= 30

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    payment_details = [
        ("Course:", payment.course),
        ("Amount Paid:", f"₹{payment.fees}"),
        ("Payment ID:", payment.payment_id),
        ("Status:", payment.status),
    ]

    for label, value in payment_details:
        p.setFont("Helvetica-Bold", 12)
        p.drawString(x_offset, y_offset, label)
        p.setFont("Helvetica", 12)
        p.drawString(x_offset + 120, y_offset, value)
        y_offset -= line_height

    # Footer Section
    p.setStrokeColor(colors.lightgrey)
    p.line(50, y_offset - 20, width - 50, y_offset - 20)
    p.setFont("Helvetica-Oblique", 10)
    p.setFillColor(colors.grey)
    p.drawCentredString(width / 2, y_offset - 40, "Thank you for enrolling with us!")

    # Finalize and save PDF
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type="application/pdf")
