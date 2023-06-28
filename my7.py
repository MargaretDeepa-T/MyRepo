from owlready2 import get_ontology

# Load the ontology
onto = get_ontology("C://Users/Deepa/Desktop/research/usecase1.owl").load()

# Define a template for the code
template = "class {0}:\n\tdef __init__(self):\n"

# Iterate over all classes
for cls in onto.classes():

    # Get the class name
    class_name = cls.name

    # Get the object properties of the class
    object_properties = [prop for prop in cls.get_properties() if prop.type == onto.ObjectProperty]

    # Get the data properties of the class
    data_properties = [prop for prop in cls.get_properties() if prop.type == onto.DataProperty]

    # Print the class name, object properties, and data properties
    print(f"Class: {cls.iri}")
    print("Object Properties: ")
    for prop in object_properties:
        print(f"\t{prop.name}")
    print("Data Properties: ")
    for prop in data_properties:
        print(f"\t{prop.name}")

    # Print the code template for the class
    print(f"\nCode template for {class_name}:")
    print(template.format(class_name))
