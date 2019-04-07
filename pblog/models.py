from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 用户
class MUSER(models.Model):
    """Model definition for MUSER."""

    # TODO: Define fields here
    muser = models.OneToOneField(User, on_delete=models.CASCADE)
    # 头像
    head = models.ImageField(blank=True, null=True, upload_to='head', height_field=None, width_field=None, max_length=None)
    # False为普通用户 True为管理员
    types = models.BooleanField(default=False)
    # False为男 True为女
    gender = models.BooleanField(default=False)
    class Meta:
        """Meta definition for MUSER."""

        verbose_name = 'MUSER'
        verbose_name_plural = 'MUSERs'

    def __str__(self):
        """Unicode representation of MUSER."""
        return self.muser.username


# 文章
class MARTICLE(models.Model):
    """Model definition for MARTICLE."""

    # TODO: Define fields here
    # 作者
    writer = models.ForeignKey(User, related_name='article_writer', on_delete=models.CASCADE)
    # 标题
    title = models.CharField(max_length=500)
    # 内容
    content = models.CharField(blank=True, null=True, max_length=1000)
    # 创建时间
    ctime = models.DateTimeField(auto_now_add=True)
    # 是否审核
    audit = models.BooleanField(default=False)

    class Meta:
        """Meta definition for MARTICLE."""

        verbose_name = 'MARTICLE'
        verbose_name_plural = 'MARTICLEs'

    def __str__(self):
        """Unicode representation of MARTICLE."""
        return self.title

class MALBUM(models.Model):
    """Model definition for MALBUM."""

    # TODO: Define fields here
    user = models.ForeignKey(User, related_name='album_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500,blank=True, null=True,default='暂无描述')
    ctime = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(blank=True, null=True, upload_to='imgs', height_field=None, width_field=None, max_length=None)
    class Meta:
        """Meta definition for MALBUM."""

        verbose_name = 'MALBUM'
        verbose_name_plural = 'MALBUMs'

    def __str__(self):
        """Unicode representation of MALBUM."""
        return self.title

class MPHOTO(models.Model):
    """Model definition for MPHOTO."""

    # TODO: Define fields here
    album = models.ForeignKey(MALBUM, related_name='photo_album', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500,blank=True, null=True,default='暂无描述')
    pic = models.ImageField(blank=True, null=True,upload_to='imgs', height_field=None, width_field=None, max_length=None)
    ctime = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for MPHOTO."""

        verbose_name = 'MPHOTO'
        verbose_name_plural = 'MPHOTOs'

    def __str__(self):
        """Unicode representation of MPHOTO."""
        return self.title


class MCOMMENT(models.Model):
    """Model definition for MCOMMENT."""

    # TODO: Define fields here
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    article = models.ForeignKey(MARTICLE, related_name='comment_article', on_delete=models.CASCADE,blank=True, null=True)
    album = models.ForeignKey(MALBUM, related_name='comment_album', on_delete=models.CASCADE,blank=True, null=True)
    photo = models.ForeignKey(MPHOTO, related_name='comment_photo', on_delete=models.CASCADE,blank=True, null=True)
    content = models.CharField(max_length=1000)
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for MCOMMENT."""

        verbose_name = 'MCOMMENT'
        verbose_name_plural = 'MCOMMENTs'

    def __str__(self):
        """Unicode representation of MCOMMENT."""
        return self.content

class MPUBLISH(models.Model):
    """Model definition for MPUBLISH."""

    # TODO: Define fields here
    types = models.IntegerField(default=1)
    article = models.ForeignKey(MARTICLE, related_name='publish_article', on_delete=models.CASCADE,blank=True, null=True,default=None)
    photo = models.ForeignKey(MPHOTO, related_name='publish_photo', on_delete=models.CASCADE,blank=True, null=True,default=None)
    comment = models.ForeignKey(MCOMMENT, related_name='publish_comment', on_delete=models.CASCADE,blank=True, null=True,default=None)
    ctime = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for MPUBLISH."""

        verbose_name = 'MPUBLISH'
        verbose_name_plural = 'MPUBLISHs'

    def __str__(self):
        """Unicode representation of MPUBLISH."""
        if self.types == 1:
            return self.article.title
        elif self.types == 2:
            return self.photo.title
        else:
            return self.comment.content
        

