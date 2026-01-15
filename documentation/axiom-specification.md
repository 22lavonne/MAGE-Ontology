## List of Axioms

| #     | Subject       | Relationship          | Object        |
| ----- | ------------- | -----------------     | -----------   |
|   1   |Symbol         |hasReference           |Reference      |
|   2   |Symbol         |hasPrimaryReference    |Reference      |
|   3   |Symbol         |associatedWith         |Address        |
|   4   |Data Symbol    |definedIn              |Lexical Scope Symbol|
|   5   |Lexical Scope Symbol|hasLabel          |Label          |
|   6   |Reference      |hasSourceAddress       |Address        |
|   7   |Reference      |hasDestinationAddress  |Address        |
|   8   |Reference      |hasType                |xsd:string     |
|   9   |Reference      |hasOperandIndex        |xsd:integer    |
|  10   |Address        |addressOf              |xsd:string     |
|  11   |DLL            |definedIn              |Import         |
|  12   |DLL            |definedIn              |Export         |
|  13   |Function       |hasReturnType          |Data Type      |
|  14   |Function       |hasParameter           |Variable       |
|  15   |Function       |returns                |Variable       |
|  16   |Function       |calls                  |Function       |
|  17   |Function       |definedIn              |Class          |
|  18   |Function       |definedIn              |Namespace      |
|  19   |Function       |containsInstruction    |Instruction    |
|  20   |Variable       |hasLabel               |Label          |
|  21   |Variable       |hasDataType            |Data Type      |
|  22   |Data Type      |hasDataTypeName        |xsd:string     |
|  23   |Class          |definedIn              |Namespace      |
|  24   |Label          |hasName                |xsd:string     |
|  25   |Label          |hasAddress             |Address        |
|  26   |Label          |modified               |xsd:boolean    |
|  27   |Namespace      |hasName                |xsd:string     |
|  28   |Instruction    |hasOpcode              |Opcode         |
|  29   |Instruction    |hasSourceOperand       |Operand        |
|  30   |Instruction    |hasDestinationOperand  |Operand        |
|  31   |Address        |performsRole           |Operand        |
|  32   |Register       |performsRole           |Operand        |
|  33   |ImmediateOperand|performsRole          |Operand        |
|  34   |Symbol         |performsRole           |Operand        |


## Axiom Selection

### Key:
* CD: Class Disjointness
* D: Domain
* R: Range
* S: Scoped
* E: Existential
* I: Inverse
* F: Functionality
* Q: Qualified
* ST: Structural Tautology
* SY: Symmetry
* TRANS: Transivity
* REF: Reflexivity


| Rel | CD  |  D  | SD  |  R  | SR  |  E  | IE  |  F  | QF  | SF  | QSF | IF  | IQF | ISF | IQSF| ST  | SY  |TRANS| REF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1    |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|2    |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|3    |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|4    |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|5    |     |     |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|6    |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|7    |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|8    |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|9    |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|10   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|11   |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|12   |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|13   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|14   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|15   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|16   |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |  x  |
|17   |     |     |  x  |     |     |     |     |     |     |     |  ?  |     |     |     |     |     |     |     |     |
|18   |     |     |     |     |     |  x  |     |     |  x  |  x  |  ?  |     |     |     |     |     |     |     |     |
|19   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|20   |     |     |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|21   |     |  x  |     |  x  |     |  x  |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|22   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|23   |     |     |     |     |  x  |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|24   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|25   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|26   |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|27   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|28   |     |  x  |     |  x  |     |  x  |     |     |  x  |     |  x  |     |     |     |     |     |     |     |     |
|29   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|30   |     |  x  |     |  x  |     |     |     |     |  x  |     |  x  |     |     |     |     |     |     |     |     |
|31   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|32   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|33   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|34   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |

### Notes:
- 3: Most symbols must have an associated address, but there are some symbols that are tied to a context or constant value instead.
- 4: Inverse is: Lexical Scope Symbol defines Data Symbol
- 11: Inverse is: Import defines DLL
- 12: Inverse is: Export defines DLL
- 16: Inverse is: Function calledBy Function
- 17: Inverse is: Class defines Function
- 18: Inverse is: Namespace contains Function
- 23: Inverse is: Namespace contains Class