#### Consideration of IoT structure in mitigation against Mirai malware
- models Mirai infection with agent oriented Petri Net (PN^2)
- Mirai is deleted when device rebooted, but device open to reinfection
- Mirai scans for devices with weak/default passwords
- Hajime infects in similar way to Mirai, but blocks ports after infection to prevent infections by other malware (like Mirai)
- Paper considers Hajime infection and reboots as Mirai conuntermeasures
- Paper considers different network topologies for different protections
- Place a Hajime infected node in your network so you can spread the Mirai protection to other nodes?

#### On Modeling and Simulation of the Behavior of IoT Malwares Mirai and Hajime
- simulate both propogation of Mirai and Hajime with PN^2
- more common reboots means fewer Mirai infections
- do Mirai vs Hajime analysis for fully connected and star topologies
- star topology with Hajime node at center means gives less Mirai than a fully connected network

#### Quantitative Evaluation of Hajime with Secondary Infectivity in Response to Mirai’s Infection Situation
- simulate Mirai and Hajime with PN^2, and different numbers of nodes that start with Mirai/Hajime
- introduce a hypothetical version of Hajime that can infect and replace Mirai
- Without Hajime ability to replace Mirai, network topology is important 
- With Hajime ability to replace Mirai, topology is less important

#### Modelling the Spread of Botnet Malware in IoT-Based Wireless Sensor Networks
- introduces a botnet propogation model based on SIS epidemiological models
- model analysis with Monte-Carlo