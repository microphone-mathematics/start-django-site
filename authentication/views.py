from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# from index.novedades.models import Novedades
from django.contrib.auth import authenticate, login, logout
from authentication import forms as AuthForms
import after_response
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import User
from django.conf import settings
from django.utils.translation import gettext as _


def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthForms.LoginForm(data=request.POST)
            print(form.data)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password')
                )
                if user.is_active:
                    login(request, user)
                    if request.GET:
                        return redirect(request.GET['next'])
                    else:
                        return redirect('/')
                else:
                    # Return a 'disabled account' error message
                    error = 'Your user is disabled'
            else:
                print(form.non_field_errors)
                # return an 'invalid login' error message
                error = 'Invalid Login'
            return render(
                request,
                'authentication/login.html',
                {'error': error, 'form': form}
            )
        else:
            form = AuthForms.LoginForm()
            return render(
                request,
                'authentication/login.html',
                {
                    'title': 'Login',
                    'currentPage': 'Login',
                    'form': form
                }
            )
    else:
        return HttpResponseRedirect('/')


def logoutView(request):
    logout(request)
    return redirect('/')


def chooseUserType(request):
    return render(
        request,
        'authentication/choose_user_type.html',
        {
            'title': 'Crear usuario',
            'currentPage': 'Login'
        }
    )


# def signupView(request, user_type, spot_id):
#     return HttpResponse('signup')


def signupView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = AuthForms.UserRegistrationForm(request.POST)
        form.instance.is_active = False

        if form.is_valid():
            args = {
                'form': form,
                'title': 'Registrar Usuario',
                'currentPage': 'Login',
            }
            form.save()
            if form.instance.is_place_owner:
                args['signupDone'] = _(
                    'Listo! ' +
                    'Te acabamos de envíar un email ' +
                    'para confirmar tu dirección.\n' +
                    'Luego de confirmar tu dirección ' +
                    'puedes empezar a crear lugares.\n' +
                    'Gracias!'
                )

            else:
                args['signupDone'] = _(
                    'Listo! ' +
                    'Te acabamos de envíar un email' +
                    'para confirmar tu dirección.\n' +
                    'Gracias!'
                )

            # user_profileForm.save()
            sendEmailConfirmationMessage.after_response(form.instance)
            # sendSignupConfirmationMessage.after_response(
            #     form.instance, form.instance.is_place_owner
            # )

            return render(
                request,
                'authentication/signup.html',
                args
            )
        else:
            args = {}
            args['form'] = form
            args['error'] = form.errors

    else:
        args = {
            'title': 'Registrar Usuario',
            'currentPage': 'Login',
        }
        args['form'] = AuthForms.UserRegistrationForm()
    return render(
        request,
        'authentication/signup.html',
        args
    )


@after_response.enable
def sendSignupConfirmationMessage(signupForm, is_place_owner):
    if is_place_owner:
        salt = 'place_owner_confirmation'
        args = {}
        args['token'] = signing.dumps(signupForm.pk, salt=salt)
        args['first_name'] = signupForm.first_name
        args['last_name'] = signupForm.last_name
        args['email'] = signupForm.email
        email = signupForm.email
        email_from = 'Registros spotter <website@spotter.live>'
        email_to = 'info@spotter.live'
        html_message = render_to_string(
            'authentication/place_registration_confirmation_email.html',
            args
        )
        email_message = EmailMultiAlternatives(
            'Registro Web en cloudtables: ' +
            args['first_name'] + ' ' + args['last_name'],
            strip_tags(html_message),
            email_from,
            [email_to],
            reply_to=[email],
        )
        email_message.attach_alternative(html_message, "text/html")
    else:
        salt = 'K?bt==R&C=<U:HjVXTnjpM,3<z7z~pmCD'
        token = signing.dumps(signupForm.pk, salt=salt)
        print(token)
        args = {}
        args['contact_name'] = signupForm.first_name
        args['contact_lastname'] = signupForm.last_name
        args['email'] = signupForm.email
        args['token'] = token
        email = signupForm.email
        email_from = 'Registros spotter <website@spotter.live>'
        email_to = 'info@spotter.live'
        html_message = render_to_string(
            'authentication/registration_confirmation_email.html',
            args
        )
        email_message = EmailMultiAlternatives(
            'Registro Web de Spot: ' + args['spot'].name,
            strip_tags(html_message),
            email_from,
            [email_to],
            reply_to=[email]
        )
        email_message.attach_alternative(html_message, "text/html")
    email_message.send()


@after_response.enable
def sendEmailConfirmationMessage(form):
    print('sending email confirmation message...')
    salt = 'Afmeu9qo42KXs7jCufEB'
    token = signing.dumps(form.pk, salt=salt)
    name = form.first_name
    email = form.email
    email_from = 'Cloudtables <registrations@cloudtables.online>'
    email_to = name + ' <' + email + '>'
    html_message = _(
        'Hola ' + name + ', ' +
        'por favor ') + \
        '<a href="https://www.cloudtables.online' + \
        '/auth/signup/confirm-your-email/' + \
        token + '/">' + \
        _('confirmá tu email') + \
        '</a> ' + _('para completar el registro.') + '<br />\n\n' + \
        _(
            'Si no podés hacer click en el link, copiá el siguiente link' +
            ' y pegalo en la barra de URL de tu navegador') + \
        ':<br />\n\n' + \
        'https://www.cloudtables.online' + \
        '/auth/signup/confirm-your-email/' + \
        token + '/'
    email_message = EmailMultiAlternatives(
        _('Registro Web Cloudtables. Confirmá tu email.: '),
        strip_tags(html_message),
        email_from,
        [email_to],
        reply_to=[email]
    )
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()
