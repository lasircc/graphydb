NAMESPACES = {
    'las'   : 'http://las.ircc.it/las-ontology#',
    'owl'   : 'http://www.w3.org/2002/07/owl#',
    'rdfs'  : 'http://www.w3.org/2000/01/rdf-schema#',
    'rdf'   : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
}

def get_namespace(uri):
    for k,v in NAMESPACES.items():
        # Prints the string by replacing geeks by Geeks
        if v in uri:
            return uri.replace(v,k+':')


