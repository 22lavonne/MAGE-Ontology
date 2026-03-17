import re

def key_value_parser(line):
    # split when we get the first instance of an = for a key
    # (prevents an = sign in a value from splitting again)
    pattern = r'(?:^| )(\w+)=(.*?)(?=\s+\w+=|$)'
    matches = re.findall(pattern, line)
    return {k: v.strip() for k, v in matches}

def group_by_blocks(lines):
    
    blocks = []
    current_block = []
    
    for l in lines:
        line = l.strip()
        # get the first word of the line
        first_word = line.split(' ')[0]
        # if the word is all in uppercase, meaning it's a tag like PARAMTER or FUNCTION,
        if first_word.isupper() and len(first_word) > 1:
            if current_block:
                blocks.append(" ".join(current_block))
                current_block = []
                
            current_block.append(line)
            
        # if the line does not start with a tag and a current block exists,
        # then the current line is part of the current block
        elif current_block:
            current_block.append(line)
            
            # since the last part of parameter and the first function line is 'parenttype=', if the current line contains that,
            # then we want to add it and end the current block
            if " parenttype=" in line:
                blocks.append(" ".join(current_block))
                current_block = []
                
    # then if there is still something in current block at the end of the loop,
    # add it to blocks and return
    if current_block:
        blocks.append(" ".join(current_block))
    return blocks

# helper method for parse_parameters,
# takes the blocks made from group_parameter_blocks and parses them and puts it into a dictionary
def parse_by_block(block):
    result = {}
    parts = block.split()
    
    current_key = None
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            result[key] = value
            current_key = key
            
        elif current_key is not None:
            result[current_key] += ' ' + part
    
    return result

# parsing functions from the output file into dictionaries
def parse_functions(filename):
    # will contain all the function dictionaries
    func_list = []
    
    # current function we are working with (since there are multiple lines for different attributes of a function,
    # like FUNCTIONCALLED and REFERENCE)
    current_function = None
    
    # buffer that will allow to get all information of a certain attribute, even if it goes over multiple lines
    buffer = []
    current_tag = None
    
    # helper method to help parse the text and update the function dictionary
    def flush_buffer(tag, text_lines, current_func):
        combined_text = " ".join(text_lines).replace("\n", " ")
        data = key_value_parser(combined_text)
        
        # start of new function dictionary
        if tag == "FUNCTION":
            # initialize the current function to data
            current_func = data
            # make key-value pairs for some of the parts needed for a function 
            # (specifically the parts that will be on newlines)
            current_func.update({"functions_called": [], "references": [], "primary_reference": None})
            
            func_list.append(current_func)
            
        # add the current data as a new item in the functions called list
        elif tag == "FUNCTIONCALLED":
            current_func["functions_called"].append(data)
            
        # add the current data as a new reference in the reference list
        elif tag == "REFERENCE":
            current_func["references"].append(data)
            
        # add the current data as the primary reference of the current function
        elif tag == "PRIMARYREFERENCE":
            current_func["primary_reference"] = data
        
        # returns the current function and all its key-value pairs
        return current_func
    
    # now compile all the function dictionaries into the list
    with open(filename, 'r') as file:
        
        for read_line in file:
            line = read_line.strip()
            if not line: 
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            
            # if the first part of the line is an uppercase tag
            if key.isupper() and len(key) > 1:
                
                # process the data in the previous buffer before processing the current data
                # (if the first word in the line is a tag)
                if current_tag:
                    # gets the new current function based on the current tag, buffer, and current function
                    current_function = flush_buffer(current_tag, buffer, current_function)
                    
                # update and reset for the new buffer
                current_tag = key
                buffer = [parts[1]] if len(parts) > 1 else [""]
                
            # if the first word of the line is not a tag, then it's a continuation of the previous attribute,
            # so add it to the current buffer
            else:
                buffer.append(line)
                
        # flush the last block of the file since the loop doesn't get to it (if a current tag exists)
        if current_tag:
            flush_buffer(current_tag, buffer, current_function)
    
    return func_list
            
# parses labels from the given file (expecting the specific format created from data_extraction.py)
def parse_labels(filename):
    
    label_list = []
    current_label = None
    
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            
            if key == "LABEL":
                current_label = key_value_parser(rest)
                current_label["references"] = []
                current_label["primary_reference"] = None
                label_list.append(current_label)
                
            elif current_label is None:
                continue
            
            elif key == "REFERENCE":
                current_label["references"].append(key_value_parser(rest))
                
            elif key == "PRIMARYREFERENCE":
                current_label["primary_reference"] = key_value_parser(rest)
                
            else:
                continue
                            
    return label_list

