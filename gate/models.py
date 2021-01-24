from django.db import models

# Create your models here.
class Question(models.Model):
    Year = models.IntegerField()
    Option = models.CharField(max_length=30)
    questions = models.ImageField(upload_to='pics')
    choice_1 = [('Compiler Design','Compiler Design'),('Computer Architecture','Computer Architecture'),
                ('Programming and Structures','Programming and Structures'),('Algorithms','Algorithms'),
                ('Theory of Computation','Theory of Computation'),('Operating System','Operating System'),
                ('Databases','Databases'),('Computer Networks','Computer Networks'),('Digital Logic','Digital Logic'),
                ('Discrete Mathematics','Discrete Mathematics'),('Linear Algebra','Linear Algebra'),('Calculus','Calculus'),
                ('Probability','Probability')]
    Topic = models.CharField(max_length=100,choices=choice_1)
    choice_2 = [('GATE_2019','GATE_2019'),]
    Gate = models.CharField(max_length=100,choices=choice_2,default=None)
