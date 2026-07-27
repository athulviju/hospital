from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_descriptrion = models.TextField()


    def __str__(self):
        return self.department_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_specialization = models.CharField(max_length=100)

    department = models.ForeignKey(
        'hospitalapp.Department',
        on_delete=models.CASCADE
    )
    doctor_image = models.ImageField(upload_to='doctors/')
    doctor_description = models.TextField()

    def __str__(self):
        return self.doctor_name

class Booking(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
