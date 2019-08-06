from rdflib import Graph



class SPARQLHelper(object):


    def __init__(self, rdfgraph):  
        self.rdflib_graph = rdfgraph


    def get_ontology(self):
        qres = self.rdflib_graph.query("""
                SELECT DISTINCT ?x
                WHERE {
                    ?x a owl:Ontology
                }
            """)
        return list(qres)


    def get_classes(self):

        print("""
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT DISTINCT ?x ?c
                WHERE {
                    {
                        { ?x a owl:Class }
                        union
                        { ?x a rdfs:Class }
                        union
                        { ?x rdfs:subClassOf ?y }
                        union
                        { ?z rdfs:subClassOf ?x }
                        union
                        { ?y rdfs:domain ?x }
                        union
                        { ?y rdfs:range ?x }

                        union
                        { ?y rdf:type ?x }

                    } .
                    OPTIONAL { ?x a ?c } 
                    # get the type too if available

                    FILTER(
                        !STRSTARTS(STR(?x), "http://www.w3.org/2002/07/owl")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/1999/02/22-rdf-syntax-ns")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/2000/01/rdf-schema")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/2001/XMLSchema")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/XML/1998/namespace")
                        && (!isBlank(?x))
                    ) .

                }
            """)

        qres = self.rdflib_graph.query("""
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT DISTINCT ?x ?c
                WHERE {
                    {
                        { ?x a owl:Class }
                        union
                        { ?x a rdfs:Class }
                        union
                        { ?x rdfs:subClassOf ?y }
                        union
                        { ?z rdfs:subClassOf ?x }
                        union
                        { ?y rdfs:domain ?x }
                        union
                        { ?y rdfs:range ?x }

                        union
                        { ?y rdf:type ?x }

                    } .
                    OPTIONAL { ?x a ?c } 
                    # get the type too if available

                    FILTER(
                        !STRSTARTS(STR(?x), "http://www.w3.org/2002/07/owl")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/1999/02/22-rdf-syntax-ns")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/2000/01/rdf-schema")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/2001/XMLSchema")
                        && !STRSTARTS(STR(?x), "http://www.w3.org/XML/1998/namespace")
                        && (!isBlank(?x))
                    ) .

                }""")

        
        return list(qres)
