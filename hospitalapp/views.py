from django.shortcuts import render, redirect
from .models import Department, Doctor, Booking


def index(request):
    return render(request, 'Index.html')


def about(request):
    return render(request, 'About.html')


def department(request):
    dept = Department.objects.all()
    return render(request, 'Department.html', {'dept': dept})


def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'Doctor.html', {'doctor': doctors})


def booking(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        patient_phone = request.POST.get('patient_phone')
        patient_email = request.POST.get('patient_email')
        booking_date = request.POST.get('booking_date')
        doctor_id = request.POST.get('doctor')

        selected_doctor = Doctor.objects.get(id=doctor_id)

        Booking.objects.create(
            patient_name=patient_name,
            patient_phone=patient_phone,
            patient_email=patient_email,
            doctor=selected_doctor,
            booking_date=booking_date
        )

        return redirect('booking')

    return render(request, 'Booking.html', {'doctor': doctors})


def contact(request):
    return render(request, 'Contact.html')