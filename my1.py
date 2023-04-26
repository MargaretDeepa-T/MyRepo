from rdflib import Namespace, Graph
from rdflib.namespace import RDF, RDFS, OWL

# Define namespace and ontology file path
#onto_ns = Namespace("http://www.semanticweb.org/deepa/ontologies/ScrumFrameworkOntology")
#onto_file = "C://Users/Deepa/Desktop/research/ScrumFrameworkOntology.owl"

onto_ns = Namespace("http://www.semanticweb.org/deepa/ontologies/CodeTemplate")
onto_file = "C://Users/Deepa/Desktop/research/usecase1.owl"


# Load ontology file into graph
g = Graph()
g.parse(onto_file, format="xml")
#print(f"Loaded {len(g)} triples from {onto_file}")
#for s, p, o in g:
    #print(s, p, o)
#print(f"Number of triples in graph: {len(g)}")


# Define Python class for each ontology class
classes = {}
for cls_uri in g.subjects(RDF.type, OWL.Class):  
    class_name = cls_uri.split("#")[-1]
    class_methods = []
    class_vars = {}
    for prop_uri in g.predicate_objects(cls_uri):        
        if prop_uri[1] == RDF.type and prop_uri[2] == OWL.ObjectProperty:          
           method_name = prop_uri[0].split("#")[-1]
           class_methods.append(method_name)
        elif prop_uri[1] == RDF.type and prop_uri[2] == OWL.DatatypeProperty:
            class_vars = prop_uri.split("#")[-1]
            var_name = prop_uri[0].split("#")[-1]
            class_vars[var_name] = None
    # Define the class with methods and variables
    #classes[class_name] = type(class_name, (), {"methods": class_methods, "vars": class_vars})
    classes[class_name] = type(class_name, (), {"methods": class_methods, "vars": class_vars})
    my_obj = classes[class_name]()
    my_obj.methods = class_methods
    my_obj.vars = class_vars

# Example usage:
for class_name in classes.keys():
    my_obj = classes[class_name]()
    #print(my_obj)
    print(f"\nClass Name: {class_name}")
    print(f"Methods: {my_obj.methods}")
    print(f"Methods of class {class_name}: {my_obj.methods}")
    print(f"Variables of class {class_name}: {my_obj.vars}")
    
