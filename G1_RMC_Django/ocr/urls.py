from django.urls import path
from . import views

urlpatterns =[

    path('',views.upload, name='ocr'),
    path('success/<int:ocr_result_id>/', views.upload_success, name='ocr_upload_success'),
    path('save_ocr_result/', views.save_ocr_result, name='save_ocr_result'),

]