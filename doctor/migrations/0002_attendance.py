# Generated by Django 2.1.5 on 2019-09-10 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attend', models.BooleanField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_booking', to='doctor.Booking')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_patient', to='doctor.Patient')),
            ],
        ),
    ]