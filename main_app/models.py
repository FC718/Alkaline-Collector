from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
# Create your models here.
class Fruit(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Alkaline(models.Model):
    name = models.CharField(max_length=100)
    # Number of charachters users are allowed to 
    # type in. Charfield(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=1000)
    # Create a M:M relationship with Fruit
    # Fruits is a realted Manager
    # Fruits is the Related Manager
    fruits = models.ManyToManyField(Fruit)

# Notice how this model is set up.
# This is how your table will be written


# Changing this instance method
# does not impact the database, therefore
# no make migrations is necessary
    def __str__(self) -> str:
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail',
        kwargs={'alkaline_id': self.id})


class Juicing(models.Model):
    date = models.DateField('Juicing Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0] 
    )
    # Create an alkaline_id FK
    alkaline = models.ForeignKey(
        Alkaline,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
