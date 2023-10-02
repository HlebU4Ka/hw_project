from django.contrib import admin
from django.urls import path, include
from myproject.users import urls as users_urls
from myproject.courses import urls as courses_urls
from myproject.lessons import urls as lessons_urls

urlpatterns =[
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('lessons.urls')),
]