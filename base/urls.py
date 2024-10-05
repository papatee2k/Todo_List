from django.urls import path
from .views import TaskList,Taskdetail, Taskcreate,TaskUpdate,TaskDelete, CustomloginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomloginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='tasks'),
    path('task-create/',Taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),
    
]
