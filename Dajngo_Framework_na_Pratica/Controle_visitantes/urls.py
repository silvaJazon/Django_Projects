from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import registrar_visitante

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("regitrar-visitantes", registrar_visitante, name="regitrar-visitantes"),

]
