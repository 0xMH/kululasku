# Generated by Django 2.2.10 on 2020-02-20 14:07

import django.core.validators
from django.db import migrations, models
import localflavor.generic.models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='cc_email',
            field=models.EmailField(blank=True, help_text='Copy of the expense will be sent to the email.', max_length=254, null=True, validators=[django.core.validators.EmailValidator()], verbose_name='CC email address'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='iban',
            field=localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False, verbose_name='Bank account no'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='swift_bic',
            field=localflavor.generic.models.BICField(blank=True, max_length=11, null=True, verbose_name='BIC no'),
        ),
        migrations.AlterField(
            model_name='person',
            name='iban',
            field=localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False, verbose_name='Bank account no'),
        ),
        migrations.AlterField(
            model_name='person',
            name='swift_bic',
            field=localflavor.generic.models.BICField(blank=True, max_length=11, null=True, verbose_name='BIC no'),
        ),
    ]