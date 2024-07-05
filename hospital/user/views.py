from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import PatientForm, MedicineForm
from .models import Patient,Medicine

# Create your views here.

class UserHome(View):
    def get(self, request):
        return render(request, 'home.html')
    
class PatientView(View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'regpatient.html', {"form": form})
    
    def post(self, request):
        form_data = PatientForm(data = request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data.get('name')
            age = form_data.cleaned_data.get('age')
            place = form_data.cleaned_data.get('place')
            phone = form_data.cleaned_data.get('phone')
            email = form_data.cleaned_data.get('email')

            Patient.objects.create(name = name, age = age, place = place, phone = phone, email = email)
            return redirect('uhome')

        return render(request, 'regpatient.html',{'form': form_data})
    
class PatientListView(View):
    def get(self, request):
        data = Patient.objects.all()
        return render(request, 'patient_list.html', {'patient': data})
    
class PatientRemoveView(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        pat = Patient.objects.get(id = pid)
        pat.delete()
        return redirect('plist')
    
class EditPatientView(View):
    def get(self, request, **kwargs):
        pid = kwargs.get('pid')
        pat = Patient.objects.get(id = pid)
        form = PatientForm(initial={'name': pat.name, 'age': pat.age, 'place': pat.place, 'phone': pat.phone, 'email': pat.email})
        return render(request, 'editpat.html', {'form': form})


    def post(self, request, **kwargs):
        pid = kwargs.get('pid')
        pat = Patient.objects.get(id = pid)

        form_data = PatientForm(data = request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data.get('name')
            age = form_data.cleaned_data.get('age')
            place = form_data.cleaned_data.get('place')
            phone = form_data.cleaned_data.get('phone')
            email = form_data.cleaned_data.get('email')

            pat.name = name
            pat.age = age
            pat.place = place
            pat.phone = phone
            pat.email = email
            pat.save()
            return redirect('plist')
        return render(request, 'editpat.html', {'form': form_data})
    

class AddMedincine(View):
    def get(self, request):
        form = MedicineForm()
        return render(request, 'addmed.html', {'form': form})
    
    def post(self, request):
        form_data = MedicineForm(data = request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('uhome')
        return render(request, 'addmed.html', {'form': form_data})
    
class MedicineListView(View):
    def get(self, request):
        medicine = Medicine.objects.all()
        return render(request, 'medicine_list.html', {'medicine': medicine})

            

            




