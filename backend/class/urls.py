from django.urls import path, include
from . import views

app_name = 'class'

urlpatterns = [
    path('whole_number/', views.whole_number,name="whole_number"),
    path('signed_number/', views.signed_number,name="signed_number"),
    path('equations/', views.equations,name="equations"),
    path('geometry/', views.geometry,name="geometry"),
    path('linear_equation/', views.linear_equation,name="linear_equation"),
    path('inequality/', views.inequality,name="inequality"),
    path('equations_two_variables/', views.equations_two_variables,name="equations_two_variables"),
    path('equations_system/', views.equations_system,name="equations_system"),
    path('polynomial/', views.polynomial,name="polynomial"),
    path('factoring/', views.factoring,name="factoring"),
    path('rational_expression/', views.rational_expression,name="rational_expression"),
    path('radical/', views.radical,name="radical"),
    path('quadratic/', views.quadratic,name="quadratic"),
] 
