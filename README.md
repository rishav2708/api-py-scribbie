api-py-scribbie
===============

Simple Api of Places and response in json along with caching


Here is the Api for scribbie places search.
A person can view users of scribbie who visited different places and their comments in the json format.

Url:http://localhost:8000/api/?place=patna

The output will be simple as:

{'status': 'ok', 'user0': {'name': 'Rishav', 'details': 'whhoijn\\r\\nkpjiojw&#039;krorejrej'}}

It's simply build on the concepts of graph.facebook.com on django and needs development on the security point of view

Need to assign oauth and session private keys in order to only view the friend

Some key features of the api:

1) Easy Parser of neo4j cypher to query and the RESTful Api


2) Converts objects to simple dictionaries and then json


3) Works on virtual memory concept



4) Provided with a one level database caching

You need to install neo4j graph database and mysql for this to proceed
and also you need to install py2neo source for implementing the graph database in dictionary and json format.

It's free and very complexity efficient! :)
