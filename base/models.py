from django.db import models

class StoreTimezone(models.Model):
    store_id = models.IntegerField(primary_key=True)
    timezone_str = models.CharField(max_length=50)

    def __str__(self):
        return f"Store {self.store_id} - Timezone: {self.timezone_str}"

class StoreActivity(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    store_id = models.ForeignKey(StoreTimezone, on_delete=models.CASCADE)
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Store {self.store_id} - {self.status} at {self.timestamp_utc}"


class StoreBusinessHours(models.Model):
    DAY_OF_WEEK_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    store_id = models.ForeignKey(StoreTimezone, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

    def __str__(self):
        return f"Store {self.store_id} - {self.get_day_of_week_display()}: {self.start_time_local} to {self.end_time_local}"



