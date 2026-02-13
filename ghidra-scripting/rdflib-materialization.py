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

# Current TODO:
# break down KGs to have triples in multiple ttl files so they can be added to a triple store without worrying about 

# Future TODO:
# get the exact type of symbol the parent is for each instance of this line
    # n_parent = pfs["mkg"][quote(n['parent'])]
    # graph.add((n_instance, definedIn, n_parent))
    # right now I'm just going to say it's of type namespace symbol, but this should be changed to be more specific later
# find a way to figure out what object type each operand should be 
    # like for something like this,
        # operand_type = pfs["mkg"][quote(s["type"])]
        # graph.add((operand, isA, operand_type))
    # figure out what kind of object the operand type should be, and add a triple based on that
    # could be a simple method that loops through and checks for stuff like ADDRESS, REGISTER, DYNAMIC, etc
    # and if there is a type that does not fit as one of the objects in my schema,
    # just do what I am currently doing and don't add an object for it
# organize files so they have consistent formatting
# update all the documentation on github repo

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
defines = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/defines")

# Data Properties
hasOperandIndex = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasOperandIndex")
hasReferenceType = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/hasReferenceType")

# Classes
SYMBOL = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Symbol")
LABEL = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Label")
NAMESPACE_SYMBOL = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/NamespaceSymbol")
NAMESPACE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Namespace")
CLASS_ = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Class")
DLL = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/DLL")
FUNCTION = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Function")
VARIABLE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Variable")
LOCAL_VARIABLE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/LocalVariable")
PARAMETER = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Parameter")
DATA_TYPE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/DataType")
ADDRESS = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Address")
REFERENCE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Reference")
INSTRUCTION = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Instruction")
IMMEDIATE_OPERAND = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/ImmediateOperand")
REGISTER = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Register")
OPCODE = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Opcode")
OPERAND = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Operand")


# Initialize an empty graph
graph = init_kg()

ontology = "ontology/symbol-ontology.ttl"
with open(ontology, "r") as f:
    graph.parse(f)

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

def add_reference(object_instance, reference, isPrimary):
    # add hasReference triple
    ref = pfs["mkg"]["ref_" + quote(str(reference['source'])) + "_to_" + quote(str(reference['destination']))]
    graph.add((ref, a, REFERENCE))
    if isPrimary:
        graph.add((object_instance, hasPrimaryReference, ref))
    else:
        graph.add((object_instance, hasReference, ref))
    
    # add other information about reference
    src_add = pfs["mkg"][quote(str(reference['source']))]
    dest_add = pfs["mkg"][quote(str(reference['destination']))]
    op_index = Literal(reference['operandindex'])
    ref_type = Literal(reference['type'])
    
    graph.add((ref, hasSourceAddress, src_add))
    graph.add((ref, hasDestinationAddress, dest_add))
    graph.add((ref, hasOperandIndex, op_index))
    graph.add((ref, hasReferenceType, ref_type))
        

# Adding Local Variabels to KG
# local variable format: {'var': 'local_8', 'datatype': 'undefined4', 'parent': 'FUN_00401090'}
for l in local_var_list:
    # use the urllib.parse.quote() method to make the variable name work with URI syntax
    local_var = pfs["mkg"][quote(l['var'])]
    data_type = pfs["mkg"][quote(l['datatype'])]
    parent_func = pfs["mkg"][quote(l['parent'])]
    graph.add((local_var, a, LOCAL_VARIABLE))
    graph.add((data_type, a, DATA_TYPE))
    graph.add((parent_func, a, FUNCTION))
    
    graph.add((parent_func, defines, local_var))
    graph.add((local_var, hasDataType, DATA_TYPE))
    
    
# Parameters:
# param format: {'var': 'hModule', 'datatype': 'typedef HMODULE HINSTANCE', 'parent': 'GetProcAddress'}
for p in parameters_list:
    param = pfs["mkg"][quote(p['var'])]
    DATA_TYPE = pfs["mkg"][quote(p['datatype'])]
    parent_func = pfs["mkg"][quote(p['parent'])]
    
    graph.add((param, a, PARAMETER))
    graph.add((parent_func, a, FUNCTION))
    graph.add((param, passesInto, parent_func))
    graph.add((param, hasDataType, DATA_TYPE))

# Namespaces:
# format: {'namespace': 'switchD_0040f727', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None}
for n in namespace_list:
    n_instance = pfs["mkg"][quote(n['namespace'])]
    graph.add( (n_instance, a, NAMESPACE))
    
    if n['address'] != "NO ADDRESS":
        n_address = pfs["mkg"][quote(n['address'])]
        graph.add((n_address, a, ADDRESS))
        graph.add( (n_instance, hasAddress, n_address))
        
    # FIXME: get the exact type of symbol the parent is for each instance of this line
    n_parent = pfs["mkg"][quote(n['parent'])]
    graph.add((n_parent, a, NAMESPACE_SYMBOL))
    graph.add((n_instance, definedIn, n_parent))
    
    if n['references']:
        for r in n['references']:
            # method that will add a reference to the given object instance
            # false indicates that it's not a primary reference
            add_reference(n_instance, r, False)

    if n['primary_reference']:
            # same as previous, except now it's a parimary reference so the third value is True
            add_reference(n_instance, n['primary_reference'], True)

   
