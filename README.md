# MAGE-Ontology: An Ontology for Malware Analysis in Ghidra for Executables
Undergraduate and Graduate research under Dr. Cogan Shimizu based on the intersection between Ontologies and Cyber Security.

## About
The MAGE-Ontology provides a structured representation of the disassembly and decompilation of an executable file. It is built upon the reverse engineering tool Ghidra, utilizing Ghidra's API to materialize RDF triples to make a knowledge graph based on an executable file. The ontology is based on the symbol tree in Ghidra, providing structured sub-class and super-clas relations between different symbols and how they interact. SPARQL queries were generated based on the knowledge graphs with the purpose of categorizing malicious behaviors within the executables, with different forms of malicious behavior detected based on the type of malware.

## Resources:
* [Documentation](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/documentation): contains useful documentation of the project, such as key notions, schema digrams, the list of competency questions along with their associated queries, and more.
* [Ontology](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/ontology): contains the Turtle file of the ontology.
* [Ghidra Scripting](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/ghidra-scripting): contains any scripts used to extract the data for the knowledge graph (writen in Pyghidra).
* [Queries](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/queries): contains a SPARQL file containing all the queries used in the project. Also contains CSV files containing the results of these queries when ran on a knowledge graph materialized from data of a malicious executable file.
* [Honors Blitz](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/honors-blitz): contains the resources and presentation used for the Wright State 2026 Honors Blitz competition.
* [DHT Final Presentation](https://github.com/22lavonne/Malware-Behavior-Knowledge-Graph/tree/main/DHT-presentation): Contains the final powerpoint presentation presented in front of the committe for my undergraduate departmental honors thesis.
