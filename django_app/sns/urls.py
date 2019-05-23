from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='top'),
        path('groups',views.groups,name='groups'),
        path('add',views.add,name='add'),
        path('creategroup',views.creategroup,name='creategroup'),
        path('post',views.post,name='post'),
        path('share/<int:share_id>',views.share,name='share'),
        path('good/<int:good_id>',views.good,name='good'),
        path('friends',views.friends,name='friends'),
        ]



from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)