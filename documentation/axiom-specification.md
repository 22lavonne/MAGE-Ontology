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
| 8     | Reference         | hasType               | xsd:string        |
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
| 19    | Instruction       | hasOpcode             | Opcode            |
| 20    | Instruction       | hasSourceOperand      | Operand           |
| 21    | Instruction       | hasDestinationOperand | Operand           |
| 22    | Instruction       | atAddress             | Address           |
| 23    | Operand           | hasType               | xsd:string        |
| 24    | Operand           | hasValue              | xsd:string        |


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
|  6  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  7  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  8  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
|  9  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 10  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 11  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 12  |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 13  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 14  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |  x  |
| 15  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 16  |     |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 17  |     |  x  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |  x  |  x  |     |     |     |
| 18  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 19  |     |  x  |     |  x  |     |  x  |  x  |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 20  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 21  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 22  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 23  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 24  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |