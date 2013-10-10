from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from osfw.models import Osfw
from django.core.context_processors import csrf
from django.shortcuts import render

# Create your views here.


def redirect_to_index(request):
    return HttpResponseRedirect("/index/")

def index(request):
    return render_to_response('home.html')

#	t = get_template('index.html')
#	html = t.render(Context())
#	return HttpResponse(html)

def test(request):
	t = get_template('test.html')
	html = t.render(Context())
	return HttpResponse(html)


def standards(request):
	t = get_template('standards.html')
	html = t.render(Context())
	return HttpResponse(html)

def about(request):
	t = get_template('about.html')
	html = t.render(Context())
	return HttpResponse(html)

def peoples(request):
	t = get_template('peoples.html')
	html = t.render(Context())
	return HttpResponse(html)

def contact(request):
	t = get_template('contact.html')
	html = t.render(Context())
	return HttpResponse(html)

def allfonts(request):
	return render_to_response ('allfonts.html',  
							{'osfws': Osfw.objects.all() })


def fontinfo(request, osfw_id=1):
	return render_to_response("fontinfo.html",
							{"osfw": Osfw.objects.get(id=osfw_id  )} )
def likefont(request, osfw_id):
	if osfw_id:
		q = Osfw.objects.get(id=osfw_id)
		count = q.likes
		count = count + 1
		q.likes = count
		q.save()
	return HttpResponseRedirect('/get/%s' % osfw_id)

def search_fonts(request):
    return render(request, 'searchfonts.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        stype = request.GET['stype']
	if not q:
		error = True
	else:
		if stype == "lang":
			osfws = Osfw.objects.filter(langsupport__icontains=q)
		else:
			osfws = Osfw.objects.filter(scriptsupport__icontains=q)
 	        return render(request, 'search_results.html',{'osfws': osfws, 'query': q})

    return render(request, 'searchfonts.html',{'error': error})
