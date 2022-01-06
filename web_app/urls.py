from django.urls import path, include
from . import views
from .views import MakeReservation, AddComment, AddPatient, ScheduleVisit, AddCommentDoc

urlpatterns = [
    path('home/', views.home, name='home'),
    path('planned_visits/', views.planned_visits, name='planned_visits'),
    path('history_visits/', views.history_visits, name='history_visits'),
    path('patients_list/', views.get_patients, name='patients_list'),
    path('reservation/', MakeReservation.as_view(), name='reserve'),
    path('comments/', AddComment.as_view(), name='comment'),
    path('add/', AddPatient.as_view(), name='add'),
    path('visit/', ScheduleVisit.as_view(), name='visit'),
    path('doc_comments/', AddCommentDoc.as_view(), name='doc_comm'),
]
