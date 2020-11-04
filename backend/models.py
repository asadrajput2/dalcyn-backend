from django.db import models
from django_currentuser.db.models import CurrentUserField
from authentication.models import Address, CustomUser


class Crop(models.Model):
    SEASON_CHOICES = [
        ('RA', 'Rabi'),
        ('KH', 'Kharif'),
    ]

    CROP_TYPE_CHOICES = [
        ('FR', 'Fruit'),
        ('VG', 'Vegetable'),
        ('PL', 'Pulse'),
        ('SP', 'Spice'),
    ]

    common_name = models.CharField(
        max_length=256, blank=True, null=True, default="")
    species = models.CharField(max_length=256, blank=True, null=True)
    season = models.CharField(
        max_length=2, choices=SEASON_CHOICES, null=True, blank=True)
    crop_type = models.CharField(
        max_length=2, choices=CROP_TYPE_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.common_name + ' ' + self.species

    class Meta:
        db_table = "Crop"


class Farm(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    owner = CurrentUserField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    area = models.FloatField(blank=True, null=True)
    contract_status = models.BooleanField(default=True)
    crop = models.ManyToManyField(Crop)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Farm"


class Node(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farm.name + ' Node ' + str(self.id)

    class Meta:
        db_table = "Node"


class Parameter(models.Model):
    soil_moisture = models.FloatField(blank=True, null=True)
    soil_temp = models.FloatField(blank=True, null=True)
    salinity = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    nitrogen = models.FloatField(blank=True, null=True)
    phosphorus = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)


class TopLevel(Parameter):
    carbon_dioxide = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "TopLevelParam"


class MiddleLevel(Parameter):
    oxygen = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "MiddleLevelParam"


class BottomLevel(Parameter):

    class Meta:
        db_table = "BottomLevelParam"


class Prediction(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crop.common_name + ' ' + self.farm.name

    class Meta:
        db_table = "Prediction"
