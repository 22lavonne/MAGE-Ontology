# Key Notions (Modules)

## Symbol
### Description
A symbol is a named entity in an executable file that is associated with a specific memory address. For this schema, the types of symbols include labels, then a sub class of symbol called namesapce symbol, which includes functions, classes, namespaces, and DLLs (dynamic link libraries). A symbol can have one or more references, but only one reference is designated as the primary reference. Each symbol is also associated with a memory address. <br>
![Symbol](../schema/schema-diagram-images/symbol-schema.png)
### Axioms
* `(1) Symbol hasReference min 0 Reference` <br/>
"A symbol has 0 or more references"
* `(2) Symbol hasPrimaryReference min 0 max 1 Reference` <br/>
"A symbol has up to one primary reference"
* `(3) Symbol hasAddress min 0 max 1 Address` <br/>
"A symbol is associated with up to one address"
* `Label subClassOf Symbol` <br/>
"Every label is a symbol"
* `Namespace Symbol subClassOf Symbol` <br/>
"Every namespace symbol is a symbol"
* `(4) Label definedIn Namespace Symbol exactly 1 Namespace Symbol` <br/>
"Every label is defined in exactly one namespace symbol" 


## Namespace Symbol
### Description
A namespace symbol is a kind of symbol in Ghidra that is used to organize other kinds of symbols. The types of namespace symbols in this schema include functions, classes, DLLs (dynamically linked libraries), and namespaces. Namespace symbols can also be defined in other namespace symbols, like functions defined in namespaces or DLLs, DLLs defined in the global namespace, classes defined in namespaces, etc. Other types of symbols and data like labels are also defined in types of namespace symbols.

![Namespace Symbol](../schema/schema-diagram-images/namespace-symbol-schema.png)

### Axioms
* `Namespace subClassOf Namespace Symbol` <br>
" Every namespace is a namespace symbol"
* `DLL subClassOf Namespace Symbol` <br/>
"Every dll is a namespace symbol"
* `Function Symbol subClassOf namespace Symbol` <br/>
"Every function is a namespace symbol"
* `Class subClassOf Namespace Symbol` <br/>
"Every class is a namespace symbol"
* `(5) Class definedIn Namespace Symbol exactly 1 Namespace Symbol` <br>
"Every class is defined in exactly one namespace symbol"


## Reference
### Description
A reference is where two memory addresses interact with each other in some way, where one address uses another. This is used for things like when a function calls another function or when data is accessed by an instrution. References are 4-tuples, which include the source address, destination address, the type of reference (function call, data being accessed, etc.), and the operand index (which is an int that is either -1, 0, or 1). <br/>
![Reference](../schema/schema-diagram-images/reference-schema.png)
### Axioms
* `(6) Reference hasSourceAddress address exactly 1 sourceAddress` <br/>
"A reference has exactly one source address"
* `(7) Reference hasDestinationAddress address exactly 1 destinationAddress` <br>
"A reference has exactly one destination address"
* `(8) Reference hasType xsd:string exactly 1 type` <br/>
"A reference has exactly one reference type indicated by a string"
* `(9) Reference hasOperandIndex xsd:integer exactly 1 index` <br/>
"A reference has exactly one operand index indicated by an integer"

## Variable
### Description
Variables in this context are tied to functions, and not a type of symbol itself. There are two types of variables in this schema: parameters, which are passed into and returned from functions, and local variables, which are defined locally within the function itself. Every variable has a data type associated with it.

![Variable](../schema/schema-diagram-images/variable-schema.png)

### Axioms
* `(10) Variable hasDataType Data Type exactly 1 data type` <br>
" Every variable has exactly 1 data type"
* `Local Variable subClassOf Variable` <br>
"Every local variable is a variable"
* `Parameter subClassOf Variable` <br>
"Every parameter is a variable"
* `(11) Parameter passesInto min 0 Function` <br>
"A parameter is passed into min 0 functions"


## Function
### Description
The Function objects keeps track of all the aspects of a function, including any functions it calls or functions called by it, the parameters passed in, the local variables defined in the function, the return type of the function, the return parameter of the function, the instructions the function contains, and what class the function is contained in (if any). <br>
![Address](../schema/schema-diagram-images/function-schema.png)
### Axioms
* `(12) Function defines min 0 Local Variables` <br>
"A fuction can define 0 or more local variables"
* `(13) Function hasReturnType Data Type min 0 max 1 datatype` <br>
"Every function has either no return type (void) or one return type"
* `(14) Function returns min 0 max 1 Parameter` <br>
"Every function returns either no parameters or one parameter"
* `(15) Function calls min 0 Function` <br>
"A function can call 0 or more other functions"
(calledBy is the inverse of calls)
* `(16) Function definedIn Namespace Symbol Exactly 1 Namespace Symbol` <br>
"A function is defined in exactly one lexical scope symbol"
* `(17) Function containsInstruction min 1 instruction` <br>
"A function contains one or more instructions"


## Instruction
### Description
The instruction object refers to an assembly instruction that will originate from the disassembly acquired from Ghidra from a given executable file. An instruction includes one opcode, and zero or more operands, where registers, immediate operands (constant values), addresses, dynamic type objects, and scalars can play the role of an operand. These are assembly instructions that come from Ghidra's disassembly from an executable file. 

![Instruction](../schema/schema-diagram-images/instruction-schema.png)

### Axioms
* `(18) Instruction hasOpcode exactly 1 Opcode` <br>
"Every instruction has exactly 1 opcode"
* `(19) Instruction hasSourceOperand min 0 Operand` <br>
"Every instruction has 0 or more source operands"
* `(20) Instruction hasDestinationOperand min 0 max 1 Operand` <br>
"Every instruction has exactly 0 or 1 destination oeprands"
* `(21) Address performsRole Operand` <br>
"An address can perform the role of an operand"
* `(22) Register performsRole Operand` <br>
"A register can perform the role of an operand"
* `(23) ImmediateOperand performsRole Operand` <br>
"An immediateOperand can perform the role of an operand"
* `(24) Dynamic performsRole Operand` <br>
"A dynamic can perform the role of an operand"
* `(25) Scalar performsRole Operand` <br>
"A scalar can perform the role of an operand"


## Overall Schema Diagram
![Schema](../schema/schema-diagram-images/updated-schema.png)