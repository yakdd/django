from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('upload_image/<int:recipe_id>', views.upload_image, name='upload_image'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('about_user/', views.AboutUser.as_view(), name='about_user'),
    path('login/',
         LoginView.as_view(
             template_name='recipeapp/login.html',
             redirect_authenticated_user=True,
         ),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
