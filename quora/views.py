
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Question, Answer
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'quora/question_list.html'
    ordering = ['-created']

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'quora/ask_question.html'
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionDetailView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        answers = Answer.objects.filter(question=question)
        form = AnswerForm()
        return render(request, 'quora/question_detail.html', {
            'question': question,
            'answers': answers,
            'form': form
        })

    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
        return redirect('question_detail', pk=pk)

class AnswerLikeView(LoginRequiredMixin, View):
    def get(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)
        answer.likes.add(request.user)
        return redirect('question_detail', pk=answer.question.id)

# class RegisterView(View):
#     def get(self, request):
#         form = RegisterationForm()
#         return render(request, 'quora/register.html', {'form': form})

#     def post(self, request):
#         form = RegisterationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('question_list')
#         return render(request, 'quora/register.html', {'form': form})

# class UserLoginView(LoginView):
#     template_name = 'quora/login.html'

# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('login')
class RegisterView(View):
    def get(self, request):
        form = RegisterationForm()
        return render(request, 'quora/register.html', {'form': form})

    def post(self, request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        return render(request, 'quora/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'quora/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('question_list')
        return render(request, 'quora/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