# {'class': 'type_info (GhidraClass)', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None} 
for c in class_list:
    c_instance = pfs["mkg"][quote(c['class'])]
    graph.add( (c_instance, a, CLASS_))
    
    if c['address'] != "NO ADDRESS":
        c_address = pfs["mkg"][quote(c['address'])]
        graph.add((c_address, a, ADDRESS))
        graph.add( (c_instance, hasAddress, c_address))
        
    c_parent = pfs["mkg"][quote(c['parent'])]
    # FIXME: change from namespace symbol to more specific
    graph.add((c_parent, a, NAMESPACE_SYMBOL))
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
    graph.add( (l_instance, a, DLL))
    
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add((l_address, a, ADDRESS))
        graph.add( (l_instance, hasAddress, l_address))
        
    l_parent = pfs["mkg"][quote(l['parent'])]
    # FIXME: make more specific than namespace symbol
    graph.add((l_parent, a, NAMESPACE_SYMBOL))
    graph.add((l_instance, definedIn, l_parent))    
    
    if l['references']:
        for r in l['references']:
            add_reference(l_instance, r, False)
    if l['primary_reference']:
        add_reference(l_instance, l['primary_reference'], True)

# {'func': 'GetTempPathW', 'address': 'EXTERNAL:00000005', 'returntype': 'typedef DWORD ulong', 'returnvalue': '[DWORD <RETURN>@EAX:4]', 
# 'parent': 'KERNEL32.DLL', 'functions_called': [], 
# 'references': [{'source': '00422018', 'destination': 'EXTERNAL:00000005', 'operandindex': '0', 'type': 'DATA'}, 
# {'source': '004012f0', 'destination': 'EXTERNAL:00000005', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}], 
# 'primary_reference': {'source': '004012f0', 'destination': 'EXTERNAL:00000005', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}} 
# TODO: if possible, get all instructions present in each function
# would have to modify both data extraction and data parser
for f in function_list:
    f_instance = pfs["mkg"][quote(f['func'])]
    graph.add( (f_instance, a, FUNCTION))
    
    if f['address'] != "NO ADDRESS":
        f_address = pfs["mkg"][quote(f['address'])]
        graph.add((f_address, a, ADDRESS))
        graph.add( (f_instance, hasAddress, f_address))
        
    f_parent = pfs["mkg"][quote(f['parent'])]
    # FIXME: make more specific
    graph.add((f_parent, a, NAMESPACE_SYMBOL))
    graph.add((f_instance, definedIn, f_parent))
     
    # get all the functions called from this function
    if f['functions_called']:
        for fc in f['functions_called']:
            # make the URI of the function since it is seen elsewhere
            func_called = pfs["mkg"][quote(fc['func'])]
            graph.add((func_called, a, FUNCTION))
            graph.add((f_instance, calls, func_called))
            
    # return type
    f_return_type = pfs["mkg"][quote(f['returntype'])]
    graph.add((f_return_type, a, DATA_TYPE))
    graph.add((f_instance, hasReturnType, f_return_type))
    
    # return value (as a parameter)
    f_return_value = pfs["mkg"][quote(f['returnvalue'])]
    graph.add((f_return_type, a, PARAMETER))
    graph.add((f_instance, returns, f_return_value))
    
    
    # if any references exist, add them as triples
    if f['references']:
        for r in f['references']:
            add_reference(f_instance, r, False)
            
    if f['primary_reference']:
        add_reference(f_instance, f['primary_reference'], True)


for l in label_list:
    l_instance = pfs["mkg"][quote(l['label'])]
    graph.add( (l_instance, a, LABEL))
    
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add((l_address, a, ADDRESS))
        graph.add( (l_instance, hasAddress, l_address))
        
    l_parent = pfs["mkg"][quote(l['parent'])]
    graph.add((l_parent, a, NAMESPACE_SYMBOL))
    graph.add((l_instance, definedIn, l_parent)) 
       
    if l['references']:
        for r in l['references']:
            add_reference(l_instance, r, False)
    if l['primary_reference']:
            add_reference(l_instance, l["primary_reference"], True)
        
# {'min_address': '00401090', 'opcode': 'PUSH', 'in_function': 'FUN_00401090', 'numoperands': '1', 
# 'source_operands': [{'operand': 'EBP', 'type': 'REGISTER'}], 
# 'destination_operand': {'operand': 'EBP', 'type': 'REGISTER'}}
for i in instruction_list:
    i_instance = pfs["mkg"]["ins_" + str(i["min_address"])]
    graph.add((i_instance, a, INSTRUCTION))
    
    # opcode
    opcode = pfs["mkg"][quote(i["opcode"])]
    graph.add((opcode, a, OPCODE))
    graph.add((i_instance, hasOpcode, OPCODE))
    
    if i['source_operands']:
        for s in i['source_operands']:
            # TODO: get the type of operand here and add another relation/triple based on that
            operand = pfs["mkg"][quote(s['operand'])]
            graph.add((operand, a, OPERAND))
            
            operand_type = pfs["mkg"][quote(s["type"])]
            # TODO: see if you can figure out what type of object the operand_type should be, and then add that as another triple
            # might have to rework schema to make the isA relation work
            # graph.add((operand, isA, operand_type))
            graph.add((operand_type, performsRole, operand))

            graph.add((i_instance, hasSourceOperand, operand))
            
    if i['destination_operand']:
        operand = pfs["mkg"][quote(i['destination_operand']['operand'])]
        graph.add((operand, a, OPERAND))
        
        operand_type = pfs["mkg"][quote(s["type"])]
        # TODO: change this like above
        # graph.add((operand, isA, operand_type))
        graph.add((operand_type, performsRole, operand))
        
        graph.add((i_instance, hasDestinationOperand, operand))
        
    # get whatever function has this instruction
    func = pfs["mkg"][quote(i['in_function'])]
    # then add the function contains instruction relation with the current instruction
    graph.add((func, a, FUNCTION))
    graph.add((func, containsInstruction, i_instance))    

# then serialize the graph
output_file = "ghidra-scripting/output.ttl"
temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)