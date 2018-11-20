from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'plantcategory'

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('', views.homePage, name='home'),
    path('plantlist/', views.plantList, name='plantlist'),
    path('plantlist/<int:plantid>', views.plantDetails, name='plantdetails'),
    path('addgrain/', views.addGrain, name='addgrain'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)