from django.db import models

class ChurnModel(models.Model):
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField()
    MembershipType = models.CharField(max_length=30)
    PreferredCategory = models.CharField(max_length=50)
    TotalOrders = models.IntegerField()
    TotalSpent = models.FloatField()
    LastPurchaseDaysAgo = models.IntegerField()
    PurchaseFrequencyPerMonth = models.FloatField()
    AppLoginFrequency = models.IntegerField()
    CouponUsageCount = models.IntegerField()
    ReturnCount = models.IntegerField()
    SatisfactionScore = models.FloatField()

    def __str__(self):
        return f"{self.Gender} - {self.Age}"
