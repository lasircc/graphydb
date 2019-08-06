"""
The main class representing a GraphDB Repo
"""

import rdflib
from rdflib.util import guess_format

from .SPARQLHelper import SPARQLHelper

class GraphyDBRepo(object):


    def __init__(self, file=None, sparql_endpoint=None):
        
        self.sparql_endpoint = sparql_endpoint
        if file: # load from file just for debugging
            self.graph = rdflib.Graph()        
            self.graph.parse(file, format=guess_format(file))
        else:
            self.graph = rdflib.ConjunctiveGraph('SPARQLUpdateStore')
            self.graph.open(sparql_endpoint)
        
        self.SPARQLHelper = SPARQLHelper(self.graph)

    

    def __repr__(self):
        return f"<Pythonic GraphyDB Reposiotory (SPARQL endpoint = {self.sparql_endpoint})>"


    def build_all(self):

        print('building ontologies')
        self.build_ontologies()


    def build_ontologies(self):

        qres = self.SPARQLHelper.get_ontology()
        print (qres)


    def build_classes(self):

        qres = self.SPARQLHelper.get_classes()
        print (qres)