def parse_functions(filename):
    func_list = []
    result_list = []
    with open(filename, 'r') as file:
        for line in file:
            func_list.append(line)
    # for line in func_list:
    #     parts = line.split()
    #     if not parts:
    #         break
    #     for part in parts:
    # return

def parse_labels(filename):
    label_list = []
    with open(filename, 'r') as file:
        for line in file:
            print("")
    return

def parse_classes(filename):
    class_list = []
    with open(filename, 'r') as file:
        for line in file:
            print("")
    return

def parse_dlls(filename):
    dll_list = []
    with open(filename, 'r') as file:
        for line in file:
            print("")
    return

def parse_namespaces(filename):
    namespace_list = []
    with open(filename, 'r') as file:
        for line in file:
            print("")
    return

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
    print(result_list[0])
    return

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
    print(result_list[0])
    return

def parse_instructions(filename):
    instruction_list = []
    with open(filename, 'r') as file:
        for line in file:
            print("")
    return

def main():
    parameter_file = "parameter-output.txt"
    # parse_parameters(parameter_file)
    local_file = "local-variable-output.txt"
    parse_local(local_file)

if __name__ == "__main__":
    main()