from django.db import migrations

def populate_res_id(apps, schema_editor):
    Reservation = apps.get_model('home', 'Reservation')
    for index, reservation in enumerate(Reservation.objects.all(), start=1):
        reservation.res_id = index
        reservation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_reservation_res_id'),
    ]

    operations = [
        migrations.RunPython(populate_res_id),
    ]