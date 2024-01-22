from django.urls import path, include
from . import views

urlpatterns = [
    path('ma010/', views.ma010,name="ma010"),
    path('ma025/', views.ma025,name="ma025"),
    path('precalculus/', views.precalculus,name="precalculus"),
    path('calculusI/', views.calculusI,name="calculusI"),
    path('calculusII/', views.calculusII,name="calculusII"),
    path('calculusIII/', views.calculusIII,name="calculusIII"),
    path('differential_equations/', views.differential_equations,name="differential_equations"),
    path('class/', include('class.urls')),
]