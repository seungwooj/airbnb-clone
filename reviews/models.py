from django.db import models
from core import models as core_models


# Create your models here.
class Review(core_models.AbstractTimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    cleanliness = models.DecimalField(max_digits=2, decimal_places=1)
    accuracy = models.DecimalField(max_digits=2, decimal_places=1)
    communication = models.DecimalField(max_digits=2, decimal_places=1)
    location = models.DecimalField(max_digits=2, decimal_places=1)
    check_in = models.DecimalField(max_digits=2, decimal_places=1)
    value = models.DecimalField(max_digits=2, decimal_places=1)
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.cleanliness
            + self.accuracy
            + self.communication
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg"
