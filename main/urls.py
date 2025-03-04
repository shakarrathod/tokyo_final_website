from django.urls import path
from . import views
from .views import enquire_now

from .views import payment_form, payment_success



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
    path('data_science_billings/', views.data_science_billings, name='data_science_billings'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
    path('terms_and_condtions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('blogs/', views.blogs, name='blogs'),
  


    path(
        'cyber_security_importance_need_and_advantages/',  # URL pattern
        views.cyber_security_importance_need_and_advantages,  # View function
        name='cyber_security_importance_need_and_advantages'  # URL name for reverse lookup
    ),
    path(
        'why-become-a-data-scientist/',  # URL pattern
        views.why_become_a_data_scientist,  # View function
        name='why-become-a-data-scientist'  # URL name for reverse lookup
    ),
    path(
        'importance-of-data-science-simple-guide-in-6-step/',  # URL pattern
        views.importance_of_data_science_simple_guide_in_6_step,  # View function
        name='importance-of-data-science-simple-guide-in-6-step'  # URL name for reverse lookup
    ),
    path(
        'understanding-data-science-a-guide-for-beginners/',  # URL pattern
        views.understanding_data_science_a_guide_for_beginners,  # View function
        name='understanding-data-science-a-guide-for-beginners'  # URL name for reverse lookup
    ),

      path(
        'understanding-what-is-cyber-security/',  # URL pattern
        views.understanding_what_is_cyber_security,  # View function
        name='understanding-what-is-cyber-security'  # URL name for reverse lookup
    ),

    path('faq/', views.faq, name='faq'),
    # path('enquire_now/', views.enquire_now, name='enquire_now'),
    path('blog/', views.blog, name='blog'),
    path('mumbai_landing-page/', views.mumbai_landing_page, name='mumbai_landing_page'),

    path('indiranagar/', views.indiranagar, name='indiranagar'),

    path('enquire-now/', enquire_now, name='enquire_now'),  # ✅ Correct name



    path('kudlu_center_benglore/', views.kudlu_center_benglore, name='kudlu_center_benglore'),

    path('murugeshpalya_center_benglore/', views.murugeshpalya_center_benglore, name='murugeshpalya_center_benglore'),

    path('andheri_mumbai/', views.andheri_mumbai, name='andheri_mumbai'),

    path('Sholinganallur_chennai/', views.Sholinganallur_chennai, name='Sholinganallur_chennai'),

    path('Kodambakkam_chennai/', views.Kodambakkam_chennai, name='Kodambakkam_chennai'),

    path('Vijay_Nagar_Square_indore/', views.Vijay_Nagar_Square_indore, name='Vijay_Nagar_Square_indore'),






    # path("payment_form/", views.payment_form, name="payment_form"),
    # path("payment_success/", views.payment_success, name="payment_success"),

    # path("download_pdf/<str:payment_id>/", views.download_pdf, name="download_pdf"),
       
  
    # path('payment_form', views.payment_form, name='payment_form'),
    # path('create_order/', views.create_order, name='create_order'),
    # path('verify_payment/', views.verify_payment, name='verify_payment'),
    # path('payment_success/<str:payment_id>/', views.payment_success, name='payment_success'),
    # path('generate_pdf/<str:payment_id>/', views.generate_pdf, name='generate_pdf'),

       path('payment_form/', views.payment_form, name='payment_form'),
    path('create_order/', views.create_order, name='create_order'),
    path('verify_payment/', views.verify_payment, name='verify_payment'),
    path('payment_success/<str:payment_id>/', views.payment_success, name='payment_success'),
    path('generate_pdf/<str:payment_id>/', views.generate_pdf, name='generate_pdf'),


]






   
