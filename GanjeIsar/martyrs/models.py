from django.db import models

class Martyr(models.Model):
    title  = models.CharField(blank=True , null=True , max_length=70)
    description   = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True , null=True , upload_to='shahidavatars')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'martyrs'
        verbose_name = 'martyr'
        verbose_name_plural = 'martyrs'