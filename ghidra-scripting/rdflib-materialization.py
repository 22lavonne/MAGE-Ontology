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
"mkg": Namespace("https://mkg.com/data#"),
"ont": Namespace("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology"),
"rdf": RDF,
"rdfs": RDFS,
"xsd": XSD,
"owl": OWL,
"time": TIME
}

# TODO: do rdflib.Literal for any time you need to add a literal or plain data values for data attributes
# TODO: Look to see what other relations need to be encoded based on the schema
# TODO: change the local variable relation in the schema, then update the triples for functions to include local variables

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
# print(ONT.symbol)

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
# TODO: change how this works because it says the same named object is defined in multiple functions
# might have to change the schema to have function defines local variable in this case?
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
# TODO: fix the parsing in data_parser.py, since at least one parameter take up multiple lines
for p in parameters_list:
    param = pfs["mkg"][quote(p['var'])]
    data_type = pfs["mkg"][quote(p['datatype'])]
    parent_func = pfs["mkg"][quote(l['parent'])]
    graph.add((param, a, parameter))
    graph.add((param, passesInto, parent_func))
    graph.add((param, hasDataType, data_type))

# Namespaces:
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
           ref = pfs["mkg"]["ref_" + str(r['source'])]
           graph.add( (n_instance, hasReference, ref))
    if n['primary_reference']:
        ref = pfs["mkg"]["ref_" + str(n['primary_reference']['source'])]
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
           ref = pfs["mkg"]["ref_" + str(r['source'])]
           graph.add( (c_instance, hasReference, ref))
    if c['primary_reference']:
        ref = pfs["mkg"]["ref_" + str(c['primary_reference']['source'])]
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
           ref = pfs["mkg"]["ref_" + str(r['source'])]
           graph.add( (l_instance, hasReference, ref))
    if l['primary_reference']:
        ref = pfs["mkg"]["ref_" + str(l['primary_reference']['source'])]
        l_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (l_instance, hasPrimaryReference, l_primary_ref))
        
# FUNCTION func=GetTempFileNameW address=EXTERNAL:00000007 returntype=typedef UINT uint returnvalue=[UINT <RETURN>@EAX:4] parent=KERNEL32.DLL
# REFERENCE source=00422020 destination=EXTERNAL:00000007 operandindex=0 type=DATA
# REFERENCE source=00401327 destination=EXTERNAL:00000007 operandindex=-1 type=COMPUTED_CALL
# PRIMARYREFERENCE source=00401327 destination=EXTERNAL:00000007 operandindex=-1 type=COMPUTED_CALL
# TODO: if possible, get all instructions present in each function
# would have to modify both data extraction and data parser
for f in function_list:
    # print(f["func"])
    f_instance = pfs["mkg"][quote(f['func'])]
    graph.add( (f_instance, a, function))
    if f['address'] != "NO ADDRESS":
        f_address = pfs["mkg"][quote(f['address'])]
        graph.add( (f_instance, hasAddress, f_address))
    f_parent = pfs["mkg"][quote(f['parent'])]
    graph.add((f_instance, definedIn, f_parent)) 
    # Add all the functions called as triples (if any called functions exist)
    if f['functions_called']:
        # print(f["func"], "has functions ")
        for fc in f['functions_called']:
            # print(quote(fc["func"]))
            # make the URI of the function since it is seen elsewhere
            func_called = pfs["mkg"][quote(fc['func'])]
            graph.add((f_instance, calls, func_called))
    # return type
    f_return_type = pfs["mkg"][quote(f['returntype'])]
    graph.add((f_instance, hasReturnType, f_return_type))
    # return value (as a parameter)
    f_return_value = pfs["mkg"][quote(f['returnvalue'])]
    graph.add((f_instance, returns, f_return_value))
    # if any references exist, add them as triples
    if f['references']:
        for r in f['references']:
            # if the reference is an entry point, then hard code it to be Entry_Point
            # since having a space in a URI is not valid
            if r['source'] == "Entry Point":
                ref = pfs["mkg"]["ref_Entry_Point"]
            else:
                ref = pfs["mkg"]["ref_" + str(r['source'])]
        #    ref = "ref_" + str(r['source'])
            graph.add( (f_instance, hasReference, ref))
    # then add the primary reference (should run if there are also references)
    if f['primary_reference']:
        if r['source'] == "Entry Point":
            ref = pfs["mkg"]["ref_Entry_Point"]
        else:
            ref = pfs["mkg"]["ref_" + str(f['primary_reference']['source'])]
        f_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (f_instance, hasPrimaryReference, f_primary_ref))

for l in label_list:
    l_instance = pfs["mkg"][quote(l['label'])]
    graph.add( (l_instance, a, dll))
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add( (l_instance, hasAddress, l_address))
    l_parent = pfs["mkg"][quote(l['parent'])]
    graph.add((l_instance, definedIn, l_parent))    
    if l['references']:
        for r in l['references']:
           ref = pfs["mkg"]["ref_" + str(r['source'])]
           graph.add( (l_instance, hasReference, ref))
    if l['primary_reference']:
        ref = pfs["mkg"]["ref_" + str(l['primary_reference']['source'])]
        l_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (l_instance, hasPrimaryReference, l_primary_ref))
        
# {'opcode': 'MOV', 'numoperands': '2', 
# 'source_operands': [{'operand': 'ECX', 'type': 'REGISTER'}], 
# 'destination_operand': [{'operand': '0x42f8a4', 'type': 'ADDRESS'}]}
# naming the instructions incrementally like this because idk how else to do it
num = 0
for i in instruction_list:
    i_instance = pfs["mkg"]["ins_" + str(num)]
    graph.add((i_instance, a, instruction))
    # opcode
    opcode = pfs["mkg"][quote(i["opcode"])]
    graph.add((i_instance, hasOpcode, opcode))
    if i['source_operands']:
        for s in i['source_operands']:
            # TODO: get the type of operand here and add another relation/triple based on that
            operand = pfs["mkg"][quote(s['operand'])]
            graph.add((i_instance, hasSourceOperand, operand))
    # print(i['destination_operand'])
    if i['destination_operand']:
        # print(i['destination_operand']["operand"])
        dest_operand = i['destination_operand']
        operand_instance = pfs["mkg"][quote(dest_operand['operand'])]
        graph.add((i_instance, hasDestinationOperand, operand_instance))
    num += 1

output_file = "ghidra-scripting/output.ttl"
temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)