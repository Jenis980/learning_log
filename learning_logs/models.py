from django.db import models # models is module. model is just a class.

# Create your models here.
class Topic(models.Model):
  """A topic the user is learning about."""
  text = models.CharField(max_length=2000)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return a string represntation of the model."""
    return self.text