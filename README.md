![alt text](http://openjdk.java.net/projects/mlvm/images/helicopter.png)

# renaissanceCI
This is a Continious integration framework base on simplicity of two design paterns and the readability of python.


## Chain of responsibility pattern.
Every pipeline can be discribed like a sequence of steps. Every step is agnostic to its previous or its next.

## Command pattern.
Each time something happens to the chain we must be able to revert the process or replay it.

## Android state system
In android we have states that an application can be found. Starting, Running, Paused, Resuming, Exiting.

## Why python?
it is readable, more flexible than yaml. Also it is widely used by the system administration community.

## Infrastructure management.
At first, the goal is to have this project run on docker. Then it will be useful to add different infrastracture management frameworks support like hadoop yarn and apache messos.
