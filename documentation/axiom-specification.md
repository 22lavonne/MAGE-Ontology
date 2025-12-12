## List of Axioms

### Key:
* LSS: Lexical Scope Symbol


| #     | Subject       | Relationship          | Object        |
| ----- | ------------- | -----------------     | -----------   |
|   1   |Symbol         |hasReference           |Reference      |
|   2   |Symbol         |hasPrimaryReference    |Reference      |
|   3   |Symbol         |associatedWith         |Address        |
|   4   |Data Symbol    |definedIn              |LSS            |
|   5   |Data Symbol    |definedIn              |Namespace      |
|   6   |Reference      |hasSourceAddress       |Address        |
|   7   |Reference      |hasDestinationAddress  |Address        |
|   8   |Reference      |hasType                |xsd:string     |
|   9   |Reference      |hasOperandIndex        |xsd:integer    |
|  10   |Address        |addressOf              |xsd:string     |
|  11   |Address        |performsRole           |Operand        |
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


| Rel | CD  | D   | SD  | R   | SR  | E   | IE  | F   | QF  | SF  | QSF | IF  | IQF | ISF | IQSF| ST  | SY  |TRANS| REF |Notes|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|2    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|3    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|4    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|5    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|6    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|7    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|8    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|9    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|10   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|11   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|12   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|13   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|14   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|15   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|16   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|17   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|18   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|19   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|20   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|21   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|22   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|23   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|24   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|25   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|26   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|27   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|28   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|29   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|30   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|31   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|32   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|33   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|34   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|35   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |