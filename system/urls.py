from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

from home import views as home_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),

    url(r'login/', home_views.login, name='login'),
    url(r'index/', home_views.index, name='index'),
    url(r'home/', home_views.home, name='home'),
    url(r'about/', home_views.about, name='about'),
    url(r'main_graph/', home_views.main_graph, name='main_graph'),

    url(r'single_detection/', home_views.single_detection, name='single_detection'),
    url(r'batch_detection/', home_views.multi_detect, name='batch_detection'),

    url(r'detection0/', home_views.detection0, name='detection0'),
    url(r'detection1/', home_views.detection1, name='detection1'),
    url(r'detection_text/', home_views.detection_text, name='detection_text'),
    url(r'detection2/', home_views.detection2, name='detection2'),
    url(r'detection3/', home_views.detection3, name='detection3'),
    url(r'detection_pic/', home_views.detection_pic, name='detection_pic'),
    url(r'detection4/', home_views.detection4, name='detection4'),
    url(r'detection_comment/', home_views.detection_comment, name='detection_comment'),

    url(r'database/', home_views.unverified_database, name='unverified_database'),
    url(r'database2/', home_views.verified_database, name='verified_database'),
    url(r'data_analyse/', home_views.data_analyse, name='data_analyse'),
    url(r'multi_detect/', home_views.multi_detect, name='multi_detect'),
    url(r'multi_detail/', home_views.multi_detail, name='multi_detail'),
    url(r'verified_multi_detail/', home_views.verified_multi_detail, name='verified_multi_detail'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
