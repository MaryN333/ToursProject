from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),  # путь к главной странице
    path('<int:tour_id>', views.single_tour, name='single_tour'),
    path('<int:tour_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete',
         views.deletereview, name='deletereview'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
