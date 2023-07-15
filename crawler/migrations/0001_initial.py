# Generated by Django 4.1 on 2023-07-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('domain', models.CharField(max_length=150)),
                ('url_musics', models.URLField(help_text='ادرس صفحه ای که موزیک ها در ان وجود دارند')),
                ('count_music_geted', models.PositiveBigIntegerField(default=0, help_text='تعداد اهنگ هایی ک از این سایت گرفته شده است')),
                ('count_pages', models.PositiveBigIntegerField(default=0, help_text='تعداد صفحه های اهنگ(Pages)')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_music_by', models.TextField(help_text='گرفتن موزیک ها بر اساس')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crawler.sitemodel')),
            ],
        ),
        migrations.CreateModel(
            name='MusicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_title_by', models.TextField(help_text='گرفتن عنوان موزیک بر اساس', null=True)),
                ('get_picture_by', models.TextField(help_text='گرفتن عکس موزیک بر اساس', null=True)),
                ('get_128_by', models.TextField(help_text='گرفتن موزیک با کیفیت 128 بر اساس', null=True)),
                ('get_320_by', models.TextField(help_text='گرفتن موزیک با کیفیت 320 بر اساس', null=True)),
                ('get_singer_by', models.TextField(help_text='گرفتن خواننده بر اساس', null=True)),
                ('get_category_by', models.TextField(help_text='گرفتن خواننده بر اساس', null=True)),
                ('musics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crawler.musicsmodel')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.sitemodel')),
            ],
        ),
    ]
