#@Emily Miller
#@category ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

from pathlib import Path
from ghidra.program.model.symbol import SymbolType

# TODO:
# look into the differences between variables in functions and SymbolType.PARAMETER, SymbolType.LOCAL_VAR, and SymbolType.GLOBAL_VAR
    # also see if variables should always have a label associated with them
# remove `namespace symbol hasLabel label` from BOTH SCHEMA AND ONTOLOGY
# for this schema we are having label be a type of symbol, so not a label for all symbols

# update key notions and axiomization with new schema
# modify script if necessary when working on string parsing
# if undefined does not work for a data type, change it to something that can work 
    # (functions can return both void and undefined)
# figure out how to see if there are nested classes

# NOTE: use getSymbolIterator() to get all label symbols


def main():
    # gets path of where this script is actually located so any extracted txt files can be put in this directory
    script_dir = Path(getSourceFile().getAbsolutePath()).parent

    # prints all label symbols in label-output.txt
    label_out_path = script_dir / "label-output.txt"
    func_out_path = script_dir / "function-output.txt"
    var_out_path = script_dir / "variable-output.txt"
    with label_out_path.open("w", encoding="utf-8") as label_file:
        with func_out_path.open("w", encoding="utf-8") as func_file:
            with var_out_path.open("w", encoding="utf-8") as var_file:
                symbol_iterator = currentProgram.getSymbolTable().getSymbolIterator()
                for s in symbol_iterator:
                    file_to_write = label_file
                    # if current symbol type is a function, print in function file
                    if (s.getSymbolType() == SymbolType.FUNCTION):
                        func_file.write("Function name: " + s.getName() + " Addesss: " + str(s.getAddress()) + " Parent Namespace: " + str(s.getParentNamespace()) + " References: ")
                        # then print the corresponding variables from that function
                        # since s is currently of type Function Symbol (which is just the naming mechanism) 
                        # and not Function (which represents the actual function), we have to get the function object from the symbol
                        # in order to call the method getAllVariables() on it.
                        var_array = s.getObject().getAllVariables()
                        for var in var_array:
                            # TODO: make this easier to parse through by using methods like var.getName(), var.getMinAddress, and var.getDataType()
                            # there is also a way to get if the variable is a parameter or local variable
                            var_file.write("Variable from " + str(s) + ": " + var.getName() + ": " + str(var) + "\n")
                        # change this to f2 so the references print to the function output file for this symbol
                        file_to_write = func_file
                    # if it's not a function, then it's a label
                    else:
                        label_file.write("Label name: " + s.getName() + " Addesss: " + str(s.getAddress()) + " Parent Namespace: " + str(s.getParentNamespace()) + " References: ")
                        file_to_write = label_file
                    # then, no matter if it was a function or label, print its references
                    ref_array = s.getReferences()
                    primary_reference = ""
                    file_to_write.write("")
                    for reference in ref_array:
                        if reference.isPrimary():
                            primary_reference = str(reference)
                        file_to_write.write(str(reference) + ",")
                    #TODO: maybe write something here that will make it print something different if there is no primary reference
                    file_to_write.write(" Primary reference: " + primary_reference + "\n")
    # variable format:
    # [undefined4 local_8@Stack[-0x8]:4]
    # [data_type variable_name@stack[location]:#_of_bits?]


    # prints all instructions in instruction-output.txt
    # TODO: use methods for instructions to make parsing easier if necessary
    ins_out_path = script_dir / "instruction-output.txt"
    with ins_out_path.open("w", encoding="utf-8") as f:
        instruction = getFirstInstruction()
        while instruction is not None:
            f.write("Instruction: " + str(instruction) + "\n")
            instruction = getInstructionAfter(instruction)
    
    # prints all classes in class-output.txt
    # NOTE: all the classes do not have an associated address, which is the case for class and namespace definitions
    class_out_path = script_dir / "class-output.txt"
    with class_out_path.open("w", encoding="utf-8") as f:
        class_iterator = currentProgram.getSymbolTable().getClassNamespaces()
        for c in class_iterator:
            f.write("Class: " + str(c) + " at address " + str(c.getSymbol().getAddress()) + "\n")

    # prints all the DLLs in dll-output.txt
    dll_out_path = script_dir / "dll-output.txt"
    with dll_out_path.open("w", encoding="utf-8") as f:
        dll_iterator_strs = currentProgram.getExternalManager().getExternalLibraryNames()
        for dll_str in dll_iterator_strs:
            f.write("DLL: " + dll_str + " at address " + str(currentProgram.getExternalManager().getExternalLibrary(dll_str).getSymbol().getAddress()) + "\n")

    # prints all namespaces into namespace-output.txt
    namespace_out_path = script_dir / "namespace-output.txt"
    with namespace_out_path.open("w", encoding="utf-8") as f:
        namespace_iterator = get_all_namespaces(currentProgram, monitor)
        for namespace in namespace_iterator:
            f.write("Namespace: " + str(namespace) + "\n")

# function to get all the namespaces of the program
# (since there is no built in method to do that in the current ghidra api)
# starts with the global namespace, then recursively traverses through the child namespaces
# and adds any symbol of type namespace it comes across
def get_all_namespaces(program, monitor):
    symbol_table = program.getSymbolTable()
    global_namespace = program.getGlobalNamespace()
    all_namespaces = []
    def traverse_namespaces(parent_namespace):
        parent_symbol = parent_namespace.getSymbol()
        children_symbols = symbol_table.getChildren(parent_symbol)
        
        for symbol in children_symbols:
            if monitor.isCancelled():
                return 
            if symbol.getSymbolType() in [SymbolType.NAMESPACE, SymbolType.CLASS, SymbolType.LIBRARY, SymbolType.FUNCTION]:
                child_namespace = symbol.getObject()
                if (child_namespace.getSymbol().getSymbolType() == SymbolType.NAMESPACE):
                    all_namespaces.append(child_namespace)
                    traverse_namespaces(child_namespace)

    traverse_namespaces(global_namespace)
    return all_namespaces

if __name__ == "__main__":
    main()