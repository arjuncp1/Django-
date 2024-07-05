from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.views import View

# Create your views here.

def landingView(request):
    return render(request, 'landing.html')

def loginView(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('password')
        return redirect('uhome')






# class RegView(View):
#     def get(self, request):
#         return render(request, 'reg.html')

#     def post(self, request):
#         if request.method == "POST":
#             name = request.POST.get('uname')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             return HttpResponse(f'name: {name}, password: {password}, email: {email}')


class RegView(View):
    def get(self, request):
        return render(request, 'reg.html')

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('uname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            response_data = {
                'name': name,
                'email': email,
                'password': password
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=400)

    
