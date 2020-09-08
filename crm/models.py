from django.db import models
from student.models import Student
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel
from datetime import date
from django.contrib.auth.models import  User
from decimal import Decimal
from django.conf import settings
# Create your models here.
class location1(models.Model):
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=23)
    city=models.CharField(max_length=23)

class Currency(models.Model):
    code = models.CharField(unique=True, max_length=3)
    pre_symbol = models.CharField(blank=True, max_length=1)
    post_symbol = models.CharField(blank=True, max_length=1)

    def __unicode__(self):
        return self.code

class Address(models.Model):
    contact_name=models.CharField(max_length=23)
    address_one=AddressField()
    town=models.CharField(max_length=34)
    postcode=models.CharField(_("zip code"), max_length=5, default="43701")
    state = models.CharField(max_length=34)

class InvoiceManager(models.Manager):
    def get_invoiced(self):
        return self.filter(invoiced=True, draft=False)

    def get_due(self):
        return self.filter(invoice_date__lte=date.today(),
                           invoiced=False,
                           draft=False)


class Invoice(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=34)
    invoice_id = models.CharField(unique=True, max_length=6, null=True,
                                  blank=True, editable=False)
    invoice_date = models.DateField(default=date.today)
    invoiced = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    paid_date = models.DateField(blank=True, null=True)

    objects = InvoiceManager()



    def __unicode__(self):
        return u'%s (%s)' % (self.invoice_id, self.total_amount())

    class Meta:
        ordering = ('-invoice_date', 'id')

    def total(self):
        total = Decimal('0.00')
        for item in self.items.all():
            total = total + item.total()
        return total

    def file_name(self):
        return u'Invoice %s.pdf' % self.invoice_id

