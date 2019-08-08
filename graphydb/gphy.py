"""
The main class representing a GraphDB Repo
"""

from .SPARQLHelper import SPARQLHelper

class GraphyDBRepo(object):


    def __init__(self, sparql_endpoint=None):
        
        self.sparql_endpoint = SPARQLHelper(sparql_endpoint)
        
    

    def __repr__(self):
        return f"<Pythonic GraphyDB Reposiotory (SPARQL endpoint = {self.sparql_endpoint})>"



    def build_all(self):

        print('building ontologies')
        self.build_ontologies()


    def build_ontologies(self):

        qres = self.sparql_endpoint.get_ontology()
        print (qres)


    def build_classes(self):

        qres = self.sparql_endpoint.get_classes()
        print (qres)
        return qres