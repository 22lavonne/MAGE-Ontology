#@Emily Miller
#@category ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

from pathlib import Path
from ghidra.program.model.symbol import SymbolType

# TODO:
# modify script if necessary when working on string parsing
# figure out if there are other variables outside of functions that need to be added to variable-output.txt
# get all labels maybe?

# NOTE:
# labels seem very related to variables. Variables are not quite symbols, but many have symbols associated with them
# I feel like I should distinguish them from symbols in the schema, which should be fine to just remove the superclass relation
# since some variables will still have a label (which links it to a type of symbol)

# TODO: AFTER getting all the data into output files, THEN update the schema with all the changes you need
# changes:
    # add functions and variables to imports and exports (since they are external symbols)
    # remove having variables as a type of symbol
    # remove imports and exports, and have DLLs be a subclass of symbol
    # remove data symbol (since only label would be in it)
    # rename lexical scope symbol to namespace symbol, then have libraries, classes, namespaces, and functions be a subclass of that

def main():
    # gets path of where this script is actually located so any extracted txt files can be put in this directory
    script_dir = Path(getSourceFile().getAbsolutePath()).parent

    # NOTE: if necessary, make variables easier to parse using functions like 
        # variable.getName(), variable.getMinAddress(), variable.getDataType()
    # prints all function names and their entry points entry points into function-output.txt
    # also prints all local and parameter variables from these functions into variable-output.txt
    # TODO: figure out if there are other variables outside of functions that need to be added to variable-output.txt
    func_out_path = script_dir / "function-output.txt"
    var_out_path = script_dir / "variable-output.txt"
    with func_out_path.open("w", encoding="utf-8") as f:
        function = getFirstFunction()
        with var_out_path.open("w", encoding="utf-8") as f2:
            while function is not None:
                f.write("Function name: " + function.getName() + " Function Entry Point: " + str(function.getEntryPoint()))
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

    # prints all symbols in symbol-output.txt
    # TODO: add primary reference to symbol
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
                else:
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