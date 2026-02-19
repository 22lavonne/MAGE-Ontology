# modified code from rdflib-starter.py from: https://github.com/kastle-lab/kastle-drawbridge/blob/master/resources/rdflib-starter.py
# rdflib documentation: https://rdflib.readthedocs.io/en/stable/

from data_parser import *

from urllib.parse import quote

##### Graph stuff
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
# break down KGs to have triples in multiple ttl files so they can be added to a triple store wihtout worrying about space
# fix issues with output.tll file
    # lines like "mkg:ADDRESS a :Address ;" and "mkg:DYNAMIC a :Dynamic ;" probably shouldn't be like that
    # and some of the things are in the form "mkg:something" and some of them are in the URI format

# Future TODO:
# maybe change the name of DLL to library since it's called library in the ghidra api

# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]

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
DYNAMIC = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Dynamic")
SCALAR = URIRef("http://www.semanticweb.org/jaspe/ontologies/2026/0/symbol-ontology/Scalar")

# used to map the string version of a symbol name to the URIRef variable for that object
class_dict = {
    "SYMBOL": SYMBOL,
    "LABEL": LABEL,
    "NAMESPACE_SYMBOL": NAMESPACE_SYMBOL,
    "NAMESPACE": NAMESPACE,
    "CLASS_": CLASS_,
    "DLL": DLL,
    "FUNCTION": FUNCTION,
    "VARIABLE": VARIABLE,
    "LOCAL_VARIABLE": LOCAL_VARIABLE,
    "PARAMETER": PARAMETER,
    "DATA_TYPE": DATA_TYPE,
    "ADDRESS": ADDRESS,
    "REFERENCE": REFERENCE,
    "INSTRUCTION": INSTRUCTION,
    "IMMEDIATE_OPERAND": IMMEDIATE_OPERAND,
    "REGISTER": REGISTER,
    "OPCODE": OPCODE,
    "OPERAND": OPERAND,
    "DYNAMIC": DYNAMIC,
    "SCALAR": SCALAR
}

# Initialize an empty graph
graph = init_kg()

# parse the ontology file
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

# method to add references triples for multiple kinds of objects
# takes in the object instance URI, the reference object,
# and a boolean for if the current reference is considered primary
def add_reference(object_instance, reference, isPrimary):
    # name the reference based on both the source and destination addresses
    ref = pfs["mkg"]["ref_" + quote(str(reference['source'])) + "_to_" + quote(str(reference['destination']))]
    graph.add((ref, a, REFERENCE))
    
    # make a slightly different triple based on if the current reference is primary
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
        

# Local variable format example: 
# {'var': 'local_8', 'datatype': 'undefined4', 'parent': 'FUN_00401090'}
for l in local_var_list:
    
    local_var = pfs["mkg"][quote(l['var'])]
    data_type = pfs["mkg"][quote(l['datatype'])]
    parent_func = pfs["mkg"][quote(l['parent'])]
    
    graph.add((local_var, a, LOCAL_VARIABLE))
    graph.add((data_type, a, DATA_TYPE))
    graph.add((parent_func, a, FUNCTION))
    
    graph.add((parent_func, defines, local_var))
    graph.add((local_var, hasDataType, data_type))
    
    
# Parameter format example:
# {'var': 'hModule', 'datatype': 'typedef HMODULE HINSTANCE', 'parent': 'GetProcAddress'}
for p in parameters_list:
    param = pfs["mkg"][quote(p['var'])]
    DATA_TYPE = pfs["mkg"][quote(p['datatype'])]
    parent_func = pfs["mkg"][quote(p['parent'])]
    
    graph.add((param, a, PARAMETER))
    graph.add((parent_func, a, FUNCTION))
    
    graph.add((param, passesInto, parent_func))
    graph.add((param, hasDataType, data_type))


