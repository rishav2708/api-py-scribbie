from django.shortcuts import render
from django.core.cache import cache
from py2neo import cypher,neo4j
import sys
g=neo4j.GraphDatabaseService()
b=sys.argv[1]
b=str(b)
if b not in cache:
	print "Cache rebuilt failed.. not in cache"
else:
	d={}
	s="MATCH (n:People)-[r:VISITS]->(m:Places) WHERE m.name='"+b+"' RETURN n,r"
	t=cypher.execute(g,s)[0]
	if len(t)==0:
		d={'status':'error handling the object'}
	else:
		for i in range(len(t)):
			d['user'+str(i)]={}
			d['user'+str(i)]['name']=str(t[i][0]['name'])
			d['user'+str(i)]['details']=str(t[i][1]['details'])
		d['status']='ok'
	cache.set(b,str(d))
