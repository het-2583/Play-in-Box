from django.urls import path
from.import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    
     path('',views.home,name='home'),

     path('login/', views.login_view, name='login_view'),
     path('register/', views.registration, name='register'),


    path('',views.home,name="home_page"),

    path('organizer_dashboard',views.organizer_dashboard,name="organizer_dashboard"),

    path('owner_dashboard',views.owner_dashboard,name="owner_dashboard"),
    
     path('logout/', auth_views.LogoutView.as_view(template_name='homepage.html'),name='logout'),
    
    path('viewCategory/',views.viewCategory,name="viewCategory"),
     
    path('view_grounds/',views.view_ground,name="view_ground"), 

    path('addCategory/',views.addCategory,name="addCategory"),
   
    path('deleteCategory/<id>',views.deleteCategory,name="deleteCategory"),
    path('updateCategory/<id>',views.updateCategory,name="updateCategory"),
    path('bulkUpload/',views. bulk_upload,name='bulkUpload'),
    path('upload_csv',views.upload_csv,name='upload_csv'),
    path('download_csv',views.download_csv,name="download_csv"),
    path('add_ground/<int:user_id>', views.add_ground, name='add_ground'),
    path('book_ground/<int:user_id>/<int:gid>', views.book_ground, name='book_ground'),
    path('ground_details/<id>', views.ground_details, name='ground_details'),
    path('profile/',views.profile,name="profile"),
    path('home/',views.home,name="home"),
    path('add_tournament/<int:user_id>', views.add_tournament, name='add_tournament'),
    path('add_team/', views.add_team, name='add_team'),
]
    