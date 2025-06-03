from django.urls import path #type: ignore

from UserServices.Controller import AuthController 


urlpatterns = [
    path('login/', AuthController.LoginView.as_view(), name='login'),
    path('signup/', AuthController.SignupView.as_view(), name='signup'),
    path('publicApi/', AuthController.PublicAPIView.as_view(), name='publicapi'),
    path('protectedApi/', AuthController.ProtectedAPIView.as_view(), name='protectedapi'),
]