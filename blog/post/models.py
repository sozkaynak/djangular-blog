from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategori Adı')
    slug = models.SlugField(unique=True, max_length=210, verbose_name='Kategori Url', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:topic', args=[self.slug])

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Topic.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Topic, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Başlık')
    slug = models.SlugField(unique=True, max_length=210, verbose_name='Yazı Url', editable=False)
    text = RichTextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    topic_name = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='topics')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.topic_name.slug, self.slug])

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['published_date']

# class PostComment(models.Model):
#    post = models.ForeignKey('blog.Post', related_name='comments',
#                             on_delete=models.CASCADE)
#
#    name = models.CharField(max_length=200, verbose_name='İsim')
#    content = models.TextField(verbose_name='Yorum')
#
#    created_date = models.DateTimeField(auto_now_add=True)
