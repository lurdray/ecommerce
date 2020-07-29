from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap, ProductSitemap
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
	"static": StaticViewSitemap,
	"product": ProductSitemap,
}

urlpatterns = [
    path('', include("main.urls")),
    path('', include("admin_app.urls")),
     path('', include("product.urls")),
     path('', include("customer.urls")),
    path('', include("order.urls")),
    path('', include("cart.urls")),

	path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path('admin/', admin.site.urls),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
