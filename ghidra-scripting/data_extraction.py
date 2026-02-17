#@Emily Miller
#@category ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

from pathlib import Path
from ghidra.program.model.symbol import SymbolType
from ghidra.program.model.lang import OperandType

# NOTE: the decompilation is in C, meaning there are not classes in the traditional sense, 
# so functions are only defined in DLLs or Namespaces

# TODO: some functions seem to not have a primary reference in the output file, so fix that

# update key notions and axiomization with new schema
# if undefined does not work for a data type, change it to something that can work 
    # (functions can return both void and undefined)

# prints the functions listed into the instruction_output.txt file
def get_instructions_from_function(func, file):
    if func is None:
        return
    func_entry = func.getAddress()
    func_obj = currentProgram.getFunctionManager().getFunctionAt(func_entry)
    
    instruction_list = []
    # gets the address set where the function body is
    body = func_obj.getBody()
    # get an iterator that iterates over the instructions in the function body
    instructionIterator = currentProgram.getListing().getInstructions(body, True)
    
    for instruction in instructionIterator:
        file.write("INSTRUCTION min_address=" + str(instruction.getMinAddress()))
        file.write(" opcode=" + str(instruction.getMnemonicString()))
        file.write(" in_function=" + str(func.getName()))
        file.write(" numoperands=" + str(instruction.getNumOperands()) + "\n")
        
        num_operands = instruction.getNumOperands()
        for op_index in range(num_operands):
            operand_type = instruction.getOperandType(op_index)
            operand = instruction.getDefaultOperandRepresentation(op_index)

            if (num_operands == 1):
                # if there is only one operand, then it is considered both the source and destination operand
                # (for instructions like push and pop)
                file.write("SOURCEOPERAND operand=" + operand)
                file.write(" type=" + get_operand_type_string(operand_type) + "\n")
                file.write("DESTINATIONOPERAND operand=" + operand)
                file.write(" type=" + get_operand_type_string(operand_type) + "\n")
            else:
                if (op_index == num_operands - 1):
                    file.write("DESTINATIONOPERAND operand=" + operand)
                    file.write(" type=" + get_operand_type_string(operand_type) + "\n")
                else:
                    file.write("SOURCEOPERAND operand=" + operand)
                    file.write(" type=" + get_operand_type_string(operand_type) + "\n")
    

def main():
    # gets path of where this script is actually located so any extracted txt files can be put in this directory
    script_dir = Path(getSourceFile().getAbsolutePath()).parent

    # prints all label symbols in label-output.txt
    label_out_path = script_dir / "label-output.txt"
    func_out_path = script_dir / "function-output.txt"
    local_var_out_path = script_dir / "local-variable-output.txt"
    param_out_path = script_dir / "parameter-output.txt"
    ins_out_path = script_dir / "instruction-output.txt"
    
    # open multiple files here since we will be iterating through all the label and function symbols,
    # and need to get any local variables, parameters, and instructions associated with those (specifically for functions)
    label_file = label_out_path.open("w", encoding="utf-8")
    func_file = func_out_path.open("w", encoding="utf-8")
    local_file = local_var_out_path.open("w", encoding="utf-8")
    param_file = param_out_path.open("w", encoding="utf-8")
    ins_file = ins_out_path.open("w", encoding="utf-8")
    
    try:
        symbol_iterator = currentProgram.getSymbolTable().getSymbolIterator()
        for s in symbol_iterator:
            file_to_write = label_file
            # if current symbol type is a function, print in function file
            if (s.getSymbolType() == SymbolType.FUNCTION):
                # get all the instructions contained in this function and put them into the instruction output file
                get_instructions_from_function(s, ins_file)
                # TODO: change the formatting of the return parameter if necessary 
                func_file.write("FUNCTION func=" + s.getName() + " address=" + str(s.getAddress()) + 
                                " returntype=" + str(s.getObject().getReturnType()) + 
                                " returnvalue=" + str(s.getObject().getReturn()) + 
                                " parent=" + str(s.getParentNamespace()) + 
                                " parenttype=" + str(get_symbol_type_string(s.getParentNamespace().getSymbol())) + "\n")
                func_array = s.getObject().getCalledFunctions(monitor)
                if func_array:
                    for func in func_array:
                        func_file.write("FUNCTIONCALLED func=" + func.getName() + "\n")                        
                # then print the corresponding variables from that function
                # both the local variables and the parameters
                # NOTE: all local variables have the undefined data type
                local_array = s.getObject().getLocalVariables()
                if local_array:
                    for local in local_array:
                        local_file.write("LOCALVARIABLE var=" + local.getName() + " datatype=" + str(local.getDataType()) + 
                                            " parent=" + str(s) + 
                                            " parenttype=FUNCTION\n") # parent type will always be function
                param_array = s.getObject().getParameters()
                if param_array:
                    for param in param_array:
                        param_file.write("PARAMETER var=" + param.getName() + " datatype=" + str(param.getDataType()) + 
                                            " parent=" + str(s) + 
                                            " parenttype=FUNCTION\n") # parent type will always be function
                
                file_to_write = func_file
            # if it's not a function, then it's a label
            else:
                label_file.write("LABEL label=" + s.getName() + " address=" + str(s.getAddress()) + 
                                    " parent=" + str(s.getParentNamespace()) +
                                    " parenttype=" + str(get_symbol_type_string(s.getParentNamespace().getSymbol())) + "\n")
                file_to_write = label_file
            # then, no matter if it was a function or label, print its references
            ref_array = s.getReferences()
            # if there is at least one reference, then print the references.
            # if there is not, then no references will be printed.
            print_references(ref_array, file_to_write)
    
    except Exception as e:
        print("Error occurred while writing to files")
    
    finally:
        label_file.close()
        func_file.close()
        local_file.close()
        param_file.close()
        ins_file.close()
        
    # prints all classes in class-output.txt
    # NOTE: all the classes do not have an associated address in the examples I have seen, 
    # which is the case for class and namespace definitions
    class_out_path = script_dir / "class-output.txt"
    with class_out_path.open("w", encoding="utf-8") as f:
        class_iterator = currentProgram.getSymbolTable().getClassNamespaces()
        for c in class_iterator:
            # NOTE: classes do not have any references when trying to access them through the ghidra api
            # this is because references to classes are often indirect
            # so if I want classes to be able to have references, I might have to do more digging to find them
            f.write("CLASS class=" + str(c) + " address=" + str(c.getSymbol().getAddress()) + 
                    " parent=" + str(c.getSymbol().getParentNamespace())  + 
                    " parenttype=" + str(get_symbol_type_string(c.getParentNamespace().getSymbol())) + "\n")
            ref_array = c.getSymbol().getReferences()
            print_references(ref_array, f)
            

    # prints all the DLLs in dll-output.txt
    dll_out_path = script_dir / "dll-output.txt"
    # define the external manager here to make other calls shorter
    ext_manager = currentProgram.getExternalManager()
    with dll_out_path.open("w", encoding="utf-8") as f:
        dll_iterator_strs = ext_manager.getExternalLibraryNames()
        for dll_str in dll_iterator_strs:
            # get the symbol representation of the library
            dll_symbol = ext_manager.getExternalLibrary(dll_str).getSymbol()
            # NOTE: all external libraries (which are dlls) will have the parent namespace of global
            # dlls also have no direct references
            f.write("DLL dll=" + dll_str + " address=" + str(dll_symbol.getAddress()) + 
                    " parent=" + str(dll_symbol.getParentNamespace()) + 
                    " parenttype=" + str(get_symbol_type_string(dll_symbol.getParentNamespace().getSymbol())) + "\n")
            ref_array = dll_symbol.getReferences()
            print_references(ref_array, f)

    # prints all namespaces into namespace-output.txt
    namespace_out_path = script_dir / "namespace-output.txt"
    with namespace_out_path.open("w", encoding="utf-8") as f:
        namespace_iterator = get_all_namespaces(currentProgram, monitor)
        for namespace in namespace_iterator:
            # f.write("Namespace: " + str(namespace) + " Address: " + str(namespace.getSymbol().getAddress()) + " Parent Namespace: " + str(namespace.getSymbol().getParentNamespace()) + "\n")
            f.write("NAMESPACE namespace=" + str(namespace) + " address=" + str(namespace.getSymbol().getAddress()) + 
                    " parent=" + str(namespace.getSymbol().getParentNamespace()) + 
                    " parenttype=" + str(get_symbol_type_string(namespace.getParentNamespace().getSymbol())) +"\n")
            # NOTE: namespaces also do not have direct references
            ref_array = namespace.getSymbol().getReferences()
            print_references(ref_array, f)

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

