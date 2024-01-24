from django.urls import path
from .views import view_question, question_list, post_question, create_comment
from django.conf.urls.static import static
from django.conf import settings
 
app_name = 'forum'

urlpatterns = [
    path('question_list/', question_list, name="question_list"),
    path('<int:question_id>', view_question, name="view_question"),
    path('', post_question, name='post_question'),
    path('<int:question_id>/create_comment/', create_comment, name="create_comment"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)