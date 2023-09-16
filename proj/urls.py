from django.urls import path

from app1.views import test_task

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [path('submit_task/', test_task, name='submit_task')]
