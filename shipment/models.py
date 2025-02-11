from django.db import models
import uuid



class StatusModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    
class TypeModel(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

class SexModel(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


class TransitModel(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
    
class ReysModel(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name



class CategoryMailModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name

class Capital(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class CountryCapital(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    capital = models.OneToOneField(Capital, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.capital.name} is the capital of {self.country.name}"    
