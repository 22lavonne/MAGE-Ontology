<!--     
TODO:
For all the relations assigned as functionality, determine if they are
- Qualified Functionality
- Scoped functionality
- Qualified scoped functionality
- inverse functionality
- inverse qualified functionality
- inverse scoped functionality
- inverse qualified scoped
-->

## List of Axioms

| #     | Subject       | Relationship          | Object        |
| ----- | ------------- | -----------------     | -----------   |
| 1     | Symbol        | hasReference          | Reference     |
| 2     | Symbol        | hasPrimaryReference   | Reference     |
| 3     | Reference     | hasSourceAddress      | Address       |
| 4     | Reference     | hasDestinationAddress | Address       |
| 5     | Reference     | hasType               | xsd:string    |
| 6     | Reference     | hasOperandIndex       | xds:integer   |
| 7     | Address       | pointsTo              | Symbol        |
| 8     | Address       | addressOf             | xsd:string    |
| 9     | Import        | subClassOf            | Symbol        |
| 10    | Export        | subClassOf            | Symbol        |
| 11    | Import        | declares              | DLL           |
| 12    | Export        | declares              | DLL           |
| 13    | Import        | hasLabel              | Label         |
| 14    | Export        | hasLabel              | Label         |
| 15    | Function      | subClassOf            | Symbol        |
| 16    | Function      | hasLabel              | Label         |
| 17    | Function      | hasReturnType         | DataType      |
| 18    | Function      | returns               | Variable      |
| 19    | Function      | declaresLocalVariable | Variable      |
| 20    | Function      | hasParameter          | Variable      |
| 21    | Function      | calls                 | Function      |
| 22    | Function      | calledBy              | Function      |
| 23    | Function      | definedIn             | Class         |
| 24    | Function      | definedIn             | Namespace     |
| 25    | Function      | containsInstruction   | Instruction   |
| 26    | Variable      | subClassOf            | Symbol        |
| 27    | Variable      | definedIn             | Namespace     |
| 28    | Variable      | definedInGlobalNamespace  | Namespace |
| 29    | Variable      | localVariableDefinedIn    | Class     |
| 30    | Variable      | hasLabel              | Label         |
| 31    | Variable      | hasDataType           | Datatype      |
| 32    | Data Type     | hasDataTypeName       | xsd:string    |
| 33    | Class         | subClassOf            | Symbol        |
| 34    | Class         | definesFunction       | Function      |
| 35    | Class         | hasLabel              | Label         |
| 36    | Class         | definesLocalVariable  | Variable      |
| 37    | Class         | definedIn             | Namespace     |
| 38    | Label         | subClassOf            | Symbol        |
| 39    | Label         | hasName               | xsd:string    |
| 40    | Label         | hasAddress            | Address       |
| 41    | Namespace     | subClassOf            | Symbol        |
| 42    | Namespace     | declares              | Symbol        |
| 43    | Symbol        | declaredBy            | Namespace     |
| 44    | Namespace     | hasName               | xsd:string    |
| 45    | Instruction   | hasOpcode             | Opcode        |
| 46    | Instruction   | hasSourceOperand      | Operand       |
| 47    | Instruction   | hasDestinationOperand | Operand       |
| 48    | Address       | performsRole          | Operand       |
| 49    | Register      | performsRole          | Operand       |
| 50    | ImmediateOperand  | performsRole      | Operand       |
| 51    | Symbol        | performsRole          | Operand       |



## Axiom Selection

### Symbol, Reference, and Address

|                                           | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 
| ---------                                 |----|----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |
| Domain                                    |    |    |    |    | ?  | ?  |    | x  |
| Scoped domain                             |    |    |    |    |    |    | ?  |    |
| Range                                     | x  | x  | x  | x  |    |    |    |    |
| Scoped range                              | ?  | ?  | ?  | ?  |    |    | ?  |    |
| Existential                               |    |    | x  | x  | ?  | ?  |    |    |
| Inverse existential                       | x  | x  |    |    |    |    |    |    |
| Functionality                             |    | x  | x  | x  | x  | x  | x  | x  |
| Qualified functionality                   |    |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    | x  | x  |    | x  |
| Qualified scoped functionality            |    | x  | x  | x  |    |    | x  |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    |
| Structural tautology                      | x  | x  | ?  | ?  |    |    | x  | x  |
|                                           |    |    |    |    |    |    |    |    |
| For the Property                          |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  | x  | x  | x  |

