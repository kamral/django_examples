from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    #Поле slug будет использоваться для создания прекрасных и
    # удобных URL-адресов для записей блога(blog posts).
    # Мы добавили параметр unique_for_date в это поле, чтобы
    # можно было построить уникальные URL-адреса содержащие
    # title поста и дату его публикации
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #author: это поле ForeignKey. В этом поле определяется
    # отношение «многие к одному». Мы сообщаем о том, что каждая запись
    # написана пользователем, и пользователь можетсоздать сколько угодно постов(posts).
    #author: это поле ForeignKey. В этом поле определяется отношение «многие к одному».
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    #publish : этот параметр DateTime указывает, когда была опубликована запись.
    # По умолчанию время определенио параметром timezone-aware datetime.now
    publish = models.DateTimeField(default=timezone.now)
    #created : этот DateTime параметр указывает, когда был создан пост. Поскольку
    # мы используем auto_now_add здесь, дата будет автоматически добавлена
    # при создании объекта.
    created = models.DateTimeField(auto_now_add=True)
    #updated : этот DateTime параметр указывает на последний
    # момент обновления этой записи. Поскольку мы используем auto_now здесь,
    # дата будет автоматически обновляться при сохранении объекта.
    updated = models.DateTimeField(auto_now=True)
    #status : это поле для отображения статуса записи(опубликован\неопубликован).
    # Мы используем параметр выбора,поэтому значение этого поля
    # может быть задано только для одного из этих вариантов.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title