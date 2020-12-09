# UPPAAL
## Uses
- graphical simulation
- model checking for verification 
- Build a model with timed automata and verify properties on it.

## Timed Automata
- finite state machines with time
- allows bounded discrete variables
    - specified as ````int[lowerBound, upperBound] varName````
    - 32 bit signed
- define constants with ````const````

### Process/Automaton/Template
- a system is comprised of a network of concurrent processes (aka automatons)
    - each process is comprised of locations (aka states)
    - transitions between locations define how the system behaves
        - transitions may have guards and synchronizations
- instantiate templates in system declarations

### Clocks
- clock times are continuous, and progresses globally at same rate
- can only check clock times or reset clocks

### Guards
- transition cannot fire until guard satisfied
- must evaluate to a boolean
- can check clocks, variables, constants, and math with these values

### Synchronization
- extra guards on transitions for communication between automata
- binary synchronization channels specified with ````chan channelName````
    - one automaton must have ````chanName?```` and the other has ````chanName!````
    - both are blocking until there is any pair of ! and ? with the same channel name
- broadcast channels specified with ````broadcast chan channelName````
    - ````a?```` is blocking, ````a!```` is never blocking for broadcasts

### Invariants
- expressions that must be satisfied while in a state
- expressions can reference variables, constants, or clocks
- expressions must evaluate to a boolean

### Updates
- comma separated list of expressions to execute on transition
- expressions can assign values to variable, reset clocks, or call functions

### Urgent synchronization
- edges with urgent synchronizations cannot also have timed guards
- specify channel as urgent with ````urgent```` prefix

### Urgent locations
- state must immediately be left upon entering
    - in UPAALL, this is modelled as time not passing while an urgent state is active

### Committed locations
- like urgent locations, time cannot pass while a committed state is active
- the next transition that fires in the network must be from the committed state

## Timed Computation Tree Logic
- used for model checker queries
- check an expression can possibly eventually hold: ````E<> booleanExpression````
- check an expression will eventually hold ````A<> booleanExpression````
- check an expression can always holds: ````E[] booleanExpression````
    - there is at least one path where the condition is always true
- check an expression will always hold: ````A[] booleanExpression````
    - the condition always holds in every path
- ````expression1 --> expression2``` means that if expression1 holds, expression2 will eventually hold

## What can verifier do?
- test reachability properties
    - can a specific state be reached
- 

    