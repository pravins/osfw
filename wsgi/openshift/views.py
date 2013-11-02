import os
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.template import RequestContext

# from example openid
from django.conf import settings
from django.contrib.auth.decorators import login_required
from social.backends.google import GooglePlusAuth

# Functions associated with openid
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
    }, RequestContext(request))

def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))

@login_required
def done(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('done.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))

def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))

def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))





def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c, context_instance=RequestContext(request))
#	return render_to_response ('index.html', context_instance=RequestContext(request))

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	print "username", username
	print "password", password

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username}, context_instance=RequestContext(request))

def invalid_login(request):
	return render_to_response('invalid_login.html', context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html', context_instance=RequestContext(request))

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args, context_instance=RequestContext(request))

def register_success(request):
	return render_to_response('register_success.html', context_instance=RequestContext(request))
