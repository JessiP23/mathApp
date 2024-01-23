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
    path('function_graph/', views.function_graph, name="function_graph"),
    path('polynomial_function/', views.polynomial_function, name="polynomial_function"),
    path('exponential_function/', views.exponential_function, name="exponential_function"),
    path('trig_function/', views.trig_function, name="trig_function"),
    path('sine_and_cosine/', views.sine_and_cosine, name="sine_and_cosine"),
    path('conic_section/', views.conic_section, name="conic_section"),
    path('function_and_graph/', views.function_and_graph, name="function_and_graph"),
    path('limit/', views.limit, name="limit"),
    path('derivative/', views.derivative, name="derivative"),
    path('derivative_application/', views.derivative_application, name="derivative_application"),
    path('integration/', views.integration, name="integration"),
    path('forum/', include('forum.urls')),
] 

