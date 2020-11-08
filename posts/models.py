from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
import os
from django.dispatch.dispatcher import receiver
# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_image/', blank=True)

    def __str__(self):
        return self.title

    def month_published(self):
        """
        Display month in string format 
        """
        return self.created_on.strftime('%B')

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': str(self.pk)})

    # Display newest on top
    class Meta:
        ordering = ['-created_on', ]


@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True,)
    updated_on = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': str(self.post.pk)})

    # Display newest on top
    class Meta:
        ordering = ['-created_on', ]
