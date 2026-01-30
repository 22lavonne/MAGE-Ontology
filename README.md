# A Knowledge Graph for the Detection of Malware Behavior in Executables
Departmental Honors Thesis under Dr. Cogan Shimizu based on the intersection between Knowledge Graphs and Cyber Security.

## About
This knowledge graph is based on the symbol table in Ghidra with the goal of assisting reverse engineers in detecting malicious behavior in executable files. The ontology takes the output of a decompiled file analyzed in Ghidra to encode the knowledge graph of said file to provide a graphical representation of the data connections of the file. The knowledge graph can be queried to detect malicious behavior in the file to determine if the executable is malware.

## Resources:
* [Documentation](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/documentation): contains useful documentation of the project like key notions and an annotated bibliography of works seen during research.
* [Schema](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/Schema): contains a .graphml file of the schema, and images of the individual modules of the schema (used in key-notions)
* [Ontology](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/ontology): contains the Turtle file of the ontology.
* [Ghidra Scripting](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/Ghidra-Scripting): contains any scripts used to extract the data for the knowledge graph (writen in Pyghidra).