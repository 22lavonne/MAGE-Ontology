# modified code from rdflib-starter.py from: https://github.com/kastle-lab/kastle-drawbridge/blob/master/resources/rdflib-starter.py
# rdflib documentation: https://rdflib.readthedocs.io/en/stable/

from data_parser import *

from urllib.parse import quote

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
"mkg": Namespace("https://mkg.com/data#"),
"ont": Namespace("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology"),
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
# definedIn = pfs["ont"]["definedIn"]
# hasDataType = pfs["ont"]["hasDataType"]
ONT = Namespace("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/")
print(ONT.symbol)

# Object Properties
definedIn = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/definedIn")
calls = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/calls")
hasParameter = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasParameter")
hasReturnType = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasReturnType")
passesInto = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/passesInto")
returns = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/returns")
containsInstruction = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/containsInstruction")
hasDataType = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasDataType")
hasAddress = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasAddress")
hasSourceAddress = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasSourceAddress")
hasDestinationAddress = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasDestinationAddress")
hasReference = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasReference")
hasPrimaryReference = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasPrimaryReference")
hasOpcode = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasOpcode")
hasSourceOperand = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasSourceOperand")
hasDestinationOperand = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasDestinationOperand")
performsRole = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/performsRole")

# Data Properties
addressOf = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/addressOf")
hasName = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasName")
hasOperandIndex = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasOperandIndex")
hasReferenceType = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasReferenceType")
hasType = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/addressOf")

# Classes
symbol = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Symbol")
label = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Label")
namespace_symbol = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/NamespaceSymbol")
namespace = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Namespace")
class_ = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Class")
dll = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/DLL")
function = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Function")
variable = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Variable")
local_variable = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/LocalVariable")
parameter = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Parameter")
data_type = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/DataType")
address = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Address")
reference = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Reference")
instruction = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Instruction")
immediate_operand = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/ImmediateOperand")
register = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Register")
opcode = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Opcode")
operand = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Operand")


# Initialize an empty graph
graph = init_kg()

ontology = "ontology/symbol-ontology.ttl"
with open(ontology, "r") as f:
    graph.parse(f)

# for individual_class in set(graph.subjects(RDF.type, RDFS.Class)) | set(graph.subjects(RDF.type, OWL.Class)):
#     print(individual_class)

# Data files, and lists of dictionaries containing the data
parameter_file = "ghidra-scripting/parameter-output.txt"
parameters_list = parse_parameters(parameter_file)
local_file = "ghidra-scripting/local-variable-output.txt"
local_var_list = parse_local(local_file)
function_file = "ghidra-scripting/function-output.txt"
function_list = parse_functions(function_file)
label_file = "ghidra-scripting/label-output.txt"
label_list = parse_labels(label_file)
class_file = "ghidra-scripting/class-output.txt"
class_list = parse_classes(class_file)
dll_file = "ghidra-scripting/dll-output.txt"
dll_list = parse_dlls(dll_file)
namespace_file = "ghidra-scripting/namespace-output.txt"
namespace_list = parse_namespaces(namespace_file)
instruction_file = "ghidra-scripting/instruction-output.txt"
instruction_list = parse_instructions(instruction_file)

# this seems to work to get all the local variables into the triples
# TODO: make sure the output for this is actually correct, although idk how to even check that
# Is it supposed to be a subclass relation thing? I currently have the relations defined above in this file and that's probably incorrect
# check if this correctly makes local variables a subclass of variable

# Adding Local Variabels to KG
# local variable format: {'var': 'local_8', 'datatype': 'undefined4', 'parent': 'FUN_00401090'}
for l in local_var_list:
    # use the urllib.parse.quote() method to make the variable name work with URI syntax
    local_var = pfs["mkg"][quote(l['var'])]
    data_type = pfs["mkg"][quote(l['datatype'])]
    parent_func = pfs["mkg"][quote(l['parent'])]
    graph.add((local_var, a, local_variable))
    graph.add((local_var, definedIn, parent_func))
    graph.add((local_var, hasDataType, data_type))
    
    
# Parameters:
# param format: {'var': 'hModule', 'datatype': 'typedef HMODULE HINSTANCE', 'parent': 'GetProcAddress'}
# TODO: fix the parsing in data_parser.py
# for p in parameters_list:
#     param = pfs["mkg"][quote(p['var'])]
#     data_type = pfs["mkg"][quote(p['datatype'])]
#     parent_func = pfs["mkg"][quote(l['parent'])]
#     graph.add((param, a, parameter))
#     graph.add((param, passesInto, parent_func))
#     graph.add((param, hasDataType, data_type))

# Namespaces:
# TODO: Adapt this to the other namespace variables
# format: {'namespace': 'switchD_0040f727', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None}
for n in namespace_list:
    n_instance = pfs["mkg"][quote(n['namespace'])]
    graph.add( (n_instance, a, namespace))
    if n['address'] != "NO ADDRESS":
        n_address = pfs["mkg"][quote(n['address'])]
        graph.add( (n_instance, hasAddress, n_address))
    # in the KG, naming the references based on the source address
    # TODO: getting this error: Object Global must be an rdflib term
    n_parent = pfs["mkg"][quote(n['parent'])]
    graph.add((n_instance, definedIn, n_parent))
    if n['references']:
        for r in n['references']:
           ref = "ref_" + str(r['source'])
           graph.add( (n_instance, hasReference, ref))
    if n['primary_reference']:
        ref = "ref_" + str(n['primary_reference']['source'])
        n_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (n_instance, hasPrimaryReference, n_primary_ref))
   
# {'class': 'type_info (GhidraClass)', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None} 
for c in class_list:
    c_instance = pfs["mkg"][quote(c['class'])]
    graph.add( (c_instance, a, class_))
    if c['address'] != "NO ADDRESS":
        c_address = pfs["mkg"][quote(c['address'])]
        graph.add( (c_instance, hasAddress, c_address))
    c_parent = pfs["mkg"][quote(c['parent'])]
    graph.add((c_instance, definedIn, c_parent))    
    if c['references']:
        for r in c['references']:
           ref = "ref_" + str(r['source'])
           graph.add( (c_instance, hasReference, ref))
    if c['primary_reference']:
        ref = "ref_" + str(c['primary_reference']['source'])
        c_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (c_instance, hasPrimaryReference, c_primary_ref))         

# {'dll': 'KERNEL32.DLL', 'address': 'NO ADDRESS parent:Global', 'references': [], 'primary_reference': None}
for l in dll_list:
    l_instance = pfs["mkg"][quote(l['dll'])]
    graph.add( (l_instance, a, dll))
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add( (l_instance, hasAddress, l_address))
    l_parent = pfs["mkg"][quote(l['parent'])]
    graph.add((l_instance, definedIn, l_parent))    
    if l['references']:
        for r in l['references']:
           ref = "ref_" + str(r['source'])
           graph.add( (l_instance, hasReference, ref))
    if l['primary_reference']:
        ref = "ref_" + str(l['primary_reference']['source'])
        l_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (l_instance, hasPrimaryReference, l_primary_ref))
        
# {'func': 'GetTempFileNameW', 'address': 'EXTERNAL:00000007', 'parent': 'KERNEL32.DLL', 
# 'returntype': 'typedef UINT uint', 'returnvalue': '[UINT <RETURN>@EAX:4]', 'functions_called': [], 
# 'references': [{'source': '00422020', 'destination': 'EXTERNAL:00000007', 'operandindex': '0', 'type': 'DATA'}, 
# {'source': '00401327', 'destination': 'EXTERNAL:00000007', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}], 
# 'primary_reference': {'source': '00401327', 'destination': 'EXTERNAL:00000007', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}}
for f in function_list:
    f_instance = pfs["mkg"][quote(f['dll'])]
    graph.add( (f_instance, a, function))
    if f['address'] != "NO ADDRESS":
        f_address = pfs["mkg"][quote(f['address'])]
        graph.add( (f_instance, hasAddress, f_address))
    f_parent = pfs["mkg"][quote(f['parent'])]
    graph.add((f_instance, definedIn, f_parent)) 
    # TODO: add stuff to get the functions called into the graph
    f_return_type = pfs["mkg"][quote(f['returntype'])]
    graph.add((f_instance, hasReturnType, f_return_type))
    f_return_value = pfs["mkg"][quote(f['returnvalue'])]
    graph.add((f_instance, returns, f_return_value))
    if f['references']:
        for r in f['references']:
           ref = "ref_" + str(r['source'])
           graph.add( (f_instance, hasReference, ref))
    if f['primary_reference']:
        ref = "ref_" + str(f['primary_reference']['source'])
        f_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (f_instance, hasPrimaryReference, f_primary_ref))

output_file = "ghidra-scripting/output.ttl"
temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)