# method to print all the references for a given symbol
# must pass in the array of references contained for the symbol, and the current file you are writing to
# NOTE: a symbol does not necessarily have to have a primary reference
def print_references(ref_array, file):
    if ref_array:
        primary_reference = None
        for reference in ref_array:
            if reference.isPrimary():
                primary_reference = reference
            # file_to_write.write(str(reference) + ",")
            file.write("REFERENCE source=" + str(reference.getFromAddress()) + " destination=" + str(reference.getToAddress()) + " operandindex=" + str(reference.getOperandIndex()) + " type=" + str(reference.getReferenceType()) + "\n")
        if primary_reference:
            file.write("PRIMARYREFERENCE source=" + str(primary_reference.getFromAddress()) + " destination=" + str(primary_reference.getToAddress()) + " operandindex=" + str(primary_reference.getOperandIndex()) + " type=" + str(primary_reference.getReferenceType()) + "\n")
    return

# returns the string of the type of operand the current operand type is
# (since operand type is an int that represents what type it is)
def get_operand_type_string(op_type):
    if OperandType.isRegister(op_type):
        op_type_str = "REGISTER"
    elif OperandType.isImmediate(op_type):
        op_type_str = "IMMEDIATE"
    elif OperandType.isAddress(op_type):
        op_type_str = "ADDRESS"
    elif OperandType.isIndirect(op_type) or OperandType.isDataReference(op_type):
        op_type_str = "MEMORY"
    elif OperandType.isImplicit(op_type):
        op_type_str = "IMPLICIT"
    elif OperandType.isScalar(op_type):
        op_type_str = "SCALAR"
    elif OperandType.isDynamic(op_type):
        op_type_str = "DYNAMIC"
    else:
        op_type_str = "UNKNOWN"
    return op_type_str

def get_symbol_type_string(symbol):
    if (symbol.getSymbolType() == SymbolType.FUNCTION):
        return "FUNCTION"
    # TODO: change this if you want global to be its own symbol
    elif (symbol.getSymbolType() == SymbolType.NAMESPACE or symbol.getSymbolType() == SymbolType.GLOBAL):
        return "NAMESPACE"
    elif (symbol.getSymbolType() == SymbolType.CLASS):
        return "CLASS"
    elif (symbol.getSymbolType() == SymbolType.LIBRARY):
        return "DLL"
    elif (symbol.getSymbolType() == SymbolType.PARAMETER):
        return "PARAMETER"
    elif (symbol.getSymbolType() == SymbolType.LABEL):
        return "LABEL"
    else:
        return ""


if __name__ == "__main__":
    main()