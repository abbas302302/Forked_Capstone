from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f"CarMake name={self.name} description={self.description}"

class CarModel(models.Model):
    TYPE_SEDAN = "Sedan"
    TYPE_SUV = "SUV"
    TYPE_WAGON = "WAGON"
    TYPE_ETC = "Others"
    TYPE_CHOICES = (
        (TYPE_SEDAN, "Sedan"),
        (TYPE_SUV, "SUV"),
        (TYPE_WAGON, "WAGON"),
        (TYPE_ETC, "Others"))
    makeId = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    dealerId = models.IntegerField(null=False)
    type = models.CharField(max_length=128, choices=TYPE_CHOICES, default=TYPE_SEDAN)
    year = models.DateField()
    def __str__(self):
        return f"dealerId={self.dealerId} name={self.name} type={self.type} year={self.year}"




# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
