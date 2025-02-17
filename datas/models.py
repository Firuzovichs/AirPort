from django.db import models
import uuid
from shipment.models import Capital, Country, StatusModel, CategoryMailModel, TypeModel, SexModel, TransitModel

class Dispatch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE, null=True,blank=True)
    tranzit = models.ForeignKey(TransitModel, on_delete=models.CASCADE,null=True,blank=True)
    sex_1 = models.ForeignKey(SexModel, null=True, blank=True, on_delete=models.CASCADE, related_name='otkuda',default=None)
    sex_2 = models.ForeignKey(SexModel, null=True, blank=True, on_delete=models.CASCADE, related_name='kuda', default=None)
    data_reception = models.DateTimeField(null=True,blank=True)
    data_dispatch = models.DateTimeField(null=True,blank=True)
    dispatches = models.CharField(max_length=255,null=True,blank=True)
    to_country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True, related_name="otkuda_country")
    to_capital = models.ForeignKey(Capital, on_delete=models.CASCADE,null=True,blank=True, related_name="otkuda_capital")
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True, related_name="kuda_country")
    from_capital = models.ForeignKey(Capital, on_delete=models.CASCADE,null=True,blank=True, related_name="kuda_capital")
    status = models.ForeignKey(StatusModel, null=True, blank=True, on_delete=models.SET_NULL)
    category_status = models.ForeignKey(CategoryMailModel, on_delete=models.CASCADE, default=None,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    note = models.TextField(null=True, blank=True)
    flightNumber = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.status is not None:
            return f" {self.status.id} ({self.quantity} ta, {self.weight} kg)"
        return f"Status belgilanmagan ({self.quantity} ta, {self.weight} kg)"