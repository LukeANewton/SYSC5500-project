##  Mirai & Mirai variants
* Mirai [Crebs/OVH - Sep 16, Dyn - Oct 16]
* Persirai [April 17]
* --> port 7547 [Nov 16]
* --> us college [Feb 17]
* --> bitcoin mining [Mar 17]
​
## Other IoT botnets
* --> Lua PL [Aug 16]
* Hajime [Counters Mirai - Oct 16]
* BrickerBot [PDoS - Apr 17]
​
​
## 1. Botnets and IoT Security
* A July 2014 report on IoT device security by HP ...
* IDS Analysis likely occurs at a __gateway device__ due to insufficient resources in IoT Devices
​
## 2. DDoS in the IoT - Mirai and the other botnets
* Typically, the CnC server communicates with other parts of the infrastructure through the anonymous __TOR__ network.
* As soon as the __Mirai binary__ is executed, it immediately attempts to protect itself from other malwares by shutting down points of intrusion such as telnet and SSH services.
* Mirai almost always leaves some kind of footprints, detectable through basic network analysis.
* newer bots are stealthier
* hard to stop botnet infection even with frequent rebooting
IoT Devices:
* Usually don't sleep
* have weak protection
* poor maintenance
* can generate huge amounts of attack traffic
* infection rarely requires user interaction
​
## 3. Mirai n Hajime Modeling and Simulation petri nets [Japan]
* Mirai and Hajime only exists in the __dynamic memory__ and disappears when rebooting devices! [US-CERT]
* Hajime: Higher stealth capabilties than Mirai, but no DDoS capabilities
* Hajime has peer-to-peer capabilities
* Hajime __blocks ports__ that Mirai uses to infect a device
* When Hajime affects a device, Mirai cannot affect it
* Reboot removes both Mirai and Hajime...the device can be __reinfected!__
*** The authors propose to use Hajime as a vaccine to IoT botnets such as Mirai
*** perform a cost-performance analysis of removing Mirai using 1. Reboot, 2. Hajime + Reboot (both temporary solutions)
​
## 4. Botnet of things - a survey
Botnet terminologies:
* Botmaster, bot herder, zombies, zombie army
* Covert channel - a secret communication channel that is not allowed by the security policy.
* Internet Relay Chat (IRC) - an application layer protocol that facilitates communication in the form of text
* Scrumping - stealing of computer resources due to being part of a botnet
Botnet Structures;
* Classical centralized [one Central CnC server]
* Decentralized [no CnC, each bot seeks a commander using some upstream query mechanism]
	* infected hosts/bots temporarily play the role of a commander
	* can easily change the CnC backbone
	* most are based on P2P technology
* Locomotive [has a constantly moving structure]
	* Conficker uses P2P+constantly changing DNS names
​
## 6. Mirai and IoT Zombie armies
* Vendors ship their devices with active remote admin capabilities (telnet, SSH), but they are undocumented.
* Linux is not suitable, safer to use a lighter OS such as RIOT, ARMs MbedOS (high security)
* Firmware update is cumbersome as it requires physical access and is vendor/model specific.
* Most affected IoT devices were using Busybox
	* Busybox packs a stripped down version of many Linux utilities into a small executable with a focus on embedded OSs having very limited resources
* Mirai Avoids a hardcoded list of IP addresses (likely to avoid US govt. attention)
* The original version attacks the Telnet port 23, and oncein every 10 attempts, the TCP port 2323
* After infection, performs memory scraping and kills all processes that use SSH, Telnet, and HTTP ports
* To avoid detection, sometimes "self-deletes" itself, but the process continues to run in memory
* Neither Mirai, nor Hajime, reset the password of a device after infection
*** Hajime secretly installs a backdoor on a infected device! 
​
​
# Project Ideas
​
## No Implementation:
### Idea 1: A Comparative Analysis of Mirai and Hajime
### Idea 2: A Comprehensive Impact Analysis of the Mirai botnet and its Variants [focus on the last 4 years]
​
## Implementation-oriented:
### Idea 1: Modeling and Simulation of Mirai and Hajime.
### Idea 2: Say something!
​
what
why
how???
​
__Fill in the Docs_
​
​
IF:
# Comparative Analysis
​
Questions:
* How much impact can botnets create on a network?
* Is there a way to characterize the impact?
* Can we classify botnets and their impacts?
* What can be used to detect/prevent botnet infection? are the techniques viable? what is the confidence in those techniques?
​
* Can we accumulate enough information to recommend a set of steps or actions to secure our networks?
* Can we combine __Secure Design Principles__ with our research results to provide more conclusive recommendations?
​
* Is there a way to build our IoT devices using the recommended steps?
* How can we ensure/promote security by-design in IoT? (a necessity)
​
​
Research Focus:
1. A comparative impact analysis of the Mirai botnet and its variants and botnets that followed after Mirai
	* Impact on the network
	* Impact on organizations
	* The Overall damage done
	*** with adequate information, it is also possible to do a botnet categorization [Centralized, decentralized, locomotive, etc.]
​
2. Will also include an analysis of recent research done on both the detection and prevention mechanism of botnets 
This will include a criticism of:
	* the degree of confidence in their use
	* feasibility of the methods in a practical scenario
	* limitations/downsides of the methods
​
3. Provide recommendations for implementing security measures to prevent the infection and dissemination of botnets
	* By combining methods from the analyzed prevention and detection mechnisms 
	* with the secure design principles
	*** focus: primarily on the security by-design approach [security should be built-in, not added after]
*** 4. Plan to take a look at IoT OSs???
​
​
Research Materials to be used:
* Recently published research papers [these are peer-reviewed and is the most authentic source of information]
* Publicly available security reports from reputed organizations [info about some of the more recent/less known botnets might not be enough]
​
Possible addition of information/shift in focus:
* Discussions in class
* Discussions with the professor for guidance
​
​
​
​
​
​
IF:
# Modeling and Simulation
Why Modeling and Simulation?
* Ethical considerations prevent us from performing attacks on actual networks and collecting data
Modeling and Simulation and subsequent experiments:
	* Allow us to use both of our specializations and interests
		* Discrete Event Modeling and Simulation
		* Data Science specialization
	* Allow us to review relevant literature, as well as to learn new ideas and put them into practice which will assist us in the long run in our __JOURNEY to a masters degree!__.
​
## Possible Tools:
UPPAAL
OMNET++
GNS3
​
## Simulation Ideas:
Possible simulation scenarios:
* All devices connected to the network at start
* Devices connected sporadically
* Devices turn off and on randomly, needs to reconnect to the network to get reinfected
* Users/vendors patch their devices, can no longer be infected
​
Extension:
* Add another botmaster who now fights the previous one for supremacy
* Inlcuding a peer-to-peer (e.g., Haijme) bot to the network and see the changes
*** Trying different topologies
​
Adding a DDoS target:
* All bots attack the target immediately upon being compromised
* Bots only atatck the target when there are no other bots to infect
* Bots only start attacking when the botmaster issues a different "Perform DDoS" command
​
​
Analysis Questions:
* All bots in the network can be successfully infected in varying scenarios
* How many bots are infected after a certain time? Do all simulations give consistent infection results?
* Is it 100%? [is there a way to reduce the infection rate?]
​
Possible Outcomes:
* The Impact of bot attacks are immediately realized/takes time
* Possible Impacts:
	* Bot attacks take the system offline
	* Bot attacks delay the transmission
	* Delay the transmission to a point where __traffic intensity__ is close to 1, results in almost infinite delay