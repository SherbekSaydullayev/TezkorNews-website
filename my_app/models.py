from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100,null=False,blank=False)

	def __str__(self):
		return self.name



class News(models.Model):
	title = models.CharField(max_length=300,null=False,blank=True)
	image = models.ImageField(upload_to='image/',blank=True)
	text = models.TextField()
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title