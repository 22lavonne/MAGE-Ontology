## List of Axioms

Not including subClassOf relations <br>

## new table
| #     | Subject           | Relationship          | Object            | Symbolic Notation     |
| ----- | ----------------- | --------------------- | ----------------- | -----------------     |
| 1     | Symbol            | hasReference          | Reference         |                       |
| 2     | Symbol            | hasPrimaryReference   | Reference         |                       |
| 3     | Symbol            | hasAddress            | Address           |                       |
| 4     | Label             | definedIn             | Namespace Symbol  |                       |
| 5     | Function          | definedIn             | Namespace Symbol  |                       | 
| 6     | Class             | definedIn             | Namespace         |                       |
| 7     | DLL               | definedIn             | Namespace         |                       |
| 8     | Reference         | hasSourceAddress      | Address           |                       |
| 9     | Reference         | hasDestinationAddress | Address           |                       |
| 10    | Reference         | hasReferenceType      | xsd:string        |                       |
| 11    | Reference         | hasOperandIndex       | xsd:integer       |                       |
| 12    | Variable          | hasDataType           | xsd:string        |                       |
| 13    | Parameter         | passesInto            | Function          |                       |
| 14    | Function          | defines               | Local Variable    |                       |
| 15    | Function          | hasReturnType         | xsd:string        |                       |
| 16    | Function          | returns               | Parameter         |                       |
| 17    | Function          | calls                 | Function          |                       |
| 18    | Function          | definedIn             | Namespace Symbol  |                       |
| 19    | Function          | containsInstruction   | Instruction       |                       |
| 20    | Function          | hasName               | xsd:string        |                       |
| 21    | Instruction       | hasOpcode             | xsd:string        |                       |
| 22    | Instruction       | hasSourceOperand      | Operand           |                       |
| 23    | Instruction       | hasDestinationOperand | Operand           |                       |
| 24    | Instruction       | atAddress             | Address           |                       |
| 25    | Operand           | hasOperandType        | xsd:string        |                       |
| 26    | Operand           | hasOperandValue       | xsd:string        |                       |


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