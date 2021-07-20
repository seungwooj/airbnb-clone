from django.urls import path
from rooms import views as room_views

app_name = "core"
# URLs starts with /
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
