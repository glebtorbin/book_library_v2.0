from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('books.urls', namespace='books')),
    path('admin/', admin.site.urls),
    # path('auth/', include('users.urls', namespace='users')),
    # path('auth/', include('django.contrib.auth.urls')),
]