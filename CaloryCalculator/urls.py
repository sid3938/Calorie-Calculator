from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path('calorie_calculator/', views.calorie_calculator, name='calorie_calculator'),
    path('Counter/', include('Counter.urls')),
    path('Recipe/', include('Recipe.urls')),
    path('BMI_Calculator/', include('BMI_Calculator.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)