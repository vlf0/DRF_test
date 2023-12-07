from django.db import models


class Woman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_alive = models.BooleanField(default=False)
    kind = models.ForeignKey(to='Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.name


class DeletedPost(models.Model):
    row_id = models.IntegerField()
    title = models.CharField(max_length=255)
    delete_time = models.DateTimeField(auto_now_add=True)

