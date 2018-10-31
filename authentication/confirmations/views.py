from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import login
import after_response
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from authentication.models import User
from django.conf import settings
from django.utils.translation import gettext as _


# def spotOwnershipConfirmation(request, spot_id, token):
#     spot = get_object_or_404(Spot, pk=spot_id)
#     salt = 'K?bt==R&C=<U:HjVXTnjpM,3<z7z~pmCD'

#     try:
#         pk = signing.loads(
#             token,
#             salt=salt
#         )

#     except signing.BadSignature:
#         return self.invalid()

#     inscripcion = get_object_or_404(User, pk=pk)
#     userProfile = Profile.objects.get(user=inscripcion)
#     userProfile.ownership_confirmed = True
#     spot.been_claimed = True
#     if inscripcion.email_confirmed is True:
#         inscripcion.is_active = True
#     inscripcion.save()
#     spot.save()
#     userProfile.save()
#     sendOwnershipConfirmationOk.after_response(inscripcion, userProfile)
#     return redirect('/auth/signup/done/spot-ownership-confirmation/')


# @after_response.enable
# def sendOwnershipConfirmationOk(inscripcion, userProfile):
#     send_mail(
#         'Propiedad de spot confirmada en spotter.live!',
#         inscripcion.first_name +
#         ',\nYa quedaste confirmado como dueño de ' +
#         userProfile.spot.name + ' en spotter.live' +
#         '!\n\nGracias y buenos spotteos!\n\nspotter\n' +
#         'Email: info@spotter.live\n' +
#         'Instagram: https://instagram.com/spotterlive/\n' +
#         'Facebook: https://facebook.com/spotterlive/',
#         'Spotter Live <' + settings.DEFAULT_FROM_EMAIL + '>',
#         [
#             inscripcion.first_name + ' ' + inscripcion.last_name +
#             ' <' + inscripcion.email + '>'
#         ]
#     )


# def emailConfirmation(request, token):
#     salt = 'Afmeu9qo42KXs7jCufEB'

#     try:
#         pk = signing.loads(
#             token,
#             salt=salt
#         )

#     except signing.BadSignature:
#         return self.invalid()

#     inscripcion = get_object_or_404(User, pk=pk)
#     userProfile = Profile.objects.get(user=inscripcion)
#     inscripcion.email_confirmed = True
#     if userProfile.ownership_confirmed is True:
#         inscripcion.is_active = True
#     inscripcion.save()
#     if inscripcion.is_active:
#         login(request, inscripcion)
#     sendEmailConfirmationOk.after_response(inscripcion)
#     return redirect('/auth/signup/done/email-confirmation/')


# @after_response.enable
# def sendEmailConfirmationOk(inscripcion):
#     send_mail(
#         'Email confirmado en spotter.live!',
#         inscripcion.first_name +
#         ',\nTu email ya quedó confirmado en spotter.live' +
#         '!\n\nGracias y buenos spotteos!\n\nspotter\n' +
#         'Email: info@spotter.live\n' +
#         'Instagram: https://instagram.com/spotterlive/\n' +
#         'Facebook: https://facebook.com/spotterlive/',
#         'Spotter Live <' + settings.DEFAULT_FROM_EMAIL + '>',
#         [
#             inscripcion.first_name + ' ' + inscripcion.last_name +
#             ' <' + inscripcion.email + '>'
#         ]
#     )


# def emailConfirmationOk(request):
#     return render(
#         request,
#         'authentication/confirmations/email_confirmation_done.html'
#     )


# def spotOwnershipConfirmationOk(request):
#     return render(
#         request,
#         'authentication/confirmations/ownership_confirmation_done.html'
#     )


def emailConfirmation(request, token):
    salt = "Afmeu9qo42KXs7jCufEB"
    try:
        pk = signing.loads(
            token,
            salt=salt
        )

    except signing.BadSignature:
        return self.invalid()

    inscripcion = get_object_or_404(User, pk=pk)
    inscripcion.email_confirmed = True
    inscripcion.is_active = True
    inscripcion.save()
    login(request, inscripcion)
    sendEmailConfirmationOk.after_response(inscripcion)
    return redirect('/auth/signup/done/email-confirmation/')


@after_response.enable
def sendEmailConfirmationOk(inscripcion):
    send_mail(
        _('Email confirmado en Cloudtables!'),
        inscripcion.first_name +
        _(',\nTu email ya quedó confirmado en Cloudtables.') +
        _('!\n\nGracias!\n') +
        'Email: info@cloudtables.app\n' +
        'Instagram: https://instagram.com/cloudtables/\n' +
        'Facebook: https://facebook.com/cloudtabless.app/',
        'Cloudtables App <' + settings.DEFAULT_FROM_EMAIL + '>',
        [
            inscripcion.first_name + ' ' + inscripcion.last_name +
            ' <' + inscripcion.email + '>'
        ]
    )


def emailConfirmationOk(request):
    args = {}
    return render(
        request,
        'authentication/email_confirmation_done.html',
        args
    )
