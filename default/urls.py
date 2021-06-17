from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('poll2/', views.poll_list), 
    path('', RedirectView.as_view(url='poll/')),
    path('poll/', views.PollList.as_view()), 
    path('poll/<int:pk>/', views.PollDetail.as_view()name='poll_view'), 
    path('option/<int:oid>/', views.PollVote.as_view()),
    path("poll/create/",views.pollcreate.as_view()),
    path('option/create/<int:pid>/', views.OptionCreate.as_view()),
]
