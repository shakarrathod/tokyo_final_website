from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404  # Combined import
from django.conf import settings

import razorpay  # Third-party imports below Django imports

from .models import Payment  # Local imports at the bottom
from reportlab.pdfgen import canvas  # PDF generation library

# ------------------ Payment Gateway Views ------------------

def index(request):
    return render(request, 'index.html')

def murugeshpalya(request):
    return render(request, 'murugeshpalya.html')

def payment_form(request):
    courses = {
        "Data Science and Business Analytics": 50000,
        "Cyber Security and Ethical Hacking": 60000,
        "Cloud Computing and DevOps": 70000,
        "Chess Analytics": 40000,
        "Event Management": 55000,
        "Spoken English": 30000,
        "Nail Artistry": 25000,
        "Makeup Artistry": 45000
    }

    if request.method == "POST":
        data = request.POST
        selected_course = data.get("course")
        amount = courses.get(selected_course, 0)  # Prevents KeyError

        if amount == 0:
            return HttpResponse("Invalid course selected", status=400)

        payment = Payment.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data["phone"],
            email=data["email"],
            gender=data["gender"],
            aadhar=data["aadhar"],
            address=data["address"],
            state=data["state"],
            city=data["city"],
            zip_code=data["zip_code"],
            course=selected_course,
            fees=amount,
            status="Pending"
        )

        # Razorpay Payment Integration
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order = client.order.create({
            "amount": amount * 100,  # Convert to paisa
            "currency": "INR",
            "payment_capture": "1"
        })

        payment.payment_id = order["id"]
        payment.save()

        return render(request, "payment_form.html", {"order": order, "payment": payment, "courses": courses})

    return render(request, "payment_form.html", {"courses": courses})

def payment_success(request):
    payment_id = request.GET.get("payment_id")

    if not payment_id:
        return HttpResponse("Payment ID is missing", status=400)

    try:
        payment = Payment.objects.get(payment_id=payment_id)
    except Payment.DoesNotExist:
        raise Http404("Payment not found in the database")

    payment.status = "Completed"
    payment.save()
    
    return render(request, "payment_success.html", {"payment": payment})

def download_pdf(request, payment_id):
    try:
        payment = Payment.objects.get(payment_id=payment_id)
    except Payment.DoesNotExist:
        raise Http404("Payment not found in the database")

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="receipt_{payment_id}.pdf"'

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Payment Receipt")
    pdf.drawString(100, 780, f"Name: {payment.first_name} {payment.last_name}")
    pdf.drawString(100, 760, f"Course: {payment.course}")
    pdf.drawString(100, 740, f"Amount Paid: ₹{payment.fees}")
    pdf.drawString(100, 720, f"Payment ID: {payment.payment_id}")
    pdf.showPage()
    pdf.save()

    return response
