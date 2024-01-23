from django.urls import path
from .views import view_question, question_list, post_question

app_name = 'forum'

urlpatterns = [
    path('question_list/', question_list, name="question_list"),
    path('<int:question_id>', view_question, name="view_question"),
    path('', post_question, name='post_question'),
]