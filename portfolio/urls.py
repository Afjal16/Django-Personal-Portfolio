from django.urls import path
from portfolio import views
urlpatterns = [
    path('',views.Home, name='home' ),
    path('about/',views.About, name='about' ),
    path('blog/',views.Blogs, name='blog' ),
    path('contact/',views.contact, name='contact' ),
    path('portfolio/',views.portfolio, name='portfolio' ),
    path('portfolio_detail/',views.portfolio_detail, name='portfolio_detail' ),
    path('blog_detail/',views.blog_detail, name='blog_detail' ),
    
    
]