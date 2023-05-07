from django.urls import path
from .views import HomePage,AboutUs,Services,contact_view,blogs,portfolio, article_detail
urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutUs.as_view(),name='about'),
    path('services/',Services.as_view(),name='services'),
    path('contact/',contact_view,name='contact'),
    path('portfolio/',portfolio,name='portfolio'),
    path('blog/',blogs,name='blog'),
    path('blog/<int:id>', article_detail, name='article_detail'),
]
