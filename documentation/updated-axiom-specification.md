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
| 18    | Instruction       | hasOpcode             | Opcode            |
| 19    | Instruction       | hasSourceOperand      | Operand           |
| 20    | Instruction       | hasDestinationOperand | Operand           |
| 21    | Address           | performsRole          | Operand           |
| 22    | Register          | performsRole          | Operand           |
| 23    | ImmediateOperand  | performsRole          | Operand           |
| 24    | Dynamic           | performsRole          | Operand           |
| 25    | Scalar            | performsRole          | Operand           |


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
|  1  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  2  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  3  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  4  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  5  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  6  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  7  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  8  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|  9  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 10  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 11  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 12  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 13  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 14  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 15  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 16  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 17  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 18  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 19  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 20  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 21  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 22  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 23  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 24  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 25  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
