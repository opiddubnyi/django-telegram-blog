from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()


class Post(models.Model):
    class Meta:
        """"""
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    created_time = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    # user = models.ForeignKey(User, verbose_name="Owner", null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)
    content = HTMLField(verbose_name="Post", max_length=2200000, blank=False, null=False)
    image = models.ImageField(verbose_name="Image", upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    title = models.CharField(verbose_name="Title", max_length=20, blank=False, null=False,
                             default=None)

    def __str__(self):
        return self.title


class PostTag(models.Model):
    class Meta:
        db_table = "post_tags"
        verbose_name = "Post tag"
        verbose_name_plural = "Post tags"

    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, blank=False,
                             null=False)
    tag = models.ForeignKey(Tag, verbose_name="Tag", on_delete=models.CASCADE, blank=False,
                            null=False)

    def __str__(self):
        return f"for '{self.post}' post"


"""
TODO: 
+ add link in view 
+ fix post display

add filters on tag to show posts
+pagination 
"""

