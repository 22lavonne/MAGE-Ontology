# A Knowledge Graph for the Detection of Malware Behavior in Executables
Departmental Honors Thesis under Dr. Cogan Shimizu based on the intersection between Knowledge Graphs and Cyber Security.

## About
This knowledge graph is based on the symbol table in Ghidra with the goal of assisting reverse engineers in detecting malicious behavior in executable files. The ontology takes the output of a decompiled file analyzed in Ghidra to encode the knowledge graph of said file to provide a graphical representation of the data connections of the file. The knowledge graph can be queried to detect malicious behavior in the file to determine if the executable is malware.

## Resources:
* [Documentation](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/documentation): contains useful documentation of the project like key notions and the list of competency questions along with their associated queries.
* [Schema](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/schema): contains a .graphml file of the schema, and images of the individual modules of the schema (used in key-notions)
* [Ontology](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/ontology): contains the Turtle file of the ontology.
* [Ghidra Scripting](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/ghidra-scripting): contains any scripts used to extract the data for the knowledge graph (writen in Pyghidra).
* [Queries](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/queries): contains a SPARQL file containing all the queries used in the project. Also contains CSV files containing the results of these queries when ran on a knowledge graph materialized from data of a malicious executable file.
* [Honors Blitz](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/honors-blitz): contains the resources and presentation used for the Wright State 2026 Honors Blitz competition.
* [DHT Final Presentation](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/DHT-presentation): Contains the final powerpoint presentation presented in front of the committe for my undergraduate departmental honors thesis.