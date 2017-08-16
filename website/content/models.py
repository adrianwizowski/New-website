from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class ContactData(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title