### Import and Export

|                                           | 9  | 10 | 11 | 12 | 13 | 14 | 
| ---------                                 |----|----|----|----|----|----|
| Subclass                                  | x  | x  |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |    |
| Range                                     |    |    |    |    | x  | x  |
| Scoped range                              |    |    | x  | x  | ?  | ?  |
| Existential                               |    |    |    |    | x  | x  |
| Inverse existential                       |    |    |    |    |    |    |
| Functionality                             |    |    |    |    | x  | x  |
| Qualified functionality                   |    |    |    |    | x  | x  |
| Scoped functionality                      |    |    |    |    |    |    |
| Qualified scoped functionality            |    |    |    |    | ?  | ?  |
| Inverse functionality                     |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |
| Structural tautology                      |    |    | x  | x  | x  | x  |
|                                           |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  | x  |


### Function

|                                           | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| ---------                                 |----|----|----|----|----|----|----|----|----|----|----|
| Subclass                                  | x  |    |    |    |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |    |    |    |    |  
| Domain                                    |    |    | ?  | ?  | ?  | ?  | ?  | ?  |    |    |    |
| Scoped domain                             |    |    | ?  | ?  | ?  | ?  | ?  | ?  |    |    |    |
| Range                                     |    | x  | x  | x  | x  | x  | ?  | ?  |    |    | x  |
| Scoped range                              |    | ?  |    |    | ?  | ?  | ?  | ?  |    |    | ?  |
| Existential                               |    | x  |    |    |    |    |    |    |    |    | x  |
| Inverse existential                       |    |    |    |    |    |    |    |    |    |    |    |
| Functionality                             |    | x  | x  | x  |    |    |    |    | x  |    |    |
| Qualified functionality                   |    | x  | x  | x  |    |    |    |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |    |    |    |    |
| Qualified scoped functionality            |    | ?  | ?  | ?  |    |    |    |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |    | ?  |    |    |
| Structural tautology                      |    | x  | x  | x  |    |    | x  | x  | x  | x  | x  |
|                                           |    |    |    |    |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  | x  | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    | x  | x  |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  | x  |    |    | x  | x  | x  |

### Variable and Data Type

|                                           | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
| ---------                                 |----|----|----|----|----|----|----|
| Subclass                                  | x  |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |
| Domain                                    |    |    |    | x  |    | ?  | x  |
| Scoped domain                             |    |    |    | ?  |    | ?  |    |
| Range                                     |    |    | x  |    | x  | x  |    |
| Scoped range                              |    | x  | ?  |    | ?  |    |    |
| Existential                               |    |    |    |    | x  |    | ?  |
| Inverse existential                       |    |    |    |    |    |    |    |
| Functionality                             |    |    | x  |    | x  | x  | x  |
| Qualified functionality                   |    |    | x  |    | x  | x  |    |
| Scoped functionality                      |    |    |    |    |    |    | x  |
| Qualified scoped functionality            |    |    | ?  |    | ?  | ?  |    |
| Inverse functionality                     |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |
| Structural tautology                      |    | x  | x  | x  | x  | x  |    |
|                                           |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  | x  | x  |

### Class
|                                           | 33 | 34 | 35 | 36 | 37 |
| ---------                                 |----|----|----|----|----|
| Subclass                                  | x  |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |
| Domain                                    |    |    |    |    |    |
| Scoped domain                             |    |    |    |    |    |
| Range                                     |    | x  | x  | x  |    |
| Scoped range                              |    | ?  | ?  | ?  | x  |
| Existential                               |    |    | x  |    |    |
| Inverse existential                       |    |    |    |    |    |
| Functionality                             |    |    | x  |    |    |
| Qualified functionality                   |    |    | x  |    |    |
| Scoped functionality                      |    |    |    |    |    |
| Qualified scoped functionality            |    |    | ?  |    |    |
| Inverse functionality                     |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |
| Structural tautology                      |    | x  | x  | x  | x  |
|                                           |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  |

