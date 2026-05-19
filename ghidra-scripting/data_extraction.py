#@Emily Miller
#@category Ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

import os
import sys

from pathlib import Path
from ghidra.program.model.symbol import SymbolType
from ghidra.program.model.lang import OperandType

# NOTE: the decompilation is in C, meaning there are not classes in the traditional sense, 
# so functions are only defined in DLLs or Namespaces

# if undefined does not work for a data type, change it to something that can work 
    # (functions can return both void and undefined)

# prints the instructions from the current function into the instruction_output.txt file
def get_instructions_from_function(func, file):
    if func is None:
        return
    func_entry = func.getAddress()
    func_obj = currentProgram.getFunctionManager().getFunctionAt(func_entry)
    
    # gets the address set where the function body is
    body = func_obj.getBody()
    # get an iterator that iterates over the instructions in the function body
    instructionIterator = currentProgram.getListing().getInstructions(body, True)
    
    for instruction in instructionIterator:
        file.write("INSTRUCTION min_address=" + str(instruction.getMinAddress()))
        file.write(" opcode=" + instruction.getMnemonicString().upper())
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
                # else if this is the final operand, then it must be the destination operand
                if (op_index == num_operands - 1):
                    file.write("DESTINATIONOPERAND operand=" + operand)
                    file.write(" type=" + get_operand_type_string(operand_type) + "\n")
                # else it's a source operand
                else:
                    file.write("SOURCEOPERAND operand=" + operand)
                    file.write(" type=" + get_operand_type_string(operand_type) + "\n")
                    
# function to get all the namespaces of the program
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
            file.write("REFERENCE source=" + str(reference.getFromAddress()) + 
                       " destination=" + str(reference.getToAddress()) + 
                       " operandindex=" + str(reference.getOperandIndex()) + 
                       " type=" + str(reference.getReferenceType()) + 
                       "\n")
            
        if primary_reference:
            file.write("PRIMARYREFERENCE source=" + str(primary_reference.getFromAddress()) + 
                       " destination=" + str(primary_reference.getToAddress()) + 
                       " operandindex=" + str(primary_reference.getOperandIndex()) + 
                       " type=" + str(primary_reference.getReferenceType()) + "\n")
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
    

