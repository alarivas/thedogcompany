from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	web_page = models.URLField()

	class Meta:
		db_table = 'Company'

	def __str__(self):
		return self.name

class Laptop(models.Model):
	model = models.CharField(max_length=30)
	serial_code = models.CharField(max_length=15)

	class Meta:
		db_table = 'Laptop'

	def __str__(self):
		return self.model

class Employee(models.Model):
	name = models.CharField(max_length=50)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	laptop = models.OneToOneField(Laptop, on_delete=models.CASCADE)

	class Meta:
		db_table = 'Employee'

	def __str__(self):
		return self.name