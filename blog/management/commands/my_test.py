from django.core.management.base import BaseCommand
from blog.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        posts_list = Post.objects.all()
        for post in posts_list:
            print(post.id)

