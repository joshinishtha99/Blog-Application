# blog/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import BlogPost

# Testing Models
class BlogPostModelTests(TestCase):

    def test_string_representation(self):
        """
        Test that the BlogPost's string representation is its title
        """
        post = BlogPost(title="Test Post")
        self.assertEqual(str(post), post.title)

    def test_blogpost_creation(self):
        """
        Test that a BlogPost instance can be created and saved correctly
        """
        post = BlogPost.objects.create(title="New Post", content="Content for the new post")
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(post.title, "New Post")
        self.assertEqual(post.content, "Content for the new post")


# Testing Views
class BlogPostViewTests(TestCase):

    def setUp(self):
        """
        Create some initial BlogPost instances for view testing
        """
        BlogPost.objects.create(title="First Post", content="Content for the first post")
        BlogPost.objects.create(title="Second Post", content="Content for the second post")

    def test_blogpost_list_view(self):
        """
        Test that the blogpost list view returns a 200 status and contains the correct data
        """
        response = self.client.get(reverse('blogpost-list'))  # Assuming you have a view named 'blogpost-list'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_list.html')  # Make sure the right template is used
        self.assertContains(response, "First Post")
        self.assertContains(response, "Second Post")

    def test_blogpost_detail_view(self):
        """
        Test that the blogpost detail view returns a 200 status for a valid post
        """
        post = BlogPost.objects.get(title="First Post")
        response = self.client.get(reverse('blogpost-detail', kwargs={'pk': post.pk}))  # Assuming 'blogpost-detail' is your view name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_detail.html')
        self.assertContains(response, "Content for the first post")
