from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.main),
    path('items', views.show_all, name='main'),
    path('items_admin', views.show_admin_all, name='items_admin'),
    path('items/<int:item_id>', views.show_item, name='items'),
    path('update_item/<int:item_id>', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    re_path('login>', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    re_path('register>', views.SingUp.as_view(), name='register'),
]

handler404 = views.error_404
handler500 = views.error_500
