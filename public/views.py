from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from crawler.models import SiteModel, AddMusics
from crawler.tasks import add_musics_task


def _get_add_obj():
    add_obj = AddMusics.objects.filter(is_active=True).first()
    return add_obj


def home(request):
    site_models = SiteModel.objects.filter(is_active=True, categorymodel__is_active=True)
    add_obj = _get_add_obj()
    add_obj_sites_id = []
    if add_obj:
        add_obj_sites_id = list(add_obj.sites.values_list('id', flat=True))
    context = {
        'site_models': site_models,
        'add_obj': add_obj,
        'add_obj_sites_id': add_obj_sites_id,
    }
    return render(request, 'public/index.html', context)


def start_crawl(request):
    models_id = request.GET.getlist('models_selected')
    site_models = SiteModel.objects.filter(id__in=models_id, is_active=True, categorymodel__is_active=True)
    add_obj = _get_add_obj()
    if add_obj:
        return HttpResponseRedirect(reverse('public:home') + '?error=یک عملیات اضافه کردن فعال وجود دارد')
    if not site_models:
        return HttpResponseRedirect(reverse('public:home') + '?error=مدلی برای بررسی یافت نشد')

    add_obj = AddMusics.objects.create()
    add_obj.sites.set(site_models)
    # add_musics_task.delay(add_obj.id)

    add_musics_task(add_obj.id)
    return redirect('public:home')


def pause_crawl(request):
    add_obj = _get_add_obj()
    if add_obj is None:
        return HttpResponseRedirect(reverse('public:home') + '?error=عملیات اضافه کردن فعالی یافت نشد')
    add_obj.delete_task()
    add_obj.is_running = False
    add_obj.save()
    return redirect('public:home')


def continue_crawl(request):
    add_obj = _get_add_obj()
    if add_obj is None:
        return HttpResponseRedirect(reverse('public:home') + '?error=عملیات اضافه کردن فعالی یافت نشد')
    add_obj.is_running = True
    add_obj.save()
    # add_musics_task.delay(add_obj.id)

    add_musics_task(add_obj.id, is_continue=True)
    return redirect('public:home')


def delete_crawl(request):
    add_obj = _get_add_obj()
    if add_obj is None:
        return HttpResponseRedirect(reverse('public:home') + '?error=عملیات اضافه کردن فعالی یافت نشد')
    add_obj.delete()
    return redirect('public:home')


def test(request):
    return redirect('public:home')
