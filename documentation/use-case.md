<!-- 
Build the Use-case

    1. Fill the Narrative section with a top-level description of your use-case, including references. As a guideline, this section should be about 500 words. This should, at a minimum, answer the questions:
        Who are you supporting?
        What are their goals?
        Why is making a Knowledge Graph interesting -- or important -- for the use-case?
        Why a knowledge graph and not a relational (tabular) database?
    2. Fill the Competency Questions section with no fewer than 10 competency questions. Thoroughly describe your intended interactions and what data will be retrieved to support said interactions.
    3. Fill the Potential Datasets section with links and access dates for no less than five potential datasets.
    Fill the Existing Resources section with any resources (e.g., ontologies, knowledge graphs, or standards) which can be used 4. in the project.
    5. Provide all references in the References section. References should be numbered starting at 1, listed in order of appearance, and otherwise following the IEEE reference style. Ensure that the DOI is included for every reference, where available.

-->

# Use Case
## Narrative
Software reverse engineering is a difficult and tedious process due a lot of the information of the original data (like the names of functions and variables) being lost during the process of disassembly and decompilation. Using reverse engineering software like Ghidra can make this process easier through collecting all the symbols used in a binary file, but these symbols usually don't have their original name (making the process of trying to figure out what they do more difficult). 

My plan is to make a knowledge graph based on the symbol table in Ghidra to help users more easily visualize how all the data from an executable file fits together. Initially, the knowledge graph will just use the data from the symbol table, with the purpose of it being to more easily see how the data from a binary executable fits together. Especially after a user renames some labels for variables or functions, the knowledge graph would make it easier to visualize how the different pieces work together to gain a better overall understanding of how the program executable works.

I also hope to expand the knowledge graph to apply to finding dependency vulnerabilities in a software supply chain. Specifically, connecting malware-specific behavior beyond just one artifact or executable file to detect vulnerabilities within a software supply chain.
<!-- I am not quite sure how I will be able to apply the knowledge graph into detecting vulnerabilities within a software supply chain, but I'll figure that out later and instead currently focus on making a knowledge graph specifically on the symbol table. -->

## Competency Questions
<!--
* Competency Question<br>
Bridges Datasets: dataset 1, dataset 2, ...
* Competency Question<br>
Bridges Datasets: dataset 1, dataset 2, ...
* Competency Question<br>
Bridges Datasets: dataset 1, dataset 2, ...
-->
1. Can the ontology detect malicious persistent API calls within the executable?
2. Is there any suspicious networking activity within the executable?
3. Are there any indirect control flow patterns in the executable file indicating vulnerable code?
4. Can sections of entropy be detected through the ratio of unique opcodes and total number of instructions in a function?
5. Can patterns of self referential decode loops be found to detect data obfuscation?
6. Can the ontology detect file system abuse?
7. Are there any suspicious jumps into memory in the executable?
8. Are there any other suspicious API calles contained in the executable file?
9. Is there cryptographic activity within the executable, that can indicate encryption to hide parts of the program?
10. What percentage of the functions in the binary file are imported (are external)?


<!-- 
How many datasets is appropriate for my scale of KG?
Will just this one github repo with loads of ELF fies be enough?
 -->
## Potential Datasets
* [Benignware and Malware Elf Binaries](https://github.com/nimrodpar/Labeled-Elfs)

## Existing Resources
* [Adapting Linguistic Deception Cues for Malware Detection](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=wright1421025881&disposition=inline)

<!-- ## References -->
<!-- References should follow a consistent format. They should appear in order of appearance in the narrative section. Remove this comment. -->
