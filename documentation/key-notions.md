# Key Notions

* Executable
    * Rationale: Represents the file that is uploaded and analyzed in ghidra, and where the data for the ontology / knowledge graph will come from.
    * Connected Pattern: [part-whole](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/part-whole)
    * Data Source: Labeled ELF files from https://github.com/nimrodpar/Labeled-Elfs 

* Address
    * Rationale: Represents a physical memory address in the executable file where data can be stored.
    * Connected Pattern: [spatial-object](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/spatial-object)
    * Data Source: Ghidra memory model of a given executable

* Reference
    * Rationale: Represents a link between two memory addresses
    * Connected Pattern: [reification](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/reification)
    * Data Source: Ghidra memory model of a given executable

* Disassembly
    * Rationale: Represents the assembly code retrieved from Ghidra disassembling the source code of the executable.
    * Connected Pattern: [data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/data-transformation)
    * Data Source: Disassembly generated from an executable in Ghidra

* Instruction
    * Rationale: Represents an individual instruction obtained from the disassembly. In ontology, will be represented as instructions part of a given function.
    * Connected Pattern: [part-whole pattern](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/part-whole)
    * Data Source: Disassembly generated from an executable in Ghidra

* Decompilation
    * Rationale: Represents the C code retrieved from Ghidra decompiling the source code of the executable.
    * Connected Pattern: [data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/data-transformation)
    * Data Source: Decompilation generated from an executable in Ghidra

* Symbol
    * Rationale: Represents an association between a name and an address, used in Ghidra to represent data.
    * Connected Pattern: [identifier](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier)
    * Data Source: Symbol Tree generated from an executable in Ghidra

* Symbol Tree
    * Rationale: Represents the hierarchical structure that holds all the symbols of the executable, which the ontology is based around.
    * Connected Pattern: [tree](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/tree)
    * Data Source: Symbol Tree generated from an executable in Ghidra

* Function
    * Rationale: Represents a function in the decompilation, where malware is either contained in a function or can be detected through control flow between functions. Implemented as function containing multiple instructions.
    * Connected Pattern: [sequence](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/sequence)
    * Data Source: Decompilation generated from an executable in Ghidra

* Dynamically Linked Library (DLL)
    * Rationale: Represents a library of functions defined externally from the program. External libraries can be used to introduce malicious functions without them being explicitly defined within the executable.
    * Connected Pattern: [aggregation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/aggregation)
    * Data Source: Imports section of symbol tree in Ghidra