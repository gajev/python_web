from django.shortcuts import render, redirect

from project_cars.cars.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm
from project_cars.cars.models import Profile, Car


# Create your views here.
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None

def sum_cars():
    cars_sum = 0
    for car in Car.objects.all():
        cars_sum += car.price
    return cars_sum


def index(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'index_no_profile.html')
    return render(request, 'index_profile.html')


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context,)


def catalogue(request):
    context = {
        "cars": Car.objects.all(),
        "number": Car.objects.count()
    }
    return render(request, 'catalogue.html', context,)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context, )


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context,)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context,)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context, )


def details_profile(request):
    cars_sum = sum_cars
    profile = get_profile()

    context = {
        'profile': profile,
        'cars_sum': cars_sum
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context, )


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        return render(request, 'profile/profile-delete.html')
    else:
        Car.objects.all().delete()
        profile.delete()
        return render(request, 'index_no_profile.html')
