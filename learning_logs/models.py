from django.db import models # models is module. model is just a class.

# Create your models here.
class Topic(models.Model):
  """A topic the user is learning about."""
  text = models.CharField(max_length=2000)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return a string represntation of the model."""
    return self.text
  
class Entry(models.Model):
  """ Something specific learned about a topic"""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField(Topic)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'entries'

    def _str_(self):
      """Return a string representation of the model."""
      return self.text[:50] + "..."