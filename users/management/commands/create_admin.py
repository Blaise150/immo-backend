from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crée un superuser admin si il n\'existe pas'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        username = 'admin'
        email = 'admin@immoapp.fr'
        password = 'Admin123!'
        
        self.stdout.write("=" * 80)
        self.stdout.write(self.style.SUCCESS('🔐 CRÉATION DU SUPERUSER'))
        self.stdout.write("=" * 80)
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS(f'✅ Superuser "{username}" existe déjà'))
            self.stdout.write(f'   Email: {user.email}')
            self.stdout.write(f'   Superuser: {user.is_superuser}')
            self.stdout.write(f'   Staff: {user.is_staff}')
        else:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                first_name='Admin',
                last_name='ImmoApp'
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Superuser "{username}" créé!'))
            self.stdout.write(f'   Email: {email}')
            self.stdout.write(f'   Password: {password}')
            
        self.stdout.write("=" * 80)