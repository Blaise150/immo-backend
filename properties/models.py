from django.db import models

# Create your models here.
from django.db import models

class Property(models.Model):
    TRANSACTION_TYPES = (
        ('vente', 'Vente'),
        ('location', 'Location'),
    )
    
    PROPERTY_TYPES = (
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('studio', 'Studio'),
        ('villa', 'Villa'),
    )
    
    STATUS_CHOICES = (
        ('disponible', 'Disponible'),
        ('vendu', 'Vendu'),
        ('loué', 'Loué'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    reference = models.CharField(max_length=50, unique=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='disponible')
    
    surface = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=1)
    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, db_index=True)
    zip_code = models.CharField(max_length=10, db_index=True)
    
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title