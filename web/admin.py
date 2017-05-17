from django.contrib import admin
from .models import tramite,detalle,noticia
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from mensajes.models import mensaje
from django.forms import CheckboxSelectMultiple
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class DetalleInline(admin.TabularInline):
    model = detalle
class TramiteInline(admin.TabularInline):
    model= tramite.users.through
    inlines = [DetalleInline,]
    def editar(self, instance):
        url = '/admin/web/tramite/'+ str(instance.id) +'/change/'
        return format_html(u'<a href="{}">Edit</a>', url)
    readonly_fields = ('editar',)

class TramiteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'referencia')
    inlines = [DetalleInline,]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class userAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name','email','password')
    list_display = ('username', 'first_name', 'last_name')
    #inlines=[TramiteInline,]
    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()
class mensajeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'asunto', 'email')
    readonly_fields=('titulo', 'asunto', 'email','texto')


class limite(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

class noticiasForm(forms.ModelForm):

    noticia = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = noticia
        fields = '__all__'


class noticiasAdmin(admin.ModelAdmin):
    form = noticiasForm

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,userAdmin)
admin.site.register(mensaje,mensajeAdmin)
admin.site.register(tramite, TramiteAdmin)
admin.site.register(detalle)
admin.site.register(noticia,noticiasAdmin)
