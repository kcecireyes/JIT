JIT
===

Jit is a programming language for journalists.

Compiler Usage
=============
**./jit_cli.py**  
Open the JIT interpreter.

**./jit_cli.py -f programs/program3.txt**  
Run the program in the file provided.


Architecture Overview
=====================

* **cli** or **test** calls the **interpreter**

    * **interpreter** calls the **parser**

        * **parser** calls the **lexer**

            * **lexer** returns lexemes

        * **parser** creates and returns an **ast**

    * **interpreter** calls the **interpreter** on the sub-nodes, and executes current **ast** node

* **cli** prints sucess, or **test** checks output