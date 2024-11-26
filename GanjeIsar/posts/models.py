from django.db import models


from users.models import MyUser



class Post(models.Model):
    title  = models.CharField(blank=True , null=True , max_length=50)
    text   = models.TextField(blank=True , null=True )
    avatar = models.ImageField(blank=True , null=True , upload_to='avatars')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post , related_name='comment' ,on_delete=models.CASCADE)
    text = models.TextField(null=True , blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    writer = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.title

    class Meta:
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'