# Namespace format example:
# {'namespace': 'switchD_0040f727', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None}
for n in namespace_list:
    n_instance = pfs["mkg"][quote(n['namespace'])]
    graph.add( (n_instance, a, NAMESPACE))
    
    # add the address of namespace KG (both the address as an ADDRESS object, and the hasAddress relation)
    if n['address'] != "NO ADDRESS":
        n_address = pfs["mkg"][quote(n['address'])]
        graph.add((n_address, a, ADDRESS))
        graph.add( (n_instance, hasAddress, n_address))
        
    # get the parent namespace of the current object
    n_parent = pfs["mkg"][quote(n['parent'])]
    # get the parent namespace type
    parent_type = n['parenttype']
    # if the given parent type is a type of symbol defined in the symbol class dictionary
    if(parent_type in class_dict):
        # then get the URIRef for that type of class and make the triple defining the parent as that type of class.
        graph.add((n_parent, a, class_dict[parent_type]))
    # then add the definedIn relation for the current namespace and its parent namespace
    graph.add((n_instance, definedIn, n_parent))
    
    # if the namespace has any references, add them
    if n['references']:
        for r in n['references']:
            # method that will add a reference to the given object instance
            # false indicates that it's not a primary reference
            add_reference(n_instance, r, False)

    # add primary reference if it exists
    if n['primary_reference']:
            # same as previous, except now it's a parimary reference so the third value is True
            add_reference(n_instance, n['primary_reference'], True)

   
# Class format example:
# {'class': 'type_info (GhidraClass)', 'address': 'NO ADDRESS', 'parent': 'Global', 'references': [], 'primary_reference': None} 
for c in class_list:
    c_instance = pfs["mkg"][quote(c['class'])]
    graph.add( (c_instance, a, CLASS_))
    
    if c['address'] != "NO ADDRESS":
        c_address = pfs["mkg"][quote(c['address'])]
        graph.add((c_address, a, ADDRESS))
        graph.add( (c_instance, hasAddress, c_address))
        
    c_parent = pfs["mkg"][quote(c['parent'])]    
    parent_type = c['parenttype']
    if(parent_type in class_dict):
        graph.add((n_parent, a, class_dict[parent_type]))
    graph.add((c_instance, definedIn, c_parent)) 
       
    if c['references']:
        for r in c['references']:
           ref = pfs["mkg"]["ref_" + str(r['source'])]
           graph.add( (c_instance, hasReference, ref))
           
    if c['primary_reference']:
        ref = pfs["mkg"]["ref_" + str(c['primary_reference']['source'])]
        c_primary_ref = pfs["mkg"][quote(ref)]
        graph.add( (c_instance, hasPrimaryReference, c_primary_ref))         

# DLL format example:
# {'dll': 'KERNEL32.DLL', 'address': 'NO ADDRESS parent:Global', 'references': [], 'primary_reference': None}
for l in dll_list:
    l_instance = pfs["mkg"][quote(l['dll'])]
    graph.add( (l_instance, a, DLL))
    
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add((l_address, a, ADDRESS))
        graph.add( (l_instance, hasAddress, l_address))
        
    l_parent = pfs["mkg"][quote(l['parent'])]
    parent_type = l['parenttype']
    if(parent_type in class_dict):
        graph.add((l_parent, a, class_dict[parent_type])) 
    graph.add((l_instance, definedIn, l_parent))    
    
    if l['references']:
        for r in l['references']:
            add_reference(l_instance, r, False)
    if l['primary_reference']:
        add_reference(l_instance, l['primary_reference'], True)

