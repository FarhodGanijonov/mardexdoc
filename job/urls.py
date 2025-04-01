from django.urls import path
from . import views
from .send_order import SendOrderToSelectedWorkersView

urlpatterns = [
    path('category_jobs/', views.category_job_list, name='category_job_list'),  # Category job ro'yxati
    path('category_jobs/<int:pk>/', views.JobListByCategoryView.as_view(), name='category_job_recent'),  # Yangi category job'lar
    path('jobs/', views.job_list, name='job_list'),  # Job ro'yxati
    path('jobs/<int:pk>/similar/', views.job_similar, name='job_similar'),  # Job'ga o'xshash ishlar

    path('city/', views.city_list, name='city_list'),  # Shahar ro'yxati
    path('city/count/', views.city_count, name='city_count'),  # Shaharlar soni
    path('regions/', views.region_list, name='region_list'),  # Regionlar ro'yxati
    path('regions/<int:pk>/in_city/', views.RegionListByCityView.as_view(), name='region_in_city'),  # Regionlarni shaharga qarab filtrlaydi

    # send-order/ url client workerlarni tanlab ularga order xaqida xabar berishi uchun
    path('send-order/', SendOrderToSelectedWorkersView.as_view(), name='send_order_to_workers'),

]
