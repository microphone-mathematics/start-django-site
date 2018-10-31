from django.urls import path
from . import views

urlpatterns = [
    # path(
    #     'confirm-spot/<int:spot_id>/<str:token>/',
    #     views.spotOwnershipConfirmation
    # ),
    path(
        'confirm-your-email/<str:token>/',
        views.emailConfirmation
    ),
    path(
        'done/email-confirmation/',
        views.emailConfirmationOk
    ),
    # path(
    #     'done/spot-ownership-confirmation/',
    #     views.spotOwnershipConfirmationOk
    # )
]
