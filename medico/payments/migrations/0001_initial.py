# Generated by Django 3.0.12 on 2021-03-04 11:29

from django.db import migrations, models
import django.db.models.deletion
import medico.payments.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djstripe', '0007_2_4'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_visit', models.TextField(blank=True, max_length=1000, validators=[medico.payments.validators.validate_max_length])),
                ('stripe_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Customer')),
                ('stripe_payment_intent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.PaymentIntent')),
            ],
        ),
    ]
