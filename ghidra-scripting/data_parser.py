import re

def key_value_parser(line):
    return {
        k: v.strip()
        for k, v in re.findall(r'(\w+)=([^=]+)(?=\s\w+=|$)', line)
    }

def parse_functions(filename):
    func_list = []
    current_function = None
    with open(filename, 'r') as file:
        for read_line in file:
            line = read_line.strip()
            if not line: 
                continue
            parts = line.split(maxsplit=1)
            key = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            # if the current key is function, then create a new function dictionary
            if key == "FUNCTION":
                current_function = key_value_parser(rest)
                current_function["functions_called"] = []
                current_function["references"] = []
                current_function["primary_reference"] = None
                func_list.append(current_function)
            # if the key isn't function and there is no current function, continue to the next line
            elif current_function is None:
                continue
            # else if the key is one of the attributes of function, add it to the current function
            elif key == "CALLEDFUNCTION":
                current_function["functions_called"].append(key_value_parser(rest))
            elif key == "REFERENCE":
                current_function["references"].append(key_value_parser(rest))
            elif key == "PRIMARYREFERENCE":
                current_function["primary_reference"] = key_value_parser(rest)
            else:
                # the key should be one of the above (since all lines should start with one of these names)
                continue
    # print(func_list[1025])
    return func_list


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
    # print(label_list[3])
                
    return label_list

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
    # print(class_list[3])
    return class_list

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
    # print(dll_list[3])
    return dll_list

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
    # print(namespace_list[3])
    return namespace_list

# examample output:
# PARAMETER var=hResInfo datatype=typedef HRSRC HRSRC__ * parent=LoadResource
def parse_parameters(filename):
    param_list = []
    result_list = []
    with open(filename, 'r') as file:
        for line in file:
            param_list.append(line)
    for line in param_list:
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
    # print(result_list[3])
    return result_list

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

def parse_instructions(filename):
    # hint: use .getMnemonicString(), which instruction inherits
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
            if key == "INSTRUCTION":
                current_instruction = key_value_parser(rest)
                current_instruction["source_operands"] = []
                current_instruction["destination_operand"] = []
                instruction_list.append(current_instruction)
            elif current_instruction is None:
                continue
            elif key == "SOURCEOPERAND":
                current_instruction["source_operands"].append(key_value_parser(rest))
            elif key == "DESTINATIONOPERAND":
                current_instruction["destination_operand"].append(key_value_parser(rest))
            else:
                continue
    # print(instruction_list[2])
    return instruction_list

def main():
    parameter_file = "ghidra-scripting/parameter-output.txt"
    l1 = parse_parameters(parameter_file)
    print(l1[0], "\n")
    local_file = "ghidra-scripting/local-variable-output.txt"
    l1 = parse_local(local_file)
    print(l1[0], "\n")
    function_file = "ghidra-scripting/function-output.txt"
    l1 = parse_functions(function_file)
    print(l1[0], "\n")
    label_file = "ghidra-scripting/label-output.txt"
    l1 = parse_labels(label_file)
    print(l1[0], "\n")
    class_file = "ghidra-scripting/class-output.txt"
    l1 = parse_classes(class_file)
    print(l1[0], "\n")
    dll_file = "ghidra-scripting/dll-output.txt"
    l1 = parse_dlls(dll_file)
    print(l1[0], "\n")
    namespace_file = "ghidra-scripting/namespace-output.txt"
    l1 = parse_namespaces(namespace_file)
    print(l1[0], "\n")
    instruction_file = "ghidra-scripting/instruction-output.txt"
    l1 = parse_instructions(instruction_file)
    print(l1[0], "\n")

if __name__ == "__main__":
    main()