from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    name = models.TextField(null=False)
    body = models.TextField(null=True)
    priority = models.IntegerField(default=3)
    due = models.DateField(null=True)
    finish = models.BooleanField(default=False)

    @staticmethod
    def getOrderByPriority():
        return Todo.objects.all().order_by('priority')
    
    @staticmethod
    def getOverDueNotFinished():
        return Todo.objects.filter(due__lt=timezone.now(), finish=False)

    def isOverDueNotFinished(self):
        return self.due < timezone.now() and self.finish==False

    def dueDateFormat(self):
        due = self.due
        return "%04d-%02d-%02d"%(due.year, due.month, due.day) if due!=None else ""

    def __str__(self):
        return "%s_%d_%s"%("Finished" if self.finish==True else "Ongoing", self.priority, self.name)
