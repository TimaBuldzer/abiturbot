from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        db_table = 'subjects'

    def __str__(self):
        return self.name if self.name else '--empty--'


class SubjectTest(models.Model):
    question = models.TextField()
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subject test'
        verbose_name_plural = 'Subject tests'
        db_table = 'subject_tests'

    def __str__(self):
        return self.question[:10]


class Answer(models.Model):
    question = models.ForeignKey(SubjectTest, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.TextField()
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'

    def __str__(self):
        return self.answer[:10]
