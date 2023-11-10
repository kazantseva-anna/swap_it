from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='available')

    options = (
        ('available', 'Available'),
        ('reserved', 'Reserved'),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='available')
    objects = models.Manager()
    newmanager = NewManager()

    def get_absolute_url(self):
        return reverse('feed:post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title