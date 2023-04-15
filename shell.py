from blog.models import *

author1=Author.objects.create(name='Nursultan Berdiev',email='nursultanberdiev@gamail.com',username='nursultanberdiev',date_register='2021-01-04')
author2=Author.objects.create(name='Lu Veronica',email='ronilyu@gamail.com',username='ronic',date_register='2023-03-12')
author3=Author.objects.create(name='Toctosunova Chynara',email='chynara0409@gamail.com',username='chynara',date_register='2023-11-21')

article1=Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды')
article2=Article.objects.create(title="Зачем нужно использовать кроссплатформенную систему")
article3=Article.objects.create(title="Сравниваем Java и Python или с чего лучше начать")
article4=Article.objects.create(title="Новый ChatGPT-4: в чем его особенность")
article5=Article.objects.create(title="История компании Boston Dynamics. Как появлялись их роботы")

p1=Publication(author_id=13,article_id=1)
p2=Publication(author_id=13,article_id=2)
p3=Publication(author_id=13,article_id=3)
p4=Publication(author_id=14,article_id=4)
p5=Publication(author_id=15,article_id=5)

Author.objects.all().order_by('date_register')
Article.objects.filter(author__name__contains='Nursultan')
Author.objects.filter(date_register__lt='2022-10-10')
articles=Article.objects.all()
articles_list=list(articles.values('author__username','title'))



