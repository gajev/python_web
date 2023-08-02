from django.urls import path, include
from exam_preparation.web.views import index, details_album, add_album, edit_album, delete_album, \
    details_profile, delete_profile, add_profile

urlpatterns = (
    path('', index, name='index'),
    path('albums/', include([
        path('details/<int:pk>/', details_album, name='details albums'),
        path('add/', add_album, name='add albums'),
        path('edit/<int:pk>/', edit_album, name='edit albums'),
        path('delete/<int:pk>/', delete_album, name='delete albums')
    ])),
    path('profile/', include([
        path('add_profile/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
)
