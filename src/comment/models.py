from django.db import models
from police.models import Police
from citizen.models import Citizen
from case.models import Case
# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    user1 = models.ForeignKey(Police, models.SET_NULL, blank=True, null=True)
    user2 = models.ForeignKey(Citizen, models.SET_NULL, blank=True, null=True)
    case  = models.ForeignKey(Case, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)
