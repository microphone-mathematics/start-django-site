from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginView),
    path('signup/', views.signupView),
    path(
        'signup/',
        include('authentication.confirmations.urls')
    ),
    # path(
    #     'signup/find-your-spot/',
    #     include('authentication.find_your_spot.urls')
    # ),
    # path(
    #     'signup/spot/<int:spot_id>/',
    #     views.signupView,
    #     {'user_type': 'spot'}
    # ),
    # path(
    #     'signup/user/',
    #     views.signupView,
    #     {
    #         'user_type': 'user',
    #         'spot_id': '0'
    #     }
    # ),
    path('logout/', views.logoutView)
]
