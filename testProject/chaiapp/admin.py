from django.contrib import admin
from .models import chaiVariety
from .models import store
from .models import chaiReview
from .models import chaiCertificate
# Register your models here.


class chaiReviewInline(admin.TabularInline):
    model=chaiReview
    extra=2

class chaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date')
    inlines=[chaiReviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display=('name','location')  
    filter_horizontal=('chai_varieties',)  

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')




admin.site.register(chaiVariety,chaiVarietyAdmin)    
admin.site.register(store,storeAdmin)    
admin.site.register(chaiCertificate,chaiCertificateAdmin)    
