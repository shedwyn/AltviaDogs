"""Objects/Models/Classes and all that makes those up"""

# from django.contrib.auth.models import User
from django.db import models


class Dog(models.Model):
    """Dog Descriptors"""
    # eventually want to add ImageField, URL (for IG or FB link)

    name = models.CharField(max_length=15)
    owner = models.ForeignKey('Owner')

    def __str__(self):
        """docstring"""
        return 'Dog_str({}, {}, {})'.format(self.id, self.name, self.owner)

    def __repr__(self):
        """docstring"""
        return 'Dog_repr({!r}, {!r}, {!r})'.format(
            self.id, self.name, self.owner)


class Owner(models.Model):
    """Owner descriptors, will supplant with User eventually"""

    name = models.CharField(max_length=40)
    email = models.EmailField()
    slack = models.CharField()

    def __str__(self):
        """docstring"""
        return 'Owner_str({}, {}, {})', format(
            self.id, self.name, self.email, self.slack)

    def __repr__(self):
        """docstring"""
        return 'Owner_repr({!r}, {!r}, {!r})'.format(
            self.id, self.name, self.email, self.slack)


class RecordFile(models.Model):
    """Record of Shout-out or Oopsie

    links to Dog and Owner
    """

    REC_TYPE_CHOICES = (
        ('SO', 'Shout-Out'), ('O', 'Oopsie')
    )

    title = models.CharField(max_length=50)
    dogs = models.ManyToMany(Dog)
    date = models.DateField()
    rec_type = models.Charfield(choices=REC_TYPE_CHOICES)
    description = models.TextField()
