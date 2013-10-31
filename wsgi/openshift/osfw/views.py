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
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

# Create your views here.



def redirect_to_index(request):
    return HttpResponseRedirect("/index/")

def index(request):
	return render_to_response ('index.html', context_instance=RequestContext(request))

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
	osfws = Osfw.objects.all().distinct().order_by('familyname')
#	osfws = Osfw.objects.all().values_list('familyname', flat=True).distinct()
#	osfws = Osfw.objects.all().order_by('familyname').values_list('familyname', flat=True).distinct()

	paginator = Paginator(osfws, 10)
	page = request.GET.get('page')

	try:
	    allfonts = paginator.page(page)
	except PageNotAnInteger:
    # If page is not an integer, deliver first page.
	    allfonts = paginator.page(1)
	except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
	    allfonts = paginator.page(paginator.num_pages)
	return render_to_response ('allfonts.html', {'osfws': allfonts}, context_instance=RequestContext(request))


def fontinfo(request, osfw_id=1):
	osfwobject = Osfw.objects.get(id=osfw_id)
	osfws = Osfw.objects.filter(familyname=osfwobject.familyname).exclude(id=osfw_id)
	langlist = osfwobject.langsupport.split(' ')
	scriptlist = osfwobject.scriptsupport.replace(","," ").replace("  "," ")
	scriptlist = scriptlist.split(' ')
	return render_to_response("fontinfo.html", {"osfw": osfwobject, "langlist" : langlist, "allosfws": osfws, "scriptlist": scriptlist}, context_instance=RequestContext(request) )

def searchlang(request, langstring="en"):
	mystring = " " + langstring + " "
        osfws = Osfw.objects.filter(langsupport__icontains=mystring)

        paginator = Paginator(osfws, 10)
        page = request.GET.get('page')

        try:
            allfonts = paginator.page(page)
        except PageNotAnInteger:
    # If page is not an integer, deliver first page.
            allfonts = paginator.page(1)
        except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
            allfonts = paginator.page(paginator.num_pages)

	return render_to_response("fontsperlang.html", {"osfws": allfonts, "langname" : langstring}, context_instance=RequestContext(request) )


def searchlicense(request, licensestring="GPL"):
#        mystring = licensestring
        osfws = Osfw.objects.filter(license__icontains=licensestring)

        paginator = Paginator(osfws, 10)
        page = request.GET.get('page')

        try:
            allfonts = paginator.page(page)
        except PageNotAnInteger:
    # If page is not an integer, deliver first page.
            allfonts = paginator.page(1)
        except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
            allfonts = paginator.page(paginator.num_pages)

        return render_to_response("fontsperlang.html", {"osfws": allfonts, "langname" : licensestring}, context_instance=RequestContext(request) )



def searchscript(request, scriptstring="en"):
        mystring = scriptstring[:-1]
        osfws = Osfw.objects.filter(scriptsupport__icontains=mystring)

        paginator = Paginator(osfws, 10)
        page = request.GET.get('page')

        try:
            allfonts = paginator.page(page)
        except PageNotAnInteger:
    # If page is not an integer, deliver first page.
            allfonts = paginator.page(1)
        except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
            allfonts = paginator.page(paginator.num_pages)

        return render_to_response("fontsperlang.html", {"osfws": allfonts, "langname" : scriptstring}, context_instance=RequestContext(request) )

def likefont(request, osfw_id):
	if osfw_id:
		q = Osfw.objects.get(id=osfw_id)
		count = q.likes
		count = count + 1
		q.likes = count
		q.save()
	return HttpResponseRedirect('/get/%s' % osfw_id)

def search_fonts(request):
    return render_to_response('searchfonts.html', request, context_instance=RequestContext(request))

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        stype = request.GET['stype']
	if not q:
		error = True
	else:
		querystr = q.replace(" ", "")
		if stype == "lang":
			q = " " + q + " "
			osfws = Osfw.objects.filter(langsupport__icontains=q)
		elif stype == "script":
			osfws = Osfw.objects.filter(scriptsupport__icontains=q)
		else:
			osfws = Osfw.objects.filter(familyname__istartswith=q)


		paginator = Paginator(osfws, 10)
                page = request.GET.get('page')
	        try:
        	    allfonts = paginator.page(page)
	        except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
        	    allfonts = paginator.page(1)
	        except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
        	    allfonts = paginator.page(paginator.num_pages)


 	        return render(request, 'search_results.html',{'osfws': allfonts, 'query': querystr, 'stype':stype}, context_instance=RequestContext(request))

    return render(request, 'searchfonts.html',{'error': error}, context_instance=RequestContext(request))
