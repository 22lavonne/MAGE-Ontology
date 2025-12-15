# Key Notions (Modules)

## Symbol
### Description
A symbol is a named entity in an executable file that is associated with a specific memory address. For this schema, symbols are broken down into two subclasses; data symbols and lexical scope symbols. Data symbols consist of variables and labels, while lexical scope symbols contain symbols where other things can be defined in (functions, classes, imports, exports, and namespaces). A symbol can have one or more references, but only one reference is designated as the primary.

![Symbol](../Schema/schema_diagram_images/symbol_schema.png)
### Axioms
* `(1) Symbol hasReference min 0 Reference` <br />
"A symbol has 0 or more references"
* `(2) Symbol hasPrimaryReference min 0 max 1 Reference` <br />
"A symbol has up to one primary reference"
* `(3) Symbol associatedWith Address exactly 1 Address` <br />
"A symbol is associated with exactly 1 address"
* `Data Symbol subClassOf Symbol` <br />
"Every Data Symbol is a Symbol"
* `Lexical Scope Symbol subClassOf Symbol` <br />
"Every Lexical Scope Symbol is a Symbol"
* `(4) Data Symbol definedIn Lexical Scope Symbol min 0 Symbol` <br />
"Every data symbol is defined in 0 or more Lexical Scope Symbols" <br />
* `(5) Data Symbol definedIn namespace exactly 1 namespace` <br />
"Every data symbol is defined in exactly 1 namespace"
* `(6) Lexical Scope Symbol hasLabel Label exactly 1 Label` <br />
"Every lexical scope symbol has exactly one label"


## Reference
### Description
A reference is where two memory addresses interact with each other in some way, where one address uses another. This is used for things like when a function calls another function or when data is accessed by an instrution. References are 4-tuples, which include the source address, destination address, the type of reference (function call, data being accessed, etc.), and the operand index (which is an int that is either -1, 0, or 1).

![Reference](../Schema/schema_diagram_images/reference_schema.png)
### Axioms
* `(7) Reference hasSourceAddress address exactly 1 sourceAddress` <br />
"A reference has exactly one source address"
* `(8) Reference hasDestinationAddress address exactly 1 destinationAddress` <br />
"A reference has exactly one destination address"
* `(9) Reference hasType xsd:string exactly 1 type` <br />
"A reference has exactly one reference type indicated by a string"
* `(10) Reference hasOperandIndex xsd:integer exactly 1 index` <br />
"A reference has exactly one operand index indicated by an integer"

## Address
### Description
An address is the memory address that holds the data of a given symbol. It is considered an object in this schema so it can be referenced, while also be used as an operand in assmebly instructions. The address itself is stored as a string.

![Address](../Schema/schema_diagram_images/address_schema.png)

### Axioms
* `(11) Address addressOf xsd:string` <br />
"An address refers to a memory address represented by a string"
* `(12) Address performsRole Operand min 0 Operand` <br />
"An address can perform the role of an operand in an instruction"

## Import/Export
### Description
Imports allow files to use outside functions within the current file through dynamic link libraries (DLLs). Exports allow other files to use the functions from the current file through DLLs. <br /> <br />
In terms of malware detection, imports and exports can contain vulnerable functions or functions commonly used in other malware.

![Import/Export](../Schema/schema_diagram_images/import_export_schema.png)
### Axioms
* `Import subClassOf Lexical Scope Symbol` <br />
"Every import is a lexical scope symbol"
* `Export subClassOf Lexical Scope Symbol` <br />
"Every export is a lexical scope symbol"
* `(13) DLL definedIn min 0 Imports` <br />
"Every DLL is defined in 0 or more imports"
* `(14) DLL definedIn min 0 Exports` <br />
"Every DLL is defined in 0 or more exports"
(defines is the inverse of definedIn)


## Function
### Description
The Function objects keeps track of all the aspects of a function, including any functions it calls or functions called by it, the variables passed in (parameters), the local variables defined in the function, the return type of the function, the return variable of the function, the instructions the function contains, and what class the function is contained in (if any).

![Function](../Schema/schema_diagram_images/function_schema.png)

