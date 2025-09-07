from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'is_featured', 'score', 'created_at']
    list_editable = ['is_published', 'is_featured', 'score']
    search_fields = ['title', 'content']
    list_filter = ['is_published', 'is_featured']
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    def save_model(self,request,obj,form,change):
        if not obj.pk:
            obj.author=request.user
        obj.save()
    def get_readonly_fields(self,request,obj=None):
        if not request.user.is_superuser:
            return ('author','score','is_published', 'is_featured',)   # Only post by user allowed at admin section
        return super().get_readonly_fields(request,obj)
    
    def get_fields(self,request,obj=None):
        fields=super().get_fields(request,obj)
        if not request.user.is_superuser:
            fields=[f for f in fields if f !='score']
        return fields
    def get_list_display(self,request):
        if not request.user.is_superuser:
            return ('title', 'author', 'created_at',) # score not allowed for non-superusers at admin section
        return self.list_display
              
#class CustomAdminSite(admin.AdminSite):
#    site_header = "EBONYI STATE LGA ADMIN PANEL"
#  site_title = "Ebonyi state LGA update"
# index_title = "Welcome to admin"
#  class Media:
#      css = {
#            'all': ('css/admin_overrides.css',)
#        }
# Replace default admin site
#admin.site = CustomAdminSite()