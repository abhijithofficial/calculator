from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails,CalculatorDetails

def get_user(request):
	if request.method == 'POST':
		if request.POST.get('name') != "" and request.POST.get('email') != "" :
			name = request.POST.get('name')
			email = request.POST.get('email')
			user = UserDetails.objects.create(name=name,email=email)
			request.session['user'] = user.id
			return redirect('get_calculator')
	return render(request, 'fahrenheit_calculator/index.html')

def get_calculator(request):
	if request.session['user'] is not None:
		if request.method == 'POST':
			celsius  = request.POST.get('celsius')
			fahrenheit = request.POST.get('fahrenheit')
			if celsius != "":
				fahrenheit = (celsius * 9/5) + 32
			else:
				celsius = (fahrenheit - 32) * 5/9
			calculator_object = CalculatorDetails.objects.create(
				celsius=celsius,
				fahrenheit=fahrenheit,
				user_id=request.session['user']
				)
		return render(request,'fahrenheit_calculator/calculator.html',{})
	else:
		return redirect('get_user')
	