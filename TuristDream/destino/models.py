from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances



# Create your models here.
class Ciudad(models.Model):
	"""Model representing an author."""
	name = models.CharField(max_length=100)
	

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('ciudad-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name
		


        
class Destino(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.SET_NULL, null=True, blank=False)
    """summary = models.TextField(max_length=1000)"""
    url = models.URLField(max_length=100, default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    

    class Meta:
        ordering=['name']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('destino-detail', args=[str(self.id)])
