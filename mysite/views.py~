from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from py2neo import neo4j,cypher
from django.core.cache import cache
import json
g=neo4j.GraphDatabaseService()
def search_form(request):
	return render(request, 'search_form.php')
def search(request):
	if 'q' in request.GET:
		request.session['name']='Rishav'
		message='You searched for: %r '% request.GET['q']
		#print "Result in json form as follows: "
		var=str(request.GET['q'])
		s="MATCH (n)-[:KNOWS]-(m) WHERE n.name="+"'"+var+"'"+" AND m.name='Rishav' RETURN n;"
		s=cypher.execute(g,s)
		s=s[0]
		if len(s)==0:
			message=str(s)
		else:
			s=s[0]
			for i in s:
				message=str(i)
	else:
		message='You Submitted an empty form'
	return HttpResponse(message+request.session['name'])
def api_creation(url):
	b=str(url.GET['place'])
	if b in cache:
		return HttpResponse(json.dumps(cache.get(b)),content_type="application/json")
	else:
		s="MATCH (n:People)-[r:VISITS]->(m:Places) WHERE m.name='"+b+"' RETURN n,r"
		t=cypher.execute(g,s)[0]
		if len(t)==0:
			d={'status':'error handling the object'}
			return HttpResponse(json.dumps(d),content_type="application/json")
		else:
			d={}
			for i in range(len(t)):
				d['user'+str(i)]={}
				d['user'+str(i)]['name']=str(t[i][0]['name'])
				d['user'+str(i)]['details']=str(t[i][1]['details'])
			d['status']='ok'
			cache.set(b,str(d))
			return HttpResponse(json.dumps(cache.get(b)),content_type="application/json")
def updateCache(url):
		cache.clear()
		b=str(url.GET['u'])
		s="MATCH (n:People)-[r:VISITS]->(m:Places) WHERE m.name='"+b+"' RETURN n,r"
		t=cypher.execute(g,s)[0]
		if len(t)==0:
			d={'status':'error handling the object'}
			return HttpResponse(str(d))
		else:
			d={}
			for i in range(len(t)):
				d['user'+str(i)]={}
				d['user'+str(i)]['name']=str(t[i][0]['name'])
				d['user'+str(i)]['details']=str(t[i][1]['details'])
			d['status']='ok'
			cache.set(b,str(d))
		return HttpResponse(json.loads(cache.get(b)))


