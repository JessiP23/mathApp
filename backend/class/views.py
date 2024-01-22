from django.shortcuts import render

def whole_number(request):
    return render(request, 'class_ma010/whole_number.html')

def signed_number(request):
    return render(request, 'class_ma010/signed_number.html')

def equations(request):
    return render(request, 'class_ma010/equations.html')

def geometry(request):
    return render(request, 'class_ma010/geometry.html')   

def linear_equation(request):
    return render(request, 'class_ma025/linear_equation.html')

def inequality(request):
    return render(request, 'class_ma025/inequality.html')

def equations_two_variables(request):
    return render(request, 'class_ma025/equations_two_variables.html')

def equations_system(request):
    return render(request, 'class_ma025/equations_system.html')

def polynomial(request):
    return render(request, 'class_ma025/polynomial.html')

def factoring(request):
    return render(request, 'class_ma025/factoring.html')

def rational_expression(request):
    return render(request, 'class_ma025/rational_expression.html')

def radical(request):
    return render(request, 'class_ma025/radical.html')

def quadratic(request):
    return render(request, 'class_ma025/quadratic.html')
