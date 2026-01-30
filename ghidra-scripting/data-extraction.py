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

# function names and entry points:
# with open('/wsl.localhost/Ubuntu/home/emiller/MKG/Ghidra-Scripting/output.txt', 'w+') as f:
# out_path = Path("\\wsl$\Ubuntu\home\emiller\MKG\Ghidra-Scriptin\goutput.txt")
# with out_path.open("w", encoding="utf-8") as f:
# with open("\\wsl$\Ubuntu\home\emiller\MKG\Ghidra-Scriptin\goutput.txt", "w+", encoding="utf-8") as f:
# with redirect_stdout(f):
script_dir = Path(getSourceFile().getAbsolutePath()).parent
func_out_path = script_dir / "function-output.txt"

# TODO: figure out how to get all the variables from each function
# returns all functions in function_output.txt
with func_out_path.open("w", encoding="utf-8") as f:
    function = getFirstFunction()
    while function is not None:
        f.write("Function name: " + function.getName() + " Function Entry Point: " + str(function.getEntryPoint()) + "\n")
        function = getFunctionAfter(function)

# returns all instructions in instruction_output.txt
ins_out_path = script_dir / "instruction-output.txt"


with ins_out_path.open("w", encoding="utf-8") as f:
    instruction = getFirstInstruction()
    while instruction is not None:
        f.write("Instruction: " + str(instruction) + "\n")
        instruction = getInstructionAfter(instruction)

# notes about instructions:
# ghidra api website: https://ghidra.re/ghidra_docs/api/index.html 
# getResultObjects() function is not recognized, even though it shows up in ghidra API website
# getOperandType() only works if you have the operand index, same with getOpObjects()
# so i need to get a way to find all the operand indexes
