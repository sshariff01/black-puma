from django.db import models

# Remember the DRY Principle

class Poll(models.Model):
    def __unicode__(self):
        return self.question

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

class Choice(models.Model):
    def __unicode__(self):
        return self.choice_text

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
