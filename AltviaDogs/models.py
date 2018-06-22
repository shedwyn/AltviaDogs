"""Objects/Models/Classes and all that makes those up"""

# from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    """Owner descriptors, may replace with User eventually"""

    name = models.CharField(max_length=40)
    email = models.EmailField()
    # slack = models.CharField()

    def __str__(self):
        """docstring"""
        return 'Owner_str({}, {}, {})'.format(
            self.id, self.name, self.email
        )

    def __repr__(self):
        """docstring"""
        return 'Owner_repr({!r}, {!r}, {!r})'.format(
            self.id, self.name, self.email
        )


class Dog(models.Model):
    """Dog Elements, links to Owner/User, DogDay, eventually to DogRecord"""
    # eventually want to add ImageField, URL (for IG or FB link)

    name = models.CharField(max_length=15)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)

    def __str__(self):
        """docstring"""
        return 'Dog_str({}, {}, {})'.format(self.id, self.name, self.owner)

    def __repr__(self):
        """docstring"""
        return 'Dog_repr({!r}, {!r}, {!r})'.format(
            self.id, self.name, self.owner)


class DogDay(models.Model):
    """Given visit day with dogs assigned, link to Dog"""

    date_of_record = models.DateField(auto_now=False, auto_now_add=False)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        """docstring"""
        return 'DogDay_str({},{},{})'.format(
            self.id, self.date_of_record, self.dogs)


# class RecordFile(models.Model):
#    """Record of Shout-out or Oopsie
#
#    links to Dog and Owner
#    """
#
#    REC_TYPE_CHOICES = (
#        ('SO', 'Shout-Out'), ('O', 'Oopsie')
#    )
#
#    title = models.CharField(max_length=50)
#    dogs = models.ManyToMany(Dog)
#    date = models.DateField()
#    rec_type = models.Charfield(choices=REC_TYPE_CHOICES)
#    description = models.TextField()
