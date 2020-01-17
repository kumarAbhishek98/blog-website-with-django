from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-detail', kwargs={'pk':self.pk})

class ContactForm(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=200)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.name		