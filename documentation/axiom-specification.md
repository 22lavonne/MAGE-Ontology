## List of Axioms

| #     | Subject       | Relationship          | Object        |
| ----- | ------------- | -----------------     | -----------   |
| 1     | Symbol        | hasReference          | Reference     |
| 2     | Symbol        | hasPrimaryReference   | Reference     |
| 3     | Symbol        | associatedWith        | Address       |
| 4     | Data Symbol   | subClassOF            | Symbol        |
| 5     | Lexical Scope Symbol   | subClassOf   | Symbol        |
| 6     | Namespace     | subClassOf            | Symbol        |
| 7     | Data Symbol   | definedIn             | Lexical Scope Symbol |
| 8     | Data Symbol   | definedIn             | Namespace     |
| 9     | Lexical Scope Symbol    | definedIn   | Namespace     |
| 10    | Reference     | hasSourceAddress      | Address       |
| 11    | Reference     | hasDestinationAddress | Address       |
| 12    | Reference     | hasType               | xsd:string    |
| 13    | Reference     | hasOperandIndex       | xds:integer   |
| 14    | Address       | pointsTo              | Symbol        |
| 15    | Address       | addressOf             | xsd:string    |
| 16    | Address       | performsRole          | Operand       |
| 17    | Import        | subClassOf            | Lexical Scope Symbol  |
| 18    | Export        | subClassOf            | Lexical Scope Symbol  |
| 19    | Import        | declares              | DLL           |
| 20    | Export        | declares              | DLL           |
| 21    | Import        | hasLabel              | Label         |
| 22    | Export        | hasLabel              | Label         |
| 23    | Function      | subClassOf            | Lexical Scope Symbol  |
| 24    | Function      | hasLabel              | Label         |
| 25    | Function      | hasReturnType         | DataType      |
| 26    | Function      | returns               | Variable      |
| 27    | Function      | hasParameter          | Variable      |
| 28    | Function      | calls                 | Function      |
| 29    | Function      | calledBy              | Function      |
| 30    | Function      | definedIn             | Class         |
| 31    | Function      | containsInstruction   | Instruction   |
| 32    | Class         | subClassOf            | Lexical Scope Symbol  |
| 33    | Class         | definesFunction       | Function      |
| 34    | Class         | hasLabel              | Label         |
| 35    | Variable      | subClassOf            | Data Symbol   |
| 36    | Variable      | hasLabel              | Label         |
| 37    | Variable      | passesInParameter     | Function      |
| 38    | Variable      | hasDataType           | Datatype      |
| 39    | Label         | subClassOf            | Data Symbol   |
| 40    | Label         | hasName               | xsd:string    |
| 41    | Label         | hasAddress            | Address       |
| 42    | Label         | modified              | xsd:boolean   |
| 43    | Data Type     | hasDataTypeName       | xsd:string    |
| 44    | Namespace     | subClassOf            | Symbol        |
| 45    | Namespace     | hasName               | xsd:string    |
| 46    | Instruction   | hasOpcode             | Opcode        |
| 47    | Instruction   | hasSourceOperand      | Operand       |
| 48    | Instruction   | hasDestinationOperand | Operand       |
| 49    | Address       | performsRole          | Operand       |
| 50    | Register      | performsRole          | Operand       |
| 51    | ImmediateOperand  | performsRole      | Operand       |
| 52    | Symbol        | performsRole          | Operand       |



## Axiom Selection

### Symbol, Address, and Reference

|                                           | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| ---------                                 |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Range                                     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped range                              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Existential                               |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse existential                       |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Functionality                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Qualified functionality                   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Qualified scoped functionality            |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Structural tautology                      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|                                           |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| For the Property                          |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Asymmetry                                 |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Transitivity                              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Irreflexivity                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

### Import, Export, Function, and Class

|                                           | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| ---------                                 |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Range                                     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped range                              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Existential                               |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse existential                       |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Functionality                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Qualified functionality                   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Qualified scoped functionality            |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Structural tautology                      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|                                           |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Asymmetry                                 |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Transitivity                              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Irreflexivity                             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

### Variable, Label, and Data Type

|                                           | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 
| ---------                                 |----|----|----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |    |    |    |    |
| Range                                     |    |    |    |    |    |    |    |    |    |
| Scoped range                              |    |    |    |    |    |    |    |    |    |
| Existential                               |    |    |    |    |    |    |    |    |    |
| Inverse existential                       |    |    |    |    |    |    |    |    |    |
| Functionality                             |    |    |    |    |    |    |    |    |    |
| Qualified functionality                   |    |    |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |    |    |
| Qualified scoped functionality            |    |    |    |    |    |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    |    |
| Structural tautology                      |    |    |    |    |    |    |    |    |    |
|                                           |    |    |    |    |    |    |    |    |    |
| For the Property                          |    |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |    |
| Asymmetry                                 |    |    |    |    |    |    |    |    |    |
| Transitivity                              |    |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |    |    |
| irreflexivity                             |    |    |    |    |    |    |    |    |    |


### Namespace and Instruction

|                                           | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 
| ---------                                 |----|----|----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |    |    |    |    |
| Range                                     |    |    |    |    |    |    |    |    |    |
| Scoped range                              |    |    |    |    |    |    |    |    |    |
| Existential                               |    |    |    |    |    |    |    |    |    |
| Inverse existential                       |    |    |    |    |    |    |    |    |    |
| Functionality                             |    |    |    |    |    |    |    |    |    |
| Qualified functionality                   |    |    |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |    |    |
| Qualified scoped functionality            |    |    |    |    |    |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    |    |
| Structural tautology                      |    |    |    |    |    |    |    |    |    |
|                                           |    |    |    |    |    |    |    |    |    |
| For the Property                          |    |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |    |
| Asymmetry                                 |    |    |    |    |    |    |    |    |    |
| Transitivity                              |    |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |    |    |
| irreflexivity                             |    |    |    |    |    |    |    |    |    |