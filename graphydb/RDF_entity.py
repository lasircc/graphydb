


class RDF_Entity(object):
    """
    Pythonic representation of an RDF entity - normally not instantiated but used for
    inheritance purposes
    """

    def __init__(self, uri, isBnode=False):
        self.uri = uri
        self.slug = slug
        self.isBnode = isBnode


class GraphDBClass(RDF_Entity):
    pass

class GraphDBProperty(RDF_Entity):
    pass

class GraphDBIndividual(RDF_Entity):
    pass