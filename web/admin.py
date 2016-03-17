from django.contrib import admin
from .models import nosotros_primero, nosotros_segundo,nosotros_tercero,tramite,detalle
from django.contrib.auth.models import User
class limite(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(nosotros_primero, limite)
admin.site.register(nosotros_segundo, limite)
admin.site.register(nosotros_tercero, limite)
admin.site.register(tramite)
admin.site.register(detalle)
