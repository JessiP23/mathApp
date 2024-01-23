from django.shortcuts import render, redirect, get_object_or_404
from .models import PostQuestion
from .forms import FormatQuestion
# Create your views here.

def question_list(request):
    list_question = PostQuestion.objects.all()
    return render(request, 'forum/question_list.html', {'list_question': list_question})

def post_question(request):
    if request.method=='POST':
        form = FormatQuestion(request.POST)
        if form.is_valid():
            setquestion = form.save(commit=False)
            setquestion.user = request.user
            setquestion.save()
            return redirect('forum:question_list')
    else:
        form = FormatQuestion()
    return render(request, 'forum/post_question.html', {'form':form})

def view_question(request, question_id):
    question = get_object_or_404(PostQuestion, id=question_id)
    return render(request, 'forum/question_view.html', {'question': question})
