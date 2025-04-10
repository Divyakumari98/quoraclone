from django.urls import path
from .views import (
    QuestionListView, QuestionCreateView, QuestionDetailView,
    AnswerLikeView, RegisterView
)
from .views import RegisterView, LoginView, LogoutView, QuestionListView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('ask/', QuestionCreateView.as_view(), name='ask_question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('like/<int:answer_id>/', AnswerLikeView.as_view(), name='like_answer'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', QuestionListView.as_view(), name='question_list'),
]
