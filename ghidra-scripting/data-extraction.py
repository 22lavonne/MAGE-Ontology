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
# remove `namespace symbol hasLabel label`
    # only functions have labels I think?
    # but labels also signify global variables I think
# change `label definedIn Namespace Symbol` or `Namespace symbol hasLabel label` if necessary
    # might need to change both honestly
    # maybe labels are only defined in namespaces?
    # some things are saying label is a type of symbol, 
    #   while others are accessing symbols when asked to access labels
# update key notions and axiomization with new schema
# modify script if necessary when working on string parsing
# if undefined does not work for a data type, change it to something that can work 
    # (functions can return both void and undefined)
# get all labels maybe?
# figure out how to see if there are nested classes

# NOTE: use getSymbolIterator() to get all label symbols


def main():
    # gets path of where this script is actually located so any extracted txt files can be put in this directory
    script_dir = Path(getSourceFile().getAbsolutePath()).parent

    # NOTE: if necessary, make variables easier to parse using functions like 
        # variable.getName(), variable.getMinAddress(), variable.getDataType()
    # prints all function names and their entry points entry points into function-output.txt
    # also prints all local and parameter variables from these functions into variable-output.txt
    func_out_path = script_dir / "function-output.txt"
    var_out_path = script_dir / "variable-output.txt"
    with func_out_path.open("w", encoding="utf-8") as f:
        function = getFirstFunction()
        with var_out_path.open("w", encoding="utf-8") as f2:
            while function is not None:
                f.write("Function name: " + function.getName() + " Entry Point: " + str(function.getEntryPoint()) + " Return Type: " + str(function.getReturnType()))
                var_array = function.getAllVariables()
                for variable in var_array:
                    # can also use getFunction() method to get the function the variable is located in
                    f2.write("Variable from " + str(function) + ": " + variable.getName() + ": " + str(variable) + "\n")
                func_calls = function.getCalledFunctions(monitor)
                # there is also a function that returns all the functions that call this function
                #func_called = function.getCallsFunction(monitor)
                for fun in func_calls:
                    f.write(" Functions called: " + str(fun) + ", ")
                f.write("\n")
                function = getFunctionAfter(function)
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

    # prints all symbols in symbol-output.txt, including their references and primary reference
    symbol_out_path = script_dir / "symbol-output.txt"
    with symbol_out_path.open("w", encoding="utf-8") as f:
        symbol_iterator = currentProgram.getSymbolTable().getAllSymbols(True)
        for s in symbol_iterator:
            f.write("Symbol: " + str(s) + " address: " + str(s.getAddress()) + " Symbol Type: " + str(s.getSymbolType()) + " Parent namespace: " + str(s.getParentNamespace()) +  " References: ")
            ref_array = s.getReferences()
            primary_reference = ""
            for reference in ref_array:
                if reference.isPrimary():
                    primary_reference = str(reference)
                f.write(str(reference) + ",")
            f.write(" Primary reference: " + primary_reference + "\n")

    # prints all classes in class-output.txt
    # NOTE: all the classes do not have an associated address, which is the case for class and namespace definitions
    class_out_path = script_dir / "class-output.txt"
    with class_out_path.open("w", encoding="utf-8") as f:
        class_iterator = currentProgram.getSymbolTable().getClassNamespaces()
        for c in class_iterator:
            f.write("Class: " + str(c) + " at address " + str(c.getSymbol().getAddress()) + "\n")

    # TODO: Do I remove this?
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