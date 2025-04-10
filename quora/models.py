from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='liked_answers',blank=True)

    def like_count(self):
        return self.likes.count()
    
    def __str__(self):
        return f"Answer to {self.question.title} by {self.author.username}"