### Label
|                                           | 38 | 39 | 40 |
| ---------                                 |----|----|----|
| Subclass                                  | x  |    |    |
| Class disjointness                        |    |    |    |
| Domain                                    |    |    |    |
| Scoped domain                             |    |    |    |
| Range                                     |    |    | x  |
| Scoped range                              |    |    |    |
| Existential                               |    | ?  | x  |
| Inverse existential                       |    |    |    |
| Functionality                             |    |    | x  |
| Qualified functionality                   |    |    | x  |
| Scoped functionality                      |    |    |    |
| Qualified scoped functionality            |    |    | ?  |
| Inverse functionality                     |    |    |    |
| Inverse qualified functionality           |    |    |    |
| Inverse scoped functionality              |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |
| Structural tautology                      |    |    | x  |
|                                           |    |    |    |
| Symmetry                                  |    |    |    |
| Asymmetry                                 | x  | x  | x  |
| Transitivity                              |    |    |    |
| Reflexivity                               |    |    |    |
| irreflexivity                             | x  | x  | x  |

### Namespace
|                                           | 41 | 42 | 43 | 44 |
| ---------                                 |----|----|----|----|
| Subclass                                  | x  |    |    |    |
| Class disjointness                        |    |    |    |    |
| Domain                                    |    |    | ?  |    |
| Scoped domain                             |    |    | x  |    |
| Range                                     |    |    | ?  |    |
| Scoped range                              |    | x  | x  |    |
| Existential                               |    |    |    | ?  |
| Inverse existential                       |    |    |    |    |
| Functionality                             |    |    |    | x  |
| Qualified functionality                   |    |    |    |    |
| Scoped functionality                      |    |    |    | x  |
| Qualified scoped functionality            |    |    |    |    |
| Inverse functionality                     |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |
| Structural tautology                      |    | x  | x  |    |
|                                           |    |    |    |    |
| Symmetry                                  |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |
| Reflexivity                               |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  |

### Instruction

|                                           | 45 | 46 | 47 | 48 | 49 | 50 | 51 |
| ---------                                 |----|----|----|----|----|----|----|
| Subclass                                  |    |    |    |    |    |    |    |
| Class disjointness                        |    |    |    |    |    |    |    |
| Domain                                    | x  | x  | x  |    |    |    |    |
| Scoped domain                             | ?  | ?  | ?  |    |    |    |    |
| Range                                     | x  | x  | x  | x  | x  | x  | x  |
| Scoped range                              | ?  | ?  | ?  | ?  | ?  | ?  | ?  |
| Existential                               | x  |    |    |    |    |    |    |
| Inverse existential                       | ?  |    |    |    |    |    |    |
| Functionality                             | x  |    | x  |    |    |    |    |
| Qualified functionality                   | x  |    | x  |    |    |    |    |
| Scoped functionality                      |    |    |    |    |    |    |    |
| Qualified scoped functionality            | ?  |    | ?  |    |    |    |    |
| Inverse functionality                     |    |    |    |    |    |    |    |
| Inverse qualified functionality           |    |    |    |    |    |    |    |
| Inverse scoped functionality              |    |    |    |    |    |    |    |
| Inverse qualified scoped functionality    |    |    |    |    |    |    |    |
| Structural tautology                      | x  | x  | x  | x  | x  | x  | x  |
|                                           |    |    |    |    |    |    |    |
| Symmetry                                  |    |    |    |    |    |    |    |
| Asymmetry                                 | x  | x  | x  | x  | x  | x  | x  |
| Transitivity                              |    |    |    |    |    |    |    |
| Reflexivity                               |    |    |    |    |    |    |    |
| irreflexivity                             | x  | x  | x  | x  | x  | x  | x  |