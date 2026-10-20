
import os
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.db import migrations


def create_admin_user(apps, schema_editor):
    # Only create the account when running against a configured
    # deployment database. Local SQLite development is unaffected.
    if not os.environ.get("DATABASE_URL"):
        return

    username = os.environ.get("DJANGO_ADMIN_USERNAME")
    email = os.environ.get("DJANGO_ADMIN_EMAIL")
    password = os.environ.get("DJANGO_ADMIN_PASSWORD")

    if not username or not email or not password:
        raise RuntimeError(
            "Set DJANGO_ADMIN_USERNAME, DJANGO_ADMIN_EMAIL, "
            "and DJANGO_ADMIN_PASSWORD in Render Environment "
            "before deploying."
        )

    User = apps.get_model(
        *settings.AUTH_USER_MODEL.split(".")
    )

    user, created = User.objects.using(
        schema_editor.connection.alias
    ).get_or_create(
        username=username,
        defaults={
            "email": email,
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )

    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.password = make_password(password)
    user.save(
        using=schema_editor.connection.alias
    )


class Migration(migrations.Migration):
    dependencies = [
        ("details", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_admin_user,
            migrations.RunPython.noop,
        ),
    ]
