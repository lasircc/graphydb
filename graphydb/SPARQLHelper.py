from rdflib import Graph



class SPARQLHelper(object):


    def __init__(self, rdfgraph):  
        self.rdflib_graph = rdfgraph


    def _run_query(self, query):
        """
        A method to run queries against a SPARQL endpoint
        """
        qres = self.rdflib_graph.query(query)
        return list(qres)


    def get_ontology(self):
        query = """
                SELECT DISTINCT ?x
                WHERE {
                    ?x a owl:Ontology
                }
            """
        return self._run_query(query)


    def get_classes(self):

        query = """
            SELECT DISTINCT ?class ?directSuperClass ?classSTR
            WHERE {
            
                ?class a owl:Class
                optional { ?class sesame:directSubClassOf ?directSuperClass}
            
                # STR(?x) returns NULL if ?x is a blank node
                # This breaks the filter below if it is based on STR(?x)
                #
                # Workaround: we set 
                # - ?classSTR = STR(?class) if ?class is not blank
                # - ?classSTR = 'Blank' (dummy string) if ?class is a blank node
                # and we send STR(?classSTR) to the filter
                #
                BIND( IF( isBlank(?class),'Blank', str(?class) ) AS ?classSTR)
                
                # filter out all RDF/RDFS/OWL/XML stuff
                FILTER(
                    !STRSTARTS(STR(?classSTR), "http://www.w3.org/2002/07/owl")
                    && !STRSTARTS(STR(?classSTR), "http://www.w3.org/1999/02/22-rdf-syntax-ns")
                    && !STRSTARTS(STR(?classSTR), "http://www.w3.org/2000/01/rdf-schema")
                    && !STRSTARTS(STR(?classSTR), "http://www.w3.org/2001/XMLSchema")
                    && !STRSTARTS(STR(?classSTR), "http://www.w3.org/XML/1998/namespace")
                ) 
            
            }
        """

        return self._run_query(query)