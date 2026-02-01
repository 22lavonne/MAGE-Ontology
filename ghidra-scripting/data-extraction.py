#@Emily Miller
#@category ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

from pathlib import Path

# TODO:
# get all namespaces (names and addresses associated with namespace)
# get all imports and exports
# get the DLLs defined in imports and exports (might just be functions)
# Figure out how to find out if functions call other functions

# TODO: AFTER getting all the data into output files, THEN update the schema with all the changes you need
# changes:
    # remove labels
    # add functions and variables to imports and exports (since they are external symbols)

# NOTE: for any given symbol, you can use getParentSymbol() to return the namespace symbol of the namespace containing this symbol

# gets path of where this script is actually located so any extracted txt files can be put in this directory
script_dir = Path(getSourceFile().getAbsolutePath()).parent


# NOTE: if necessary, make variables easier to parse using functions like 
    # variable.getName(), variable.getMinAddress(), variable.getDataType()
# TODO: Figure out how to find out if functions call other functions
# prints all function names and their entry points entry points into function.txt
func_out_path = script_dir / "function-output.txt"
var_out_path = script_dir / "variable-output.txt"
with func_out_path.open("w", encoding="utf-8") as f:
    function = getFirstFunction()
    with var_out_path.open("w", encoding="utf-8") as f2:
        while function is not None:
            f.write("Function name: " + function.getName() + " Function Entry Point: " + str(function.getEntryPoint()) + "\n")
            var_array = function.getAllVariables()
            for variable in var_array:
                # can also use getFunction() method to get the function the variable is located in
                f2.write("Variable from " + str(function) + ": " + variable.getName() + ": " + str(variable) + "\n")
            function = getFunctionAfter(function)
# variable format:
# [undefined4 local_8@Stack[-0x8]:4]
# [data_type variable_name@stack[location]:#_of_bits?]


# prints all instructions in instruction-output.txt
ins_out_path = script_dir / "instruction-output.txt"
with ins_out_path.open("w", encoding="utf-8") as f:
    instruction = getFirstInstruction()
    while instruction is not None:
        f.write("Instruction: " + str(instruction) + "\n")
        instruction = getInstructionAfter(instruction)

# prints all symbols in symbol-output.txt
# TODO: make printing the references in a better format for parsing
# NOTE: there might not be a way to get the primary reference of a symbol, might have to remove it from schema
symbol_out_path = script_dir / "symbol-output.txt"
with symbol_out_path.open("w", encoding="utf-8") as f:
    symbol_iterator = currentProgram.getSymbolTable().getAllSymbols(True)
    for s in symbol_iterator:
        f.write("Symbol: " + str(s) + " address: " + str(s.getAddress()) + " References: ")
        ref_array = s.getReferences()
        for reference in ref_array:
            f.write(str(reference) + ",")
        f.write("\n")

# prints all classes in class-output.txt
# NOTE: all the classes do not have an associated address, which is the case for class and namespace definitions
class_out_path = script_dir / "class-output.txt"
with class_out_path.open("w", encoding="utf-8") as f:
    class_iterator = currentProgram.getSymbolTable().getClassNamespaces()
    for c in class_iterator:
        f.write("Class: " + str(c) + " at address " + str(c.getSymbol().getAddress()) + "\n")

# accessing all namespaces will be a little more difficult, as there is not a function in the API that does this

# TODO: get all symbols for each library
# prints all the DLLs in dll-output.txt
dll_out_path = script_dir / "dll-output.txt"
with dll_out_path.open("w", encoding="utf-8") as f:
    dll_iterator_strs = currentProgram.getExternalManager().getExternalLibraryNames()
    for dll_str in dll_iterator_strs:
        f.write("DLL: " + dll_str + " at address " + str(currentProgram.getExternalManager().getExternalLibrary(dll_str).getSymbol().getAddress()) + "\n")

# getExternalSymbols() gets all symbols external to the given binary, meaning from imports
# TODO: do I update the schema so DLLs contain both variables and functions?