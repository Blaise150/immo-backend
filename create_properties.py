import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immo_api.settings')
django.setup()
print("=" * 60)
print("🚀 DÉBUT DU SCRIPT DE CRÉATION DES PROPRIÉTÉS")
print("=" * 60)
from properties.models import Property
from users.models import User

# Créer ou récupérer un utilisateur
try:
    user = User.objects.get(email='agent@immoapp.fr')
except User.DoesNotExist:
    user = User.objects.create_user(
        username='agent_immo',
        email='agent@immoapp.fr',
        password='Agent123!',
        first_name='Agent',
        last_name='Immobilier'
    )
    print("✅ Utilisateur agent créé")

# Villes et leurs codes postaux
cities_data = [
    ('Paris', ['75001', '75002', '75008', '75016', '75017']),
    ('Lyon', ['69001', '69002', '69003', '69006', '69007']),
    ('Nice', ['06000', '06100', '06200', '06300']),
    ('Monaco', ['98000']),
]

property_types = ['appartement', 'maison', 'studio', 'loft']
transaction_types = ['vente', 'location']

print("\n🏗️  Création des propriétés...\n")

for city, zip_codes in cities_data:
    print(f"📍 Création de 5 biens à {city}...")
    
    for i in range(5):
        bedrooms = random.randint(1, 5)
        surface = random.randint(30, 200)
        bathrooms = random.randint(1, min(3, bedrooms))
        prop_type = random.choice(property_types)
        transaction_type = random.choice(transaction_types)
        
        # Prix selon la ville
        if city == 'Monaco':
            base_price = random.randint(1000000, 5000000)
        elif city == 'Paris':
            base_price = random.randint(300000, 2000000)
        elif city == 'Nice':
            base_price = random.randint(250000, 1200000)
        else:  # Lyon
            base_price = random.randint(200000, 900000)
        
        # Prix pour location (diviser par 300-400)
        price = base_price if transaction_type == 'vente' else int(base_price / random.randint(300, 400))
        
        # Description selon le type
        descriptions = {
            'appartement': f"Magnifique appartement de {bedrooms} pièces situé au cœur de {city}. Lumineux et spacieux.",
            'maison': f"Belle maison familiale avec {bedrooms} chambres dans un quartier calme de {city}.",
            'studio': f"Studio moderne et fonctionnel idéalement situé à {city}.",
            'loft': f"Superbe loft de {surface}m² avec volumes exceptionnels à {city}."
        }
        
        property_data = {
            'title': f'{prop_type.capitalize()} {bedrooms}P - {city}',
            'description': descriptions.get(prop_type, f"Beau bien à {city}"),
            'property_type': prop_type,
            'transaction_type': transaction_type,
            'price': price,
            'surface': surface,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'city': city,
            'zip_code': random.choice(zip_codes),
            'address': f'{random.randint(1, 200)} Rue {random.choice(["de la République", "Victor Hugo", "des Lilas", "du Commerce"])}',
            'owner': user,
            'is_available': True
        }
        
        # Créer la propriété si elle n'existe pas déjà
        prop, created = Property.objects.get_or_create(
            title=property_data['title'],
            city=city,
            defaults=property_data
        )
        
        if created:
            print(f"  ✅ {prop.title} - {prop.price:,}€")

print("\n🎉 Toutes les propriétés ont été créées avec succès !")
print(f"\n📊 Total : {Property.objects.count()} biens dans la base de données")

# Afficher la répartition par ville
print("\n📍 Répartition par ville :")
for city, _ in cities_data:
    count = Property.objects.filter(city=city).count()
    print(f"   {city}: {count} biens")