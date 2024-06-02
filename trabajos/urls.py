from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('trabajo/<int:trabajo_id>/', views.detalle_trabajo, name='detalle_trabajo'),
    path('crear/', views.crear_trabajo, name='crear_trabajo'),
    path('editar/<int:pk>/', views.crear_trabajo, name='editar_trabajo'),
    path('obtener_actividades', views.obtener_actividades, name='obtener_actividades'),
]