# modified code from rdflib-starter.py from: https://github.com/kastle-lab/kastle-drawbridge/blob/master/resources/rdflib-starter.py
# rdflib documentation: https://rdflib.readthedocs.io/en/stable/

from data_parser import *

##### Graph stuff
import rdflib
from rdflib import URIRef, Graph, Namespace, Literal
from rdflib import OWL, RDF, RDFS, XSD, TIME
# Prefixes
name_space = "https://kastle-lab.org/"
pfs = {
"kl-res": Namespace(f"{name_space}lod/resource/"),
"kl-ont": Namespace(f"{name_space}lod/ontology/"),
"geo": Namespace("http://www.opengis.net/ont/geosparql#"),
"geof": Namespace("http://www.opengis.net/def/function/geosparql/"),
"sf": Namespace("http://www.opengis.net/ont/sf#"),
"wd": Namespace("http://www.wikidata.org/entity/"),
"wdt": Namespace("http://www.wikidata.org/prop/direct/"),
"dbo": Namespace("http://dbpedia.org/ontology/"),
"time": Namespace("http://www.w3.org/2006/time#"),
"ssn": Namespace("http://www.w3.org/ns/ssn/"),
"sosa": Namespace("http://www.w3.org/ns/sosa/"),
"cdt": Namespace("http://w3id.org/lindt/custom_datatypes#"),
"ex": Namespace("https://example.com/"),
"rdf": RDF,
"rdfs": RDFS,
"xsd": XSD,
"owl": OWL,
"time": TIME
}
# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]

# Initialize an empty graph
graph = init_kg()

# Initialize from a file
# filename = "path/to/file"
# with open(filename, "w") as f:
#     graph.parse(f)
ontology = "ontology/symbol-ontology.ttl"
with open(ontology, "r") as f:
    graph.parse(f)

parameter_file = "ghidra-scripting/parameter-output.txt"
parameters = parse_parameters(parameter_file)
local_file = "ghidra-scripting/local-variable-output.txt"
local_vars = parse_local(local_file)
function_file = "ghidra-scripting/function-output.txt"
functions = parse_functions(function_file)
label_file = "ghidra-scripting/label-output.txt"
labels = parse_labels(label_file)
class_file = "ghidra-scripting/class-output.txt"
classes = parse_classes(class_file)
dll_file = "ghidra-scripting/dll-output.txt"
dlls = parse_dlls(dll_file)
namespace_file = "ghidra-scripting/namespace-output.txt"
namespaces = parse_namespaces(namespace_file)
instruction_file = "ghidra-scripting/instruction-output.txt"
instructions = parse_instructions(instruction_file)

# local variable format:
# {'var': 'local_8', 'datatype': 'undefined4', 'parent': 'FUN_00401090'}
# for local in local_vars:
#     print("Variable: ", local)
#     graph.add( (pfs(["ex"][local["var"]], definedIn, pfs["ex"][local["parent"]])))

for prefix, namespace in graph.namespaces():
    print(f"{prefix}: {namespace}")

kastle_members = ["Cogan", "Andrea", "Brandon"]
for x in kastle_members:
    # Add a specific triple
	# g.add( (subject_node, predicate_node, object_node) )
	graph.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )

output_file = "output.ttl"
temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)