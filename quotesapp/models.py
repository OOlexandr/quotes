from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    quote = models.TextField()

    def __str__(self):
        return f"{self.quote}"