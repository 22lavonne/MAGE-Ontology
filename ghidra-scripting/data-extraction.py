#TODO extract the data needed from the decompiled ghidra executable
#@Emily Miller
#@category ontology
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

from pathlib import Path

# TODO:
# get all the function names and entry points
# get all the local variables for each function
# get all the symbols and their addresses
# maybe put all types of symbols into their own classes?

# gets path of where this script is actually located so any extracted txt files can be put in this directory
script_dir = Path(getSourceFile().getAbsolutePath()).parent


# TODO: figure out how to get all the variables from each function
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

# prints all instructions in instruction-output.txt
ins_out_path = script_dir / "instruction-output.txt"
with ins_out_path.open("w", encoding="utf-8") as f:
    instruction = getFirstInstruction()
    while instruction is not None:
        f.write("Instruction: " + str(instruction) + "\n")
        instruction = getInstructionAfter(instruction)

# prints all symbols in symbol-output.txt
symbol_out_path = script_dir / "symbol-output.txt"
with symbol_out_path.open("w", encoding="utf-8") as f:
    symbol_iterator = currentProgram.getSymbolTable().getAllSymbols(True)
    for s in symbol_iterator:
        f.write("Symbol: " + str(s) + " address: " + str(s.getAddress()) +  "\n")



# notes about instructions:
# ghidra api website: https://ghidra.re/ghidra_docs/api/index.html 