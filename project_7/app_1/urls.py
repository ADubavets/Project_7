from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('items', views.show_all, name='main'),
    path('items_admin', views.show_admin_all, name='admin'),
    path('items/<int:item_id>', views.show_item, name='items'),
    path('update_item/<int:item_id>', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
]

handler404 = views.error_404
handler500 = views.error_500
