## List of Axioms

Not including subClassOf relations <br>

| #     | Subject           | Relationship          | Object            |
| ----- | ----------------- | --------------------- | ----------------- |
| 1     | Symbol            | hasReference          | Reference         |
| 2     | Symbol            | hasPrimaryReference   | Reference         |
| 3     | Symbol            | hasAddress            | Address           |
| 4     | Label             | definedIn             | Namespace Symbol  |
| 5     | Class             | definedIn             | Namespace Symbol  |
| 6     | Reference         | hasSourceAddress      | Address           |
| 7     | Reference         | hasDestinationAddress | Address           |
| 8     | Reference         | hasReferenceType      | xsd:string        |
| 9     | Reference         | hasOperandIndex       | xsd:integer       |
| 10    | Variable          | hasDataType           | Data Type         |
| 11    | Parameter         | passesInto            | Function          |
| 12    | Function          | defines               | Local Variable    |
| 13    | Function          | hasReturnType         | Data Type         |
| 14    | Function          | returns               | Parameter         |
| 15    | Function          | calls                 | Function          |
| 16    | Function          | definedIn             | Namespace Symbol  |
| 17    | Function          | containsInstruction   | Instruction       |
| 18    | Function          | hasName               | xsd:string        |
| 19    | Instruction       | hasOpcode             | xsd:string        |
| 20    | Instruction       | hasSourceOperand      | Operand           |
| 21    | Instruction       | hasDestinationOperand | Operand           |
| 22    | Instruction       | atAddress             | Address           |
| 23    | Operand           | hasOperandType        | xsd:string        |
| 24    | Operand           | hasOperandValue       | xsd:string        |

## new table
| #     | Subject           | Relationship          | Object            |
| ----- | ----------------- | --------------------- | ----------------- |
| 1     | Symbol            | hasReference          | Reference         | 1
| 2     | Symbol            | hasPrimaryReference   | Reference         | 2
| 3     | Symbol            | hasAddress            | Address           | 3
| 4     | Label             | definedIn             | Namespace Symbol  | 4
| 5     | Function          | definedIn             | Namespace Symbol  | 
| 6     | Class             | definedIn             | Namespace         | 5
| 7     | DLL               | definedIn             | Namespace         | 
| 8     | Reference         | hasSourceAddress      | Address           | 6
| 9     | Reference         | hasDestinationAddress | Address           | 7
| 10    | Reference         | hasReferenceType      | xsd:string        | 8
| 11    | Reference         | hasOperandIndex       | xsd:integer       | 9
| 12    | Variable          | hasDataType           | xsd:string        | 10!
| 13    | Parameter         | passesInto            | Function          | 11
| 14    | Function          | defines               | Local Variable    | 12
| 15    | Function          | hasReturnType         | xsd:string        | 13!
| 16    | Function          | returns               | Parameter         | 14
| 17    | Function          | calls                 | Function          | 15
| 18    | Function          | definedIn             | Namespace Symbol  | 16
| 19    | Function          | containsInstruction   | Instruction       | 17
| 20    | Function          | hasName               | xsd:string        | 18
| 21    | Instruction       | hasOpcode             | xsd:string        | 19
| 22    | Instruction       | hasSourceOperand      | Operand           | 20
| 23    | Instruction       | hasDestinationOperand | Operand           | 21
| 24    | Instruction       | atAddress             | Address           | 22
| 25    | Operand           | hasOperandType        | xsd:string        | 23
| 26    | Operand           | hasOperandValue       | xsd:string        | 24


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
|  1  |     |  x  |     |  x  |     |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |
|  2  |     |  x  |     |  x  |     |     |  x  |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  3  |     |  x  |     |  x  |     |     |  x  |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  4  |     |     |  x  |     |     |  x  |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|  5  |     |     |  x  |     |     |  x  |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|  6  |     |     |  x  |     |     |  x  |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|  7  |     |     |  x  |     |     |  x  |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
|  8  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  9  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 10  |     |  x  |     |     |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 11  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 12  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 13  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 14  |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 15  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 16  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 17  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 18  |     |     |  x  |     |  x  |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 19  |     |  x  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |  x  |  x  |     |     |     |
| 20  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 21  |     |  x  |     |     |     |  x  |  x  |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 22  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 23  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 24  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 25  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 26  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |