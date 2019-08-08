# from parent dir run: ipython test/dummy_test.py 

import graphydb

# import os
# script_dir = os.path.dirname(__file__)
# file = os.path.join(script_dir, 'model.ttl')
# print(file)

g = graphydb.GraphyDBRepo(sparql_endpoint='http://localhost:7200/repositories/las_ontology')
g.build_classes()  
