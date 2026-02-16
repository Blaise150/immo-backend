from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from properties.models import Property
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        # Créer user test
        if not User.objects.filter(email='john@test.fr').exists():
            User.objects.create_user(
                username='john',
                email='john@test.fr',
                password='test123',
                first_name='John',
                last_name='Doe'
            )
            self.stdout.write('✓ User créé')

        CITIES = {
            'Paris': ['75001', '75002', '75003'],
            'Monaco': ['98000'],
            'Nice': ['06000', '06100'],
            'Lyon': ['69001', '69002'],
            'Marseille': ['13001', '13002']
        }

        count = 0
        for city, zips in CITIES.items():
            num = 30 if city == 'Paris' else 15
            for i in range(num):
                surface = random.randint(30, 200)
                rooms = random.randint(1, 5)
                
                Property.objects.create(
                    title=f"Appartement {rooms}P - {city}",
                    description=f"Magnifique bien à {city}. Surface {surface}m².",
                    reference=f"{city[:3].upper()}{count:04d}",
                    transaction_type=random.choice(['vente', 'location']),
                    property_type=random.choice(['appartement', 'maison', 'studio']),
                    price=random.randint(100000, 1000000),
                    surface=surface,
                    rooms=rooms,
                    bedrooms=max(1, rooms-1),
                    bathrooms=1,
                    address=f"{random.randint(1, 200)} Rue Test",
                    city=city,
                    zip_code=random.choice(zips),
                    status='disponible',
                    featured=(count % 10 == 0)
                )
                count += 1

        self.stdout.write(f'✅ {count} biens créés!')