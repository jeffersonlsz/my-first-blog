import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
sys.path.append('../../')
from faker import Faker
#from faker.providers import company
import django
django.setup()

from django.contrib.auth.models import User
from blog.models import Post

from django.utils import timezone



if __name__ == '__main__':

    faker = Faker('pt_BR')
    user = User.objects.get(username='ola')
    print(user)
    posts = Post.objects.all()
    print(posts)

    #p_title = faker.catch_phrase()
    #p_text = faker.text(max_nb_chars=1500, ext_word_list=None)
    #Post.objects.create(author=user, title=p_title, text=p_text)
    #post = Post(author=user, title=p_title, text=p_text)
    #post.publish()

    i=0
    for i in range(50):
        p_title = faker.catch_phrase()
        p_text = faker.text(max_nb_chars=1500, ext_word_list=None)
        #Post.objects.create(author=user, title=p_title, text=p_text)
        post = Post(author=user, title=p_title, text=p_text)
        post.publish()
