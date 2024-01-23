from django.shortcuts import render, redirect, get_object_or_404
from .models import PostQuestion, Comment
from .forms import FormatQuestion, CommentFormat
# Create your views here.

def question_list(request):
    list_question = PostQuestion.objects.all()
    return render(request, 'forum/question_list.html', {'list_question': list_question})

def post_question(request):
    if request.method=='POST':
        form = FormatQuestion(request.POST, request.FILES)
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

def create_comment(request, question_id):
    specific_question = get_object_or_404(PostQuestion, id=question_id)

    if request.method == 'POST':
        form = CommentFormat(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.question_related = specific_question
            comment.save()
            return redirect('forum:view_question', question_id=question_id)
    else:
        form = CommentFormat()
    return render(request, 'forum/create_comment.html', {'form':form, 'question': specific_question})