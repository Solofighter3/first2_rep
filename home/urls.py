
from django.urls import path
from home import views
urlpatterns = [
    path('',views.Login,name="Login"),
    path('index',views.index,name="index"),
    path('contacts/',views.contacts,name="contacts"),
    path('signup/',views.signup,name="signup"),
    path('Logout',views.Logout,name="Logout"),
   
]
