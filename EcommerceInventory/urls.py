
from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore

from UserServices.Controller.DynamicFormController import DynamicFormController       # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('UserServices.urls')),  # User management
    path('api/getForm/<str:modelName>/', DynamicFormController.as_view(), name='dynamicForm' ),  # User management
]
