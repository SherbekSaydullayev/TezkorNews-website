from django.urls import path
from .views import homePageView,indexPageView,categoryPageView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('',indexPageView,name = 'index'),
	# path('post_detail/<int:pk>/',HomePageView.as_view(),name='post_detail'),
	path('post_detail/<str:news_id>/',homePageView,name='post_detail'),
	path('category/<int:category_id>/',categoryPageView,name='category'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)