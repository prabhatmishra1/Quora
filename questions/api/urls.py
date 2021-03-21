from rest_framework import routers
from questions.api.views import QuestionViewSet,AnswerCreateAPIView,AnswerListAPIView, AnswerRUDAPIView, AnswerLikeAPIView
from django.urls import path

router = routers.SimpleRouter()
router.register(r'questions',QuestionViewSet)

urlpatterns = [
    path('create_answers/<slug:slug>/', AnswerCreateAPIView.as_view(),name="create-answer"),
    path('get_answers/<slug:slug>/', AnswerListAPIView.as_view(),name="answer-list"),
    path('update_delete_answers/<int:pk>/', AnswerRUDAPIView.as_view(),name="answer-details"),
    path('like_dislike_answers/<int:pk>/', AnswerLikeAPIView.as_view(),name="answer-like"),
]
urlpatterns+= router.urls