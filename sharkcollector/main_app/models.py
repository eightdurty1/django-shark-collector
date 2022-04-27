from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Shark(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()


#adding the __str__ method new code below
# def __str__(self):
#     return self.name


# Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})


# Add new Feeding model below Cat model
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
      max_length=1,
      # add the 'choices' field option
      choices=MEALS,
      # set the default value for meal to be 'B'
      default=MEALS[0][0]

      )
# Create a cat_id FK
shark = models.ForeignKey(Shark, on_delete=models.CASCADE)      

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']
