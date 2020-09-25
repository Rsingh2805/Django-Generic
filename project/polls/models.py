from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text