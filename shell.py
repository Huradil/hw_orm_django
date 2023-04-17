from blog.models import *
from django.db.models import Q,Subquery


author1=Author.objects.create(name='Nursultan Berdiev',email='nursultanberdiev@gamail.com',username='nursultanberdiev',date_register='2021-01-04')
author2=Author.objects.create(name='Lu Veronica',email='ronilyu@gamail.com',username='ronic',date_register='2023-03-12')
author3=Author.objects.create(name='Toctosunova Chynara',email='chynara0409@gamail.com',username='chynara',date_register='2023-11-21')

article1=Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды')
article2=Article.objects.create(title="Зачем нужно использовать кроссплатформенную систему")
article3=Article.objects.create(title="Сравниваем Java и Python или с чего лучше начать")
article4=Article.objects.create(title="Новый ChatGPT-4: в чем его особенность")
article5=Article.objects.create(title="История компании Boston Dynamics. Как появлялись их роботы")

p1=Publication.objects.create(author_id=13,article_id=1)
p2=Publication.objects.create(author_id=13,article_id=2)
p3=Publication.objects.create(author_id=13,article_id=3)
p4=Publication.objects.create(author_id=14,article_id=4)
p5=Publication.objects.create(author_id=15,article_id=5)

Author.objects.all().order_by('date_register')
Article.objects.filter(author__name__contains='Nursultan')
Author.objects.filter(date_register__lt='2022-10-10')
articles=Article.objects.all()
articles_list=list(articles.values('author__username','title'))


authors=Author.objects.all()
Article.objects.get(id=2).author.add(authors[2])
Article.objects.get(id=3).author.add(authors[1])

articles_endswith_gmail=Article.objects.filter(author__email__endswith='@gamail.com',publication__date_published__lt='2024-04-18')
articles_endswith_gmail

articles_q=Article.objects.filter(Q(author__email__endswith='@gamail.com'),Q(publication__date_published__lt='2024-04-18'))
articles_q

article_join=Article.objects.filter(author__email__endswith='@gamail.com') & Article.objects.filter(publication__date_published__lt='2024-04-18')
article_join

article_no_veronica=Article.objects.exclude(author__name='Lu Veronica')
article_no_veronica

article_no_veronica_q=Article.objects.filter(~Q(author__name='Lu Veronica'))
article_no_veronica_q

authors=Author.objects.all().values('username')
authors

author_veronica_chynara=Author.objects.filter(Q(name__icontains='chynara') | Q(name__icontains='veronica'),~Q(date_register='2021-01-04'))
author_veronica_chynara



