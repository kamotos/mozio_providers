# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('ZMK', 'Zambian Kwacha'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('LTL', 'Lithuanian Litas'), ('ISK', 'Iceland Krona'), ('ARS', 'Argentine Peso'), ('DJF', 'Djibouti Franc'), ('XPT', 'Platinum'), ('BSD', 'Bahamian Dollar'), ('HTG', 'Haitian gourde'), ('TZS', 'Tanzanian Shilling'), ('XFU', 'UIC-Franc'), ('GYD', 'Guyana Dollar'), ('VEF', 'Bolivar Fuerte'), ('HKD', 'Hong Kong Dollar'), ('MWK', 'Malawian Kwacha'), ('RUB', 'Russian Ruble'), ('SLL', 'Leone'), ('MKD', 'Denar'), ('TND', 'Tunisian Dinar'), ('MGA', 'Malagasy Ariary'), ('CHF', 'Swiss Franc'), ('SAR', 'Saudi Riyal'), ('JMD', 'Jamaican Dollar'), ('ZAR', 'Rand'), ('KMF', 'Comoro Franc'), ('VUV', 'Vatu'), ('SOS', 'Somali Shilling'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('TMM', 'Manat'), ('PLN', 'Zloty'), ('IQD', 'Iraqi Dinar'), ('SCR', 'Seychelles Rupee'), ('NZD', 'New Zealand Dollar'), ('KWD', 'Kuwaiti Dinar'), ('IRR', 'Iranian Rial'), ('BAM', 'Convertible Marks'), ('LBP', 'Lebanese Pound'), ('MRO', 'Ouguiya'), ('GTQ', 'Quetzal'), ('BND', 'Brunei Dollar'), ('SGD', 'Singapore Dollar'), ('KPW', 'North Korean Won'), ('CUC', 'Cuban convertible peso'), ('BHD', 'Bahraini Dinar'), ('MNT', 'Tugrik'), ('XYZ', 'Default currency.'), ('XDR', 'SDR'), ('XAF', 'CFA franc BEAC'), ('RSD', 'Serbian Dinar'), ('BBD', 'Barbados Dollar'), ('AWG', 'Aruban Guilder'), ('LAK', 'Kip'), ('RWF', 'Rwanda Franc'), ('XPD', 'Palladium'), ('KYD', 'Cayman Islands Dollar'), ('OMR', 'Rial Omani'), ('SRD', 'Surinam Dollar'), ('PEN', 'Nuevo Sol'), ('ILS', 'New Israeli Sheqel'), ('TOP', 'Paanga'), ('HRK', 'Croatian Kuna'), ('AZN', 'Azerbaijanian Manat'), ('UZS', 'Uzbekistan Sum'), ('MMK', 'Kyat'), ('FKP', 'Falkland Islands Pound'), ('BTN', 'Bhutanese ngultrum'), ('SEK', 'Swedish Krona'), ('GBP', 'Pound Sterling'), ('CVE', 'Cape Verde Escudo'), ('MXN', 'Mexican peso'), ('MAD', 'Moroccan Dirham'), ('CAD', 'Canadian Dollar'), ('ETB', 'Ethiopian Birr'), ('TVD', 'Tuvalu dollar'), ('LYD', 'Libyan Dinar'), ('GIP', 'Gibraltar Pound'), ('WST', 'Tala'), ('XPF', 'CFP Franc'), ('RON', 'New Leu'), ('TJS', 'Somoni'), ('ZMW', 'Zambian Kwacha'), ('IDR', 'Rupiah'), ('MVR', 'Rufiyaa'), ('YER', 'Yemeni Rial'), ('KRW', 'Won'), ('LRD', 'Liberian Dollar'), ('AUD', 'Australian Dollar'), ('PGK', 'Kina'), ('UAH', 'Hryvnia'), ('KGS', 'Som'), ('NAD', 'Namibian Dollar'), ('THB', 'Baht'), ('TTD', 'Trinidad and Tobago Dollar'), ('CRC', 'Costa Rican Colon'), ('JPY', 'Yen'), ('PKR', 'Pakistan Rupee'), ('UYU', 'Uruguayan peso'), ('BZD', 'Belize Dollar'), ('MDL', 'Moldovan Leu'), ('FJD', 'Fiji Dollar'), ('LSL', 'Lesotho loti'), ('AOA', 'Kwanza'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('HNL', 'Lempira'), ('ANG', 'Netherlands Antillian Guilder'), ('KZT', 'Tenge'), ('TWD', 'New Taiwan Dollar'), ('SBD', 'Solomon Islands Dollar'), ('GEL', 'Lari'), ('BWP', 'Pula'), ('PYG', 'Guarani'), ('CZK', 'Czech Koruna'), ('KES', 'Kenyan Shilling'), ('CUP', 'Cuban Peso'), ('INR', 'Indian Rupee'), ('CNY', 'Yuan Renminbi'), ('TRY', 'Turkish Lira'), ('BRL', 'Brazilian Real'), ('ZWD', 'Zimbabwe Dollar A/06'), ('AFN', 'Afghani'), ('NOK', 'Norwegian Krone'), ('COP', 'Colombian peso'), ('BGN', 'Bulgarian Lev'), ('CLP', 'Chilean peso'), ('JOD', 'Jordanian Dinar'), ('GNF', 'Guinea Franc'), ('NIO', 'Cordoba Oro'), ('IMP', 'Isle of Man pount'), ('GMD', 'Dalasi'), ('XAU', 'Gold'), ('BDT', 'Taka'), ('EGP', 'Egyptian Pound'), ('KHR', 'Riel'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('EUR', 'Euro'), ('ZWN', 'Zimbabwe dollar A/08'), ('AED', 'UAE Dirham'), ('SDG', 'Sudanese Pound'), ('MUR', 'Mauritius Rupee'), ('NPR', 'Nepalese Rupee'), ('USD', 'US Dollar'), ('STD', 'Dobra'), ('HUF', 'Forint'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('QAR', 'Qatari Rial'), ('LVL', 'Latvian Lats'), ('DOP', 'Dominican Peso'), ('MOP', 'Pataca'), ('SYP', 'Syrian Pound'), ('XOF', 'CFA Franc BCEAO'), ('XTS', 'Codes specifically reserved for testing purposes'), ('XAG', 'Silver'), ('XFO', 'Gold-Franc'), ('BYR', 'Belarussian Ruble'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('CDF', 'Congolese franc'), ('MZN', 'Metical'), ('DKK', 'Danish Krone'), ('DZD', 'Algerian Dinar'), ('GHS', 'Ghana Cedi'), ('ZWL', 'Zimbabwe dollar A/09'), ('UGX', 'Uganda Shilling'), ('SHP', 'Saint Helena Pound'), ('SZL', 'Lilangeni'), ('LKR', 'Sri Lanka Rupee'), ('BIF', 'Burundi Franc'), ('VND', 'Dong'), ('AMD', 'Armenian Dram'), ('ALL', 'Lek'), ('XCD', 'East Caribbean Dollar'), ('MYR', 'Malaysian Ringgit'), ('PHP', 'Philippine Peso')], default='USD', max_length=3, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], default='en', max_length=2, verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=30, verbose_name='Phone number'),
            preserve_default=False,
        ),
    ]