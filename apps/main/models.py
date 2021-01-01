from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    show = models.BooleanField(default=True)

    class Meta:
        db_table = 'sources'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        db_table = 'subjects'

    def __str__(self):
        return self.name if self.name else '--empty--'


class Question(models.Model):
    question = models.TextField()
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'questions'

    def __str__(self):
        return self.question[:10]


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.TextField()
    letter = models.CharField(max_length=1, blank=True, null=True)
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'

    def __str__(self):
        return self.answer[:10]
