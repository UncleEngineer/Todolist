from django.urls import path
from .views import * 
# * ดึงมาทุกฟังชั่นใน views.py

urlpatterns = [
    path('', Home),
    path('api/all-todolist/',all_todolist), # localhost:8000/api/all-todolist
    path('api/post-todolist', post_todolist),
    path('api/update-todolist/<int:TID>', update_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolist),
]