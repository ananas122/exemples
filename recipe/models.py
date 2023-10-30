python
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  ingredients = models.TextField()
  instructions = models.TextField()
  time = models.IntegerField()

  def __str__(self):
    return self.title