# Function format example:
# {'func': 'GetTempPathW', 'address': 'EXTERNAL:00000005', 'returntype': 'typedef DWORD ulong', 'returnvalue': '[DWORD <RETURN>@EAX:4]', 
# 'parent': 'KERNEL32.DLL', 'functions_called': [], 
# 'references': [{'source': '00422018', 'destination': 'EXTERNAL:00000005', 'operandindex': '0', 'type': 'DATA'}, 
# {'source': '004012f0', 'destination': 'EXTERNAL:00000005', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}], 
# 'primary_reference': {'source': '004012f0', 'destination': 'EXTERNAL:00000005', 'operandindex': '-1', 'type': 'COMPUTED_CALL'}} 
for f in function_list:
    f_instance = pfs["mkg"][quote(f['func'])]
    graph.add( (f_instance, a, FUNCTION))
    
    if f['address'] != "NO ADDRESS":
        f_address = pfs["mkg"][quote(f['address'])]
        graph.add((f_address, a, ADDRESS))
        graph.add( (f_instance, hasAddress, f_address))
        
    f_parent = pfs["mkg"][quote(f['parent'])]    
    parent_type = f['parenttype']
    if(parent_type in class_dict):
        graph.add((f_parent, a, class_dict[parent_type]))
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

# Label format example:
# {'label': 'shift', 'address': '00000000', 'parent': 'Global', 'parenttype': 'NAMESPACE', 'references': [], 'primary_reference': None}
for l in label_list:
    # add address to the name to diffrentiate different labels with the same name
    l_instance = pfs["mkg"][quote(l['label'] + "_" + l['address'])]
    graph.add( (l_instance, a, LABEL))
    
    if l['address'] != "NO ADDRESS":
        l_address = pfs["mkg"][quote(l['address'])]
        graph.add((l_address, a, ADDRESS))
        graph.add( (l_instance, hasAddress, l_address))
        
    l_parent = pfs["mkg"][quote(l['parent'])]
    parent_type = l['parenttype']
    if(parent_type in class_dict):
        graph.add((l_parent, a, class_dict[parent_type]))
    graph.add((l_instance, definedIn, l_parent)) 
       
    if l['references']:
        for r in l['references']:
            add_reference(l_instance, r, False)
    if l['primary_reference']:
            add_reference(l_instance, l["primary_reference"], True)
        
# Instruction format example:
# {'min_address': '00401090', 'opcode': 'PUSH', 'in_function': 'FUN_00401090', 'numoperands': '1', 
# 'source_operands': [{'operand': 'EBP', 'type': 'REGISTER'}], 
# 'destination_operand': {'operand': 'EBP', 'type': 'REGISTER'}}
for i in instruction_list:
    i_instance = pfs["mkg"]["ins_" + str(i["min_address"])]
    graph.add((i_instance, a, INSTRUCTION))
    
    # opcode
    opcode = pfs["mkg"][quote(i["opcode"])]
    graph.add((opcode, a, OPCODE))
    graph.add((i_instance, hasOpcode, opcode))
    
    if i['source_operands']:
        for s in i['source_operands']:
            operand = pfs["mkg"][quote(s['operand'])]
            graph.add((operand, a, OPERAND))
            
            op_type = s["type"]
            operand_type_instance = pfs["mkg"][quote(op_type)]
            # if the type of operand object is in the class list, then add that triple
            # if the operand type is in the class dictionary, then add that as a triple
            if (op_type in class_dict):
                graph.add((operand_type_instance, a, class_dict[op_type]))
            # then say that that instance performs the role of the current operand
            graph.add((operand_type_instance, performsRole, operand))
            # then give the instrution instance a source operand of this operand
            graph.add((i_instance, hasSourceOperand, operand))
            
    if i['destination_operand']:
        operand = pfs["mkg"][quote(i['destination_operand']['operand'])]
        graph.add((operand, a, OPERAND))
        
        op_type = s["type"]
        operand_type_instance = pfs["mkg"][quote(op_type)]

        if (op_type in class_dict):
            graph.add((operand_type_instance, a, class_dict[op_type]))
        graph.add((operand_type_instance, performsRole, operand))
        
        graph.add((i_instance, hasDestinationOperand, operand))
        
    # get whatever function has this instruction
    func = pfs["mkg"][quote(i['in_function'])]
    # then add the function contains instruction relation with the current instruction
    graph.add((func, a, FUNCTION))
    graph.add((func, containsInstruction, i_instance))    

# then serialize the graph
output_file = "ghidra-scripting/output.ttl"
temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)