from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from osfw.models import Osfw
from django.core.context_processors import csrf
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


# Create your views here.


def redirect_to_index(request):
    return HttpResponseRedirect("/index/")
	

def index(request):
    return render_to_response ('index.html', context_instance=RequestContext(request))

#	t = get_template('index.html')
#	html = t.render(Context())
#	return HttpResponse(html)

def test(request):
    return render_to_response ('test.html', context_instance=RequestContext(request))

def standards(request):
    return render_to_response ('standards.html', context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def about(request):
    return render_to_response ('about.html', context_instance=RequestContext(request))

def peoples(request):
    return render_to_response ('peoples.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response ('contact.html', context_instance=RequestContext(request))

def allfonts(request):
	return render_to_response ('allfonts.html', {'osfws': Osfw.objects.all() }, context_instance=RequestContext(request))


def fontinfo(request, osfw_id=1):
        osfwobject = Osfw.objects.get(id=osfw_id)
        langlist = osfwobject.langsupport.split(',')
	return render_to_response("fontinfo.html", {"osfw": Osfw.objects.get(id=osfw_id), "langlist" : langlist}, context_instance=RequestContext(request) )

def likefont(request, osfw_id):
	if osfw_id:
		q = Osfw.objects.get(id=osfw_id)
		count = q.likes
		count = count + 1
		q.likes = count
		q.save()
	return HttpResponseRedirect('/get/%s' % osfw_id)

def search_fonts(request):
    return render(request, 'searchfonts.html', context_instance=RequestContext(request))

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
 	        return render(request, 'searchresults.html',{'osfws': osfws, 'query': q}, context_instance=RequestContext(request))

    return render(request, 'searchfonts.html',{'error': error}, context_instance=RequestContext(request))

def searchlang(request, langstring="en"):
        osfws = Osfw.objects.filter(langsupport__icontains=langstring)
# todo handle if osfws=Null
        return render_to_response("fontsperlang.html", {"osfws": osfws, "langname" : langstring}, context_instance=RequestContext(request) )
