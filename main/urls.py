from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('makeup/', views.makeup, name='makeup'),
    path('nail_artistry/', views.nail_artistry, name='nail_artistry'),


    path('technical_courses/', views.technical_courses, name='technical_courses'),
    path('centers/', views.centers, name='centers'),
    path('data_science_business_analytics/', views.data_science_business_analytics, name='data_science_business_analytics'),
    path('cyber_security_and_ethical_hacking/', views.cyber_security_and_ethical_hacking, name='cyber_security_and_ethical_hacking'),
    path('cloud_and_devops/', views.cloud_and_devops, name='cloud_and_devops'),

    path('chess_analytics/', views.chess_analytics, name='chess_analytics'),
    path('event_management/', views.event_management, name='event_management'),
    path('spoken_english/', views.spoken_english, name='spoken_english'),

    path('admissions/', views.admissions, name='admissions'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
    path('terms_and_condtions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('blogs/', views.blogs, name='blogs'),
    path('faq/', views.faq, name='faq'),
    path('enquire_now/', views.enquire_now, name='enquire_now'),
    path('blog/', views.blog, name='blog'),
    path('mumbai_landing-page/', views.mumbai_landing_page, name='mumbai_landing_page'),

    path('indiranagar/', views.indiranagar, name='indiranagar'),


]
