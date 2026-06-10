## List of Axioms

Not including subClassOf relations <br>

## new table
| #     | Subject           | Relationship          | Object            | Description Logic Syntax      |
| ----- | ----------------- | --------------------- | ----------------- | ----------------------------- |
| 1     | Symbol            | hasReference          | Reference         | Symbol ⊑ ∀hasReference.Reference |
| 2     | Symbol            | hasPrimaryReference   | Reference         | Symbol ⊑ ≤1 hasPrimaryReference.Reference |
| 3     | Symbol            | hasAddress            | Address           | Symbol ⊑ ≤1 hasAddress.Address |
| 4     | Label             | definedIn             | Structural Namespace Symbol | Label ⊑ ≤1 definedIn.StructuralNamespaceSymbol  |
| 5     | Class             | definedIn             | Namespace         | Class ⊑ ≤1 definedIn.Namespace |
| 6     | DLL               | definedIn             | Namespace         | DLL ⊑ ≤1 definedIn.Namespace   |
| 7     | Reference         | hasSourceAddress      | Address           | Reference ⊑ ≤1 hasSourceAddress.Address |
| 8     | Reference         | hasDestinationAddress | Address           | Reference ⊑ ≤1 hasDestinationAddress.AddressAddress |
| 9     | Reference         | hasReferenceType      | xsd:string        | Reference ⊑ ≤1 hasReferenceType.xsd:string |
| 10    | Reference         | hasOperandIndex       | xsd:integer       | Reference ⊑ ≤1 hasOperandIndex.xsd:integer |
| 11    | Variable          | hasDataType           | xsd:string        | Variable ⊑ ∀hasDataType.xsd:string |
| 12    | Parameter         | passesInto            | Function          | Parameter ⊑ ∀passesInto.Function |
| 13    | Function          | defines               | Local Variable    | Function ⊑ ∀defines.LocalVariable |
| 14    | Function          | hasReturnType         | xsd:string        | Function ⊑ ≤1 hasReturnType.xsd:string |
| 15    | Function          | returns               | Parameter         | Function ⊑ ≤1 returns.Parameter |
| 16    | Function          | calls                 | Function          | Function ⊑ ∀calls.Function    |
| 17    | Function          | definedIn             | StructuralNamespaceSymbol  | Function ⊑ ≤1 definedIn.StructuralNamespaceSymbol |
| 18    | Function          | containsInstruction   | Instruction       | Function ⊑ ∀containsInstruction.Instruction|
| 19    | Function          | hasName               | xsd:string        | Function ⊑ ≤1 hasName.xsd:string |
| 20    | Instruction       | hasOpcode             | xsd:string        | Instruction ⊑ ≤1 hasOpcode.xsd:string |
| 21    | Instruction       | hasSourceOperand      | Operand           | Instruction ⊑ ∀hasSourceOperand.Operand |
| 22    | Instruction       | hasDestinationOperand | Operand           | Instruction ⊑ ≤1 hasDestinationOperand.Operand |
| 23    | Instruction       | atAddress             | Address           | Instruction ⊑ ≤1 atAddress.Address |
| 24    | Operand           | hasOperandType        | xsd:string        | Operand ⊑ ≤1 hasOperandType.xsd:string |
| 25    | Operand           | hasOperandValue       | xsd:string        | Operand ⊑ ≤1 hasOperandValue.xsd:string |


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
|  7  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
|  8  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 9   |     |  x  |     |     |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 10  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 11  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 12  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 13  |     |     |  x  |     |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 14  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 15  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 16  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 17  |     |     |  x  |     |  x  |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 18  |     |  x  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |  x  |  x  |     |     |     |
| 19  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 20  |     |  x  |     |     |     |  x  |  x  |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 21  |     |  x  |     |  x  |     |     |     |     |     |     |     |     |     |     |     |  x  |     |     |     |
| 22  |     |  x  |     |  x  |     |     |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 23  |     |  x  |     |  x  |     |  x  |     |     |     |     |  x  |     |     |     |     |  x  |     |     |     |
| 24  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |
| 25  |     |  x  |     |     |     |     |     |     |     |     |  x  |     |     |     |     |     |     |     |     |