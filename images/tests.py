from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .forms import UploadImageForm
from .models import Post


# Create your tests here.
class PostTest(TestCase):
    def test_image_upload(self):
        Post.objects.create(
            title = 'test',
            pub_date = datetime.date.today(),
            private = 1,
            image = '..//testfiles/leafs.jpg'
        )

    def test_title_max_length(self):
        user = Post.objects.get(id=1)
        max_length = user._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)


class ImageFormTest(TestCase):
    def test_private_field(self):
        form = UploadImageForm()
        self.assertEqual(form.fields['private'] == 1 or form.fields['private'] == 0)

    def test_date_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = UploadImageForm(data={'pub_date': date})
        self.assertFalse(form.is_valid())


##### TO-DO LIST #####
# 1. All images shown in home page are public
# 2. User viewing a particular page must be authenticated/logged in (myimages.html)
# 3. Uploaded images have a unique ID attached when uploaded to server
# 4. Max size for Images
# 5. Every image has an owner
