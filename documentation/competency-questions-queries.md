## Competency Questions and Queries

### Can the ontology detect malicious API calls within the executable?
* Query goal: detecting persistant API calls and other suspicious API calls <br>
```
SELECT ?f ?fname ?cname
WHERE {

    ?f ontology:calls ?api .
    ?f ontology:hasName ?fname .
    ?api ontology:hasName ?cname .

    FILTER regex(?cname,
      "system|execve|popen",
      "i")
}
```

```
SELECT DISTINCT ?f ?fname ?cname
WHERE {

    ?f ontology:calls ?api .
    ?f ontology:hasName ?fname .
    ?api ontology:hasName ?cname .

    FILTER regex(?cname,
      "process_vm_writev|fork|clone",
      "i")
}
```

### Is there any suspicious networking activity within the executable?
* Query goal: search for api calls that are often used in networking activity<br>
```
SELECT ?f ?fname ?name
WHERE {

    ?f ontology:calls ?api .
    ?f ontology:hasName ?fname .
    ?api ontology:hasName ?name .

    FILTER regex(?name,
      "socket|connect|send|recv|sendto|recvfrom",
      "i")
}
```
### Are there any indirect control flow patterns in the executable file indicating vulnerable code?
* Query goal: find instructions with a jump or call opcode, with the destination operand being a register to detect indirect control flow <br>
```
SELECT ?instr ?opcode ?reg
WHERE {

    ?instr ontology:hasOpcode ?opcode ;
           ontology:hasDestinationOperand ?op .

    ?op ontology:hasOperandType "REGISTER" ;
        ontology:hasOperandValue ?reg .

    FILTER (?opcode IN ("JMP","CALL"))
}
```
### Can sections of entropy be detected through the ratio of unique opcodes and total number of instructions in a function?
* Query goal: return a ratio of total instructions in a function to how many unique opcodes are used, since the more unique opcodes there are, the more entropy there usually is.
```
SELECT ?function 
    (COUNT(DISTINCT ?opcode) AS ?uniqueOpcodes) 
    (COUNT(?instruction) AS ?totalInstructions)
    ((COUNT(DISTINCT ?opcode) * 1.0 / COUNT(?instruction)) AS ?diversityRatio)

WHERE {
    ?function ontology:containsInstruction ?instruction .
    ?instruction ontology:hasOpcode ?opcode .
}
GROUP BY ?function
HAVING (?totalInstructions > 10)
ORDER BY DESC(?diversityRatio)
```
### Can patterns of self referential decode loops be found to detect data obfuscation?
* Query goal: looks for functions that contain both a transformation opcode and a loop/branch opcode, which can indicate self referencial decode loops, which can be a sign of data obfuscation.
```
SELECT ?function (COUNT(?inst) AS ?totalRelevantInst)
WHERE {
  ?function ontology:containsInstruction ?inst .
  ?inst ontology:hasOpcode ?opcode .
  
  BIND(LCASE(STR(?opcode)) AS ?opStr)
  
  # ensure the function has at least one TRANSFORMATION opcode
  FILTER EXISTS {
    ?function ontology:containsInstruction ?i_trans .
    ?i_trans ontology:hasOpcode ?op_trans .
    FILTER(?op_trans IN ("XOR", "ADD", "SUB", "ROR", "ROL", "NOT"))
  }
  
  # ensure the same function has at least one LOOP/BRANCH opcode
  FILTER EXISTS {
    ?function ontology:containsInstruction ?i_loop .
    ?i_loop ontology:hasOpcode ?op_loop .
    FILTER(?op_loop IN ("JNZ", "JZ", "JMP", "LOOP"))
  }

  # only count the instructions that match our overall 'suspicious' list
  FILTER(?opcode IN ("XOR", "ADD", "SUB", "ROR", "ROL", "NOT", "JNZ", "JZ", "JMP", "LOOP"))
}
GROUP BY ?function
HAVING (COUNT(?inst) >= 2) 
ORDER BY DESC(?totalRelevantInst)
```
### Can the ontology detect anti VM behavior from the executable?
* Query goal: Detect API calls and instruction opcodes that indicate anti VM behavior
```
SELECT ?f
WHERE {

    ?f ontology:calls ?api .
    ?api ontology:hasName ?name .

    FILTER regex(?name,"ptrace","i")
}
```
```
SELECT ?func ?instr
WHERE {
    ?func ontology:containsInstruction ?instr .
    ?instr a ontology:Instruction ;
           ontology:hasOpcode "CPUID" .
}
```
### Does the executable perform unauthorized system privilege escalation?
* Query goal: look for API calls that indicate privilege escalation
```
SELECT ?f ?name
WHERE {

    ?f ontology:calls ?api .
    ?api ontology:hasName ?name .

    FILTER regex(?name,
      "setuid|setgid|capset|prctl",
      "i")
}
```
### Are there command and control indicators in the executable file?
* Query goal: search for indicators for c2c like hard coded ip addresses, domain names, and urls
```
SELECT ?f ?value
WHERE {

    ?f ontology:calls ?api .
    ?api ontology:hasName ?name .

    FILTER regex(?name,"socket|connect|send|recv","i")

    ?f ontology:containsInstruction ?i .
    ?i ontology:hasSourceOperand ?op .
    ?op ontology:hasOperandValue ?value .

    FILTER regex(?value,"http|\\.(com|net|org)","i")
}
```
### Is there cryptographic activity within the executable, that can indicate encryption to hide parts of the program?
* Query goals: 
  * Get the number of XOR opcodes from a function, where large numbers can indicate custom encryption algorithms
  * Detecting API calls to encryption libraries
  * Detecting patterns in loops that often indicate custom encryption routines
```
SELECT ?f (COUNT(?xor) AS ?xorCount)
WHERE {
    ?f a ontology:Function ;
       ontology:containsInstruction ?xor .

    ?xor ontology:hasOpcode "XOR" .
}
GROUP BY ?f
HAVING (?xorCount > 10)
ORDER BY DESC(?xorCount)
```
```
SELECT ?f ?name
WHERE {

    ?f ontology:calls ?api .
    ?api ontology:hasName ?name .

    FILTER regex(?name,
      "aes|sha|md5|evp",
      "i")
}
```
```
SELECT ?f (COUNT(?instr) AS ?bitwiseOps)
WHERE {

    ?f ontology:containsInstruction ?instr .
    ?instr ontology:hasOpcode ?op .

    FILTER (?op IN ("XOR","ROL","ROR","SHL","SHR","AND","OR"))
}
GROUP BY ?f
HAVING (?bitwiseOps > 30)
ORDER BY DESC(?bitwiseOps)
```
### What percentage of the functions in the binary file are imported (are external)?
* Query goal: Get the percentage of functions that have the parent namespace as a DLL, or are external.
```
SELECT 
  ?totalFunctions
  ?externalFunctions
#   gets percentage based on the numbers returned from external functions and total functions
  (((?externalFunctions * 1.0) / ?totalFunctions) * 100 AS ?percentage)
#   where those numbers are returned from this sub query
WHERE {
  {
    SELECT 
    # get the count of how many functions are defined in, with the parent name containing EXTERNAL 
    # (indicating it's from a dll)
      (COUNT(?f) AS ?totalFunctions)
      (SUM(IF(CONTAINS(STR(?dll), "EXTERNAL"), 1, 0)) AS ?externalFunctions)
    WHERE {
        ?f a ontology:Function .
        ?f ontology:definedIn ?dll .
    }
  }
}
```