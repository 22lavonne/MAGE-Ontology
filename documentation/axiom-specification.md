## List of Axioms

| #     | Subject       | Relationship          | Object        |
| ----- | ------------- | -----------------     | -----------   |
|   1   |Symbol         |hasReference           |Reference      |
|   2   |Symbol         |hasPrimaryReference    |Reference      |
|   3   |Symbol         |associatedWith         |Address        |
|   4   |Data Symbol    |definedIn              |Lexical Scope Symbol|
|   5   |Data Symbol    |definedIn              |Namespace      |
|   6   |Lexical Scope Symbol|hasLabel          |Label          |
|   7   |Reference      |hasSourceAddress       |Address        |
|   8   |Reference      |hasDestinationAddress  |Address        |
|   9   |Reference      |hasType                |xsd:string     |
|  10   |Reference      |hasOperandIndex        |xsd:integer    |
|  11   |Address        |addressOf              |xsd:string     |
|  12   |DLL            |definedIn              |Import         |
|  13   |DLL            |definedIn              |Export         |
|  14   |Function       |hasReturnType          |Data Type      |
|  15   |Function       |hasParameter           |Variable       |
|  16   |Function       |returns                |Variable       |
|  17   |Function       |calls                  |Function       |
|  18   |Function       |definedIn              |Class          |
|  19   |Function       |definedIn              |Namespace      |
|  20   |Function       |containsInstruction    |Instruction    |
|  21   |Variable       |hasLabel               |Label          |
|  22   |Variable       |hasDataType            |Data Type      |
|  23   |Data Type      |hasDataTypeName        |xsd:string     |
|  24   |Class          |definedIn              |Namespace      |
|  25   |Label          |hasName                |xsd:string     |
|  26   |Label          |hasAddress             |Address        |
|  27   |Label          |modified               |xsd:boolean    |
|  28   |Namespace      |hasName                |xsd:string     |
|  29   |Instruction    |hasOpcode              |Opcode         |
|  30   |Instruction    |hasSourceOperand       |Operand        |
|  31   |Instruction    |hasDestinationOperand  |Operand        |
|  32   |Address        |performsRole           |Operand        |
|  33   |Register       |performsRole           |Operand        |
|  34   |ImmediateOperand|performsRole          |Operand        |
|  35   |Symbol         |performsRole           |Operand        |


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
|5    |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|6    |     |     |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|7    |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|8    |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|9    |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|10   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|11   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|12   |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|13   |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|14   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|15   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|16   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|17   |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |  x  |
|18   |     |     |  x  |     |     |     |     |     |     |     |  ?  |     |     |     |     |     |     |     |     |
|19   |     |     |     |     |     |  x  |     |     |  x  |  x  |  ?  |     |     |     |     |     |     |     |     |
|20   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|21   |     |     |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|22   |     |  x  |     |  x  |     |  x  |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|23   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|24   |     |     |     |     |  x  |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|25   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|26   |     |  x  |     |  x  |     |     |     |     |  x  |  x  |     |     |     |     |     |     |     |     |     |
|27   |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|28   |     |  x  |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |     |
|29   |     |  x  |     |  x  |     |  x  |     |     |  x  |     |  x  |     |     |     |     |     |     |     |     |
|30   |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|31   |     |  x  |     |  x  |     |     |     |     |  x  |     |  x  |     |     |     |     |     |     |     |     |
|32   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|33   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|34   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|35   |     |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |

### Notes:
- 3: Most symbols must have an associated address, but there are some symbols that are tied to a context or constant value instead.
- 4: Inverse is: Lexical Scope Symbol defines Data Symbol
- 5: Inverse is: Namespace contains Data Symbol
- 12: Inverse is: Import defines DLL
- 13: Inverse is: Export defines DLL
- 17: Inverse is: Function calledBy Function
- 18: Inverse is: Class defines Function
- 19: Inverse is: Namespace contains Function
- 24: Inverse is: Namespace contains Class