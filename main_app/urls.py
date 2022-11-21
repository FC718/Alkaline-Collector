from django.urls import path
from . import views

# THIS IS WHERE WE DEFINE OUR ROUTES
urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    
    path('alkaline/', views.alkaline_index, name='index'),
    
    path('alkalines/<int:alkaline_id>/', views.alkalines_detail, name='detail'),
    
    path('alkalines/create/', views.AlkalineCreate.as_view(), name='alkalines_create'),
    
    path('alkalines/<int:pk>/update/', views.AlkalineUpdate.as_view(), name='alkalines_update'),
    
    path('alkalines/<int:pk>/delete/', views.AlkalineDelete.as_view(), name='alkalines_delete'),
    
    path('alkalines/<int:alkaline_id>/add_juicing/', views.add_juicing, name='add_juicing'),

    path('fruits/', views.FruitList.as_view(), name='fruits_index'),
    
    path('fruits/<int:pk>/', views.FruitDetail.as_view(), name='fruits_detail'),
    
    path('fruits/create/', views.FruitCreate.as_view(), name='fruits_create'),
    
    path('fruits/<int:pk>/update/', views.FruitUpdate.as_view(), name='fruits_update'),
    
    path('fruits/<int:pk>/delete/', views.FruitDelete.as_view(), name='fruits_delete'),
]
