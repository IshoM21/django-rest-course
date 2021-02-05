from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTest(TestCase):
    
    def setUp(self):
        
        instance = Post.objects.create(title='Curso de Django', description='Cursode django')
        instance.save()
        
        instance = Post.objects.create(title='Taller de Django', description='Taller de django')
        instance.save()
        
    def test_for_post(self):
        print(Post.objects.all())
        print(Post.objects.filter(title='Curso de Django'))
        print(Post.objects.filter(title__icontains='Django'))
        print(Post.objects.get(pk=1))
        instance = Post.objects.get(pk=1)
        instance.title = 'Curso por Raul'
        instance.save()
        print(Post.objects.get(pk=1))