### Axioms
* `Function subClassOf Lexical Scope Symbol` <br />
"Every function is a lexical scope symbol"
* `(15) Function hasReturnType Data Type min 0 max 1 datatype` <br />
"Every function has either no return type (void) or one return type"
* `(16) Function hasParameter min 0 variable` <br />
"A function can pass in 0 or more parameters"
* `(17) Function returns min 0 max 1 variable` <br />
"Every function returns either no variables or one variable"
* `(18) Function calls min 0 Function` <br />
"A function can call 0 or more other functions"
(calledBy is the inverse of calls)
* `(19) Function definedIn class min 0 max 1 Class` <br />
"A function is defined in either 0 or 1 classes"
* `(20) Function definedIn Namespace exactly 1 Namespace` <br />
"A function is defined in exactly 1 namespace"
* `(21) Function containsInstruction min 1 instruction` <br />
"A function contains one or more instructions"

## Variable
### Description
The variable object keeps track of the information about a variable used within the program, including its data type and label. Since it's of type Data Symbol, it means it can be defined in all lexical scope symbols (meaning it can be defined in functions, classes, imports, exports, and/or namespaces).

![Variable](../Schema/schema_diagram_images/variable_schema.png)
### Axioms
* `Variable subClassOf Data Symbol` <br />
"Every variable is a data symbol"
* `(22) Variable hasLabel Label exactly 1 Label` <br />
"Every variable has exactly one label"
* `(23) Variable hasDataType DataType exactly 1 Datatype` <br />
"Every variable has exactly one data type"

## Data Type
### Description
The data type object signifies the data type of a variable or the return type of a function. The name of the data type is specified via string.

![DataType](../Schema/schema_diagram_images/datatype_schema.png)

### Axioms
* `(24) Data Type hasDataTypeName xsd:string exactly 1 name` <br />
"Data type has exactly one data type name indicated by a string"

## Class
### Description
The class objects keeps track of information about a given class. It is defined within a namespace, and variables and functions are defined within the class.

![Class](../Schema/schema_diagram_images/class_schema.png)

### Axioms
* `Class subClassOf Lexical Scope Symbol` <br />
"Every class is a lexical scope symbol"
* `(25) Class definedIn Namespace exactly 1 Namespace` <br />
"A class is defined in exactly 1 namespace"


## Label
### Description
The label object is a type of data symbol that contains a human readable label for all other kinds of symbols. It contains the string of the name of the label and the memory address the label points to.

![Label](../Schema/schema_diagram_images/label_schema.png)
### Axioms
* `Label subClassOf Data Symbol` <br />
"Every label is a data symbol"
* `(26) Label hasName xsd:string exactly 1 name` <br />
"Every label has exactly one name indicated as xsd:string"
* `(27) Label hasAddress Address exactly 1 address` <br />
"Every label has exactly one memory address"
* `(28) Label modified xsd:boolean` <br />
"A label has a value modified that is either true or false" <br />
(If the user modifies the name of a label, this will be set to true.)

## Namespace
### Description
Namespaces group together symbols like functions and classes to make sure there is no naming conflicts within the same scope. Namespaces can hold functions, variables, classes, and other namespaces. Namespaces cannot share names, and classes cannot share names with namespaces.

![Namespace](../Schema/schema_diagram_images/namespace_schema.png)
### Axioms
* `Namespace subClassOf Lexical Scope Symbol` <br />
"Every namespace is a lexical scope symbol"
* `(29) Namespace hasName xsd:string exactly 1 name` <br />
"Every namespace has exactly one name indicated by xsd:string"

## Instruction
### Description
The instruction object refers to an assembly instruction that will originate from the disassembly acquired from Ghidra from a given executable file. An instruction includes one opcode, and one or more operands, where registers, immediate operands (constant values), addresses, or symbols can play the role of an operand.
Assembly instructions that come from Ghidra's disassembly from an executable file. 

![Instruction](../Schema/schema_diagram_images/instruction_schema.png)

### Axioms
* `(30) Instruction hasOpcode exactly 1 Opcode` <br />
"Every instruction has exactly 1 opcode"
* `(31) Instruction hasSourceOperand min 0 Operand` <br />
"Every instruction has 0 or more source operands"
* `(32) Instruction hasDestinationOperand min 0 max 1 Operand` <br />
"Every instruction has exactly 0 or 1 destination oeprands"
* `(33) Address performsRole Operand` <br />
"An address can perform the role of an operand"
* `(34) Register performsRole Operand` <br />
"A register can perform the role of an operand"
* `(35) ImmediateOperand performsRole Operand` <br />
"An immediateOperand can perform the role of an operand"
* `(36) Symbol performsRole Operand` <br />
"A symbol can perform the role of an operand"


## Overall Schema Diagram
![Schema](../Schema/schema_diagram_images/schema.png)