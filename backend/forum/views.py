from django.shortcuts import render, redirect, get_object_or_404
from .models import PostQuestion, Comment
from .forms import FormatQuestion, CommentFormat
# Create your views here.

def question_list(request): 
    #Retrieve PostQuestion objects
    list_question = PostQuestion.objects.all()
    return render(request, 'forum/question_list.html', {'list_question': list_question})

def post_question(request):
    #POST request
    if request.method=='POST':
        #FormatQuestion form
        form = FormatQuestion(request.POST, request.FILES)
        if form.is_valid():
            setquestion = form.save(commit=False)
            #user that submitted the question become current user
            setquestion.user = request.user
            setquestion.save()
            return redirect('forum:question_list')
    #GET request
    else:
        #Start a new form
        form = FormatQuestion()
    return render(request, 'forum/post_question.html', {'form':form})

def view_question(request, question_id):
    #get PostQuestion based on the question_id parameter
    #if object does not exist, retrieve error 404
    question = get_object_or_404(PostQuestion, id=question_id)
    return render(request, 'forum/question_view.html', {'question': question})

def create_comment(request, question_id):
    specific_question = get_object_or_404(PostQuestion, id=question_id)

    #POST request
    if request.method == 'POST':
        #CommentFormat form validation
        form = CommentFormat(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.question_related = specific_question
            comment.save()
            return redirect('forum:view_question', question_id=question_id)
        #GET request
    else:
        #start a new form 
        form = CommentFormat()
    return render(request, 'forum/create_comment.html', {'form':form, 'question': specific_question})