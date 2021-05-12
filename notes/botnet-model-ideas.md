# Information to collect
- reachability 
    - will all bots always be infected?
    - will X% of devices always be infected?
- timing
    - will X% of devices always infected within a certain amount of time?
- counting
    - how many messages need to be sent over the network to infect X% of devices?
    - how many login attempts are required to infect X% od devices?
- reinfectivity 
    - if rebooting is allowed (which clears the infection), how many times does a device get infected before X% of devices are infected at once?
- botnet stability
    - with rebooting, we have some rate at which bots are added, and some rate at which bots leave the network. What is the steady state size?

# Situations to consider
- how different amounts of rebooting affects information above
    - none
    - period (every X seconds exactly)
    - random (exponential)
    - what if devices are vulnerable only X% of the time they boot up? (not concrete)
    - rebooting should take some amount of time
- network stability
    - change invariants and guards on clocks to simulate network delay
- password scheme
    - how does having a larger number of potential passwords affect the data above?
- amount of time devices spend propagating botnet (Mirai does not try to hide itself)
    - currently, once infected, all the bot does is propagate
    - if the bot wants to hide, it should only be propagating X% of the time
        - model with longer time delays, or extra states
    - **if the network needs some % required availability, you do not want to have to reboot devices because they will be offline. However, if a certain percentage of time your devices are propagating a botnet instead of doing their work, then you may get more up time in the long run by rebooting now**

# Possible Extensions
- different topologies
    - default is a fully connected network
    - what if you need to infect certain nodes to try and infect others?
        - may be too complicated to model
- second botnet with mutually exclusive infection
    - with rebooting to remove either infection, can one every infect X% of devices at once?

# Issues
- multiple devices might being waiting to download a binary, but only the most recently infected one will get the binary
- model complexity
    - there is an upper limit to how complicated we can make the model and still be able to use some verifier features
    - if we can't use the verifier even after attempting to simplify the model, then we might as make it is complicated as we like and collect all our date through simulation runs
- we need "realistic times" for guards and invariants
    - both aspects of times (processing time and network delay) are hard to estimate
    - if the processing is simple (which it is in most cases), maybe we can focus on network delay only?
    - if network delay is also har to estimate, then what about using time units as something less absolute?
        - eg. one time unit is the time for one message to be sent
            - round trips would then be two time units
        - with this, we can make a more realistic model, but may be limited in what kind of information we collect
            - eg. when selecting larger or smaller times for aspects such as reboot period, we can only specify the relationship between changing values and the new results, not any hard values