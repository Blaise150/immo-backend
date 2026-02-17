import os
import django

print("\n" + "=" * 80)
print("🔐 DÉBUT DU SCRIPT DE CRÉATION DU SUPERUSER")
print("=" * 80)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immo_api.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@immoapp.fr'
password = 'Admin123!'

print(f"\n📝 Tentative de création du superuser '{username}'...")

try:
    if User.objects.filter(username=username).exists():
        print(f"✅ Le superuser '{username}' existe déjà.")
        user = User.objects.get(username=username)
        print(f"   📧 Email: {user.email}")
        print(f"   👑 Superuser: {user.is_superuser}")
        print(f"   👔 Staff: {user.is_staff}")
    else:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name='Admin',
            last_name='ImmoApp'
        )
        print(f"✅ Superuser '{username}' créé avec succès!")
        print(f"   📧 Email: {email}")
        print(f"   🔑 Password: {password}")
        print(f"   👑 Superuser: {user.is_superuser}")
        print(f"   👔 Staff: {user.is_staff}")
        print(f"\n🌐 Accédez à l'admin sur: /admin/")
        print(f"   Username: {username}")
        print(f"   Password: {password}")
except Exception as e:
    print(f"❌ ERREUR lors de la création du superuser:")
    print(f"   {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("🏁 FIN DU SCRIPT")
print("=" * 80 + "\n")