# parses through classes
def parse_classes(filename):
    class_list = []
    current_class = None
    
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            
            if key == "CLASS":
                current_class = key_value_parser(rest)
                current_class["references"] = []
                current_class["primary_reference"] = None
                class_list.append(current_class)
                
            elif current_class is None:
                continue
            
            elif key == "REFERENCE":
                current_class["references"].append(key_value_parser(rest))
                
            elif key == "PRIMARYREFERENCE":
                current_class["primary_reference"] = key_value_parser(rest)
                
            else:
                continue

    return class_list

# DLLs
def parse_dlls(filename):
    dll_list = []
    current_dll = None
    
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            
            if key == "DLL":
                current_dll = key_value_parser(rest)
                current_dll["references"] = []
                current_dll["primary_reference"] = None
                dll_list.append(current_dll)
                
            elif current_dll is None:
                continue
            
            elif key == "REFERENCE":
                current_dll["references"].append(key_value_parser(rest))
                
            elif key == "PRIMARYREFERENCE":
                current_dll["primary_reference"] = key_value_parser(rest)
                
            else:
                continue

    return dll_list

# namespaces
def parse_namespaces(filename):
    namespace_list = []
    current_namespace = None
    
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            
            if key == "NAMESPACE":
                current_namespace = key_value_parser(rest)
                current_namespace["references"] = []
                current_namespace["primary_reference"] = None
                namespace_list.append(current_namespace)
                
            elif current_namespace is None:
                continue
            
            elif key == "REFERENCE":
                current_namespace["references"].append(key_value_parser(rest))
                
            elif key == "PRIMARYREFERENCE":
                current_namespace["primary_reference"] = key_value_parser(rest)
                
            else:
                continue

    return namespace_list

# parameters
def parse_parameters(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # gets the parameters into blocks 
    # since some parameters might take up more than one line in the output file
    blocks = group_by_blocks(lines)
    
    result_list = []
    # iterate through all the parameter blocks, puts each into a dictionary 
    # and adds it to the result list
    for block in blocks:
        # makes the dictionary for the current parameter
        result_list.append(parse_by_block(block))
    return result_list

# NOTE: if local variables sometimes take up more lines like parameters do, 
# update this method to implement similarly to the parse parameters function
def parse_local(filename):
    local_list = []
    result_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            local_list.append(line)
            
    for line in local_list:
        parts = line.split()
        if not parts:
            break
        
        current_key = None
        result = {}
        
        for part in parts:
            # if = is contained in the current part, then that means it's a key
            if '=' in part:
                # then split the key value pair
                key, value = part.split('=', 1)
                result[key] = value
                # then change the key
                current_key = key
            # else then the current part is part of a value (where there is a space in a value like in a data type)
            # (unless the current key is still None, in that case the current part is "PARAMETER" and should be ignored)
            elif current_key is not None:
                result[current_key] += ' ' + part
        result_list.append(result)
    # print(result_list[0])
    return result_list

# parse instructions
def parse_instructions(filename):
    instruction_list = []
    current_instruction = None
    
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            
            # similar method to how to parse through references
            if key == "INSTRUCTION":
                current_instruction = key_value_parser(rest)
                current_instruction["source_operands"] = []
                current_instruction["destination_operand"] = None
                instruction_list.append(current_instruction)
                
            elif current_instruction is None:
                continue
            
            elif key == "SOURCEOPERAND":
                current_instruction["source_operands"].append(key_value_parser(rest))
                
            elif key == "DESTINATIONOPERAND":
                current_instruction["destination_operand"] = key_value_parser(rest)
                
            else:
                continue

    return instruction_list

# testing all the parsing functions by printing an item (or multiple) from each list of dictionaries
def main():
    parameter_file = "ghidra-scripting/parameter-output.txt"
    l1 = parse_parameters(parameter_file)
    print(l1[0], "\n")
    # for item in l1:
    #     print(item, "\n")
    
    
    local_file = "ghidra-scripting/local-variable-output.txt"
    l1 = parse_local(local_file)
    print(l1[0], "\n")
    
    function_file = "ghidra-scripting/function-output.txt"
    l1 = parse_functions(function_file)
    print(l1[0], "\n")
    print(l1[4], "\n")
    
    label_file = "ghidra-scripting/label-output.txt"
    l1 = parse_labels(label_file)
    print(l1[0], "\n")
    
    class_file = "ghidra-scripting/class-output.txt"
    l1 = parse_classes(class_file)
    if l1: 
        print(l1[0], "\n")
        
    dll_file = "ghidra-scripting/dll-output.txt"
    l1 = parse_dlls(dll_file)
    print(l1[0], "\n")
    
    namespace_file = "ghidra-scripting/namespace-output.txt"
    l1 = parse_namespaces(namespace_file)
    if l1:
        print(l1[0], "\n")
    
    instruction_file = "ghidra-scripting/instruction-output.txt"
    l1 = parse_instructions(instruction_file)
    print(l1[0], "\n")
    

if __name__ == "__main__":
    main()