from django.conf import settings
from django.db import models
from django.urls import reverse


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('List', on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text


class List(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
    )
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_lists')

    def get_absolute_url(self):
        return reverse('view_list', args=[self.pk])

    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_

    @property
    def name(self):
        return self.item_set.first().text
