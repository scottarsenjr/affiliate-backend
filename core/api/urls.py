from django.urls import include, path

urlpatterns = [
    path('v1/affiliate/', include('core.api.affiliatedata.urls'), name='affiliatedata'),
]