def main():
    # gets path of where this script is actually located
    script_dir = Path(getSourceFile().getAbsolutePath()).parent
    
    # then ask the user for a name of a directory that they want the output files to go into
    dir_name = askString("Name", "Enter new directory name:", "default_name")
    
    # then establish that directory as the ones the output files will go into
    new_dir = script_dir / dir_name
    
    # boolean that checks if the new directory was created
    dir_created = False
    # if the new directory was created, then move forward with the data extraction.
    # if some exception is found, print what the exception is
    try:
        os.mkdir(new_dir)
        print(f"Directory '{new_dir}' created successfully.")
        dir_created = True
    except FileExistsError:
        print(f"Directory '{new_dir}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{new_dir}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # if a new directory could not be created, the exit the program.
    if not new_dir:
        sys.exit

    
    # get the path for where these 5 files will be stored in, 
    # will be used in try catch block to print information about all 5 types of objects
    label_out_path = new_dir / "label-output.txt"
    func_out_path = new_dir / "function-output.txt"
    local_var_out_path = new_dir / "local-variable-output.txt"
    param_out_path = new_dir / "parameter-output.txt"
    ins_out_path = new_dir / "instruction-output.txt"
    class_out_path = new_dir / "class-output.txt"
    dll_out_path = new_dir / "dll-output.txt"
    namespace_out_path = new_dir / "namespace-output.txt"
    
    
    # open multiple files here since we will be iterating through all the label and function symbols,
    # and need to get any local variables, parameters, and instructions associated with those (specifically for functions)
    label_file = label_out_path.open("w", encoding="utf-8")
    func_file = func_out_path.open("w", encoding="utf-8")
    local_file = local_var_out_path.open("w", encoding="utf-8")
    param_file = param_out_path.open("w", encoding="utf-8")
    ins_file = ins_out_path.open("w", encoding="utf-8")
    
    try:
        # iterate through all the symbols in the current program
        symbol_iterator = currentProgram.getSymbolTable().getSymbolIterator()
        for s in symbol_iterator:
            
            # this variable indicates where the references to the current object will be printed to
            # (will be either func_file or label_file)
            file_to_write = None
            
            # if current symbol type is a function, print in function file
            if (s.getSymbolType() == SymbolType.FUNCTION):
                file_to_write = func_file
                # get all the instructions contained in this function and put them into the instruction output file
                get_instructions_from_function(s, ins_file)
                
                # write information about the function in the function output file
                func_file.write("FUNCTION func=" + s.getName() + 
                                " address=" + str(s.getAddress()) + 
                                " returntype=" + str(s.getObject().getReturnType()) + 
                                " returnvalue=" + str(s.getObject().getReturn()) + 
                                " parent=" + str(s.getParentNamespace()) + 
                                " parenttype=" + str(get_symbol_type_string(s.getParentNamespace().getSymbol())) +
                                "\n")
                
                # get all the functions called by this current function
                func_array = s.getObject().getCalledFunctions(monitor)
                if func_array:
                    for func in func_array:
                        func_file.write("FUNCTIONCALLED func=" + func.getName() + "\n")  
                                              
                # print the corresponding variables from that function
                # both the local variables and the parameters
                # NOTE: all local variables have the undefined data type in the examples I have seen
                local_array = s.getObject().getLocalVariables()
                if local_array:
                    for local in local_array:
                        local_file.write("LOCALVARIABLE var=" + local.getName() + 
                                         " datatype=" + str(local.getDataType()) + 
                                         " parent=" + str(s) + 
                                         " parenttype=FUNCTION\n") # parent type will always be function
                
                param_array = s.getObject().getParameters()
                if param_array:
                    for param in param_array:
                        param_file.write("PARAMETER var=" + param.getName() + 
                                         " datatype=" + str(param.getDataType()) + 
                                         " parent=" + str(s) + 
                                         " parenttype=FUNCTION\n") # parent type will always be function
                
            # if it's not a function, then it's a label
            else:
                file_to_write = label_file
                
                label_file.write("LABEL label=" + s.getName() + 
                                 " address=" + str(s.getAddress()) + 
                                 " parent=" + str(s.getParentNamespace()) +
                                 " parenttype=" + str(get_symbol_type_string(s.getParentNamespace().getSymbol())) + 
                                 "\n")
                
            # then, no matter if it was a function or label, get its references
            ref_array = s.getReferences()
            
            # if there is at least one reference, then print the references.
            # if there is not, then no references will be printed.
            # this method will print the references of the current symbol in the given file
            print_references(ref_array, file_to_write)
    
    # in case there are any errors with file management
    except Exception as e:
        print("Error occurred while writing to files")
    
    # make sure all the files are closed after executing this section
    finally:
        label_file.close()
        func_file.close()
        local_file.close()
        param_file.close()
        ins_file.close()
        
    # prints all classes in class-output.txt
    # NOTE: all the classes do not have an associated address in the examples I have seen, 
    # which is the case for class and namespace definitions
    with class_out_path.open("w", encoding="utf-8") as f:
        
        # get a list of all the classes
        class_iterator = currentProgram.getSymbolTable().getClassNamespaces()
        
        for c in class_iterator:
            # NOTE: classes do not have any references when trying to access them through the ghidra api
            # this is because references to classes are often indirect
            f.write("CLASS class=" + str(c) + 
                    " address=" + str(c.getSymbol().getAddress()) + 
                    " parent=" + str(c.getSymbol().getParentNamespace())  + 
                    " parenttype=" + str(get_symbol_type_string(c.getParentNamespace().getSymbol())) + 
                    "\n")
            
            ref_array = c.getSymbol().getReferences()
            # then print the references for the class (if there are any)
            print_references(ref_array, f)
            

    # prints all the DLLs in dll-output.txt
    # define the external manager here to make other calls shorter
    ext_manager = currentProgram.getExternalManager()
    
    with dll_out_path.open("w", encoding="utf-8") as f:
        # get all the external libraries
        dll_iterator_strs = ext_manager.getExternalLibraryNames()
        for dll_str in dll_iterator_strs:
            # get the symbol representation of the library
            dll_symbol = ext_manager.getExternalLibrary(dll_str).getSymbol()
            
            # NOTE: all external libraries (which are dlls) will have the parent namespace of global
            # dlls also have no direct references
            f.write("DLL dll=" + dll_str + 
                    " address=" + str(dll_symbol.getAddress()) + 
                    " parent=" + str(dll_symbol.getParentNamespace()) + 
                    " parenttype=" + str(get_symbol_type_string(dll_symbol.getParentNamespace().getSymbol())) + 
                    "\n")
            
            ref_array = dll_symbol.getReferences()
            print_references(ref_array, f)

    # prints all namespaces into namespace-output.txt
    with namespace_out_path.open("w", encoding="utf-8") as f:
        
        namespace_iterator = get_all_namespaces(currentProgram, monitor)
        for namespace in namespace_iterator:
            f.write("NAMESPACE namespace=" + str(namespace) + 
                    " address=" + str(namespace.getSymbol().getAddress()) + 
                    " parent=" + str(namespace.getSymbol().getParentNamespace()) + 
                    " parenttype=" + str(get_symbol_type_string(namespace.getParentNamespace().getSymbol())) +
                    "\n")
            
            # NOTE: namespaces also do not have direct references
            ref_array = namespace.getSymbol().getReferences()
            print_references(ref_array, f)

if __name__ == "__main__":
    main()