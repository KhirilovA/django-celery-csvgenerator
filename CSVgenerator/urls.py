from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/./scheme_list/', permanent=False)),
    path('', include('generator.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
