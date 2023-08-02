from django.urls import path, include

from project_cars.cars.views import catalogue, create_car, edit_car, delete_car, details_car, index, \
    edit_profile, create_profile, details_profile, delete_profile


urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('edit/', edit_profile, name='edit profile')])),

    path('car/', include([
        path('create/', create_car, name='create car'),
        path('details/<int:pk>/', details_car, name='details car'),
        path('delete//<int:pk>/', delete_car, name='delete car'),
        path('edit/<int:pk>/', edit_car, name='edit car'),
    ])),
)