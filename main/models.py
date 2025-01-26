from django.db import models

#post uchun model
class Post(models.Model):
    image=models.ImageField()
    date=models.DateField()
    text=models.TextField(default='Salom!')

    def __str__(self):
        return self.text

turlari=[
    ('Phishing', 'Phishing'),
    ('DOS', 'DOS'),
    ('DDOS', 'DDOS'),
    ('Malware', 'Malware'),
    ('SQL Injection', 'SQL Injection'),
]

tillar=[
    ('Python', 'Python'),
    ('Golang', 'Golang'),
    ('Java Script', 'JS'),
    ('Bat', 'Bat'),
]

class PythonContent(models.Model):
    tili=models.CharField(max_length=50,choices=tillar,null=False,blank=False)
    turlari=models.CharField(max_length=50,choices=turlari,null=False,blank=False)
    izoh=models.TextField(null=False,blank=False)
    kod=models.TextField(null=False,blank=False)

class GolangContent(models.Model):
    tili=models.CharField(max_length=50,choices=tillar,null=False,blank=False)
    turlari=models.CharField(max_length=50,choices=turlari,null=False,blank=False)
    izoh=models.TextField(null=False,blank=False)
    kod=models.TextField(null=False,blank=False)
    
class JSContent(models.Model):
    tili=models.CharField(max_length=50,choices=tillar,null=False,blank=False)
    turlari=models.CharField(max_length=50,choices=turlari,null=False,blank=False)
    izoh=models.TextField(null=False,blank=False)
    kod=models.TextField(null=False,blank=False)

class BatContent(models.Model):
    tili=models.CharField(max_length=50,choices=tillar,null=False,blank=False)
    turlari=models.CharField(max_length=50,choices=turlari,null=False,blank=False)
    izoh=models.TextField(null=False,blank=False)
    kod=models.TextField(null=False,blank=False)