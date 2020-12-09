# Problem: how to pick accurate values for clocks on timed automata?
- we want to play with these values to see how the botnet propogation is affected (ie. sensitivity analysis), but we should be starting with accurate values

## Accurate times for the bots
- **Challenge**: IoT devices are heterogeneous, so there are potentially many many types of devices as part of the botnet
    - times will vary because times are related to the computational power, and different devices have different computational power
    - times guards will likely be wide ranges
        - a more accurate model would be able to select a time from a distribution that matches the distribution of devices in the botnet, rather than uniformly random smapling from the range
- **Current UPPAAL bot automaton has times for:**
    - absolute time when the bot becomes active
    - time to scan for open telnet ports
    - time to attempt break in (dictionary attack)
    - also consider later: time device is rebooted
- port scanning and attack times are mainly depended on bot processing time and network delay
- **Method 1** If bot processing time is more important, the solution to finding values for times to scan and attack may lie in estimating **device composition** of the botnet
    - from device composition, estimate processing power, then estimate time for activity
    - [~50 billion IoT devices in 2020](https://www.mdpi.com/1424-8220/18/9/2796/htm)
    - Hajime in 2018: [74.2% of devices were mipseb architecture, another 14.4% were arm](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_02B-3_Herwig_paper.pdf)
    - Mirai in 2016: [KrebsOnSecurity lists the default password combos Mirai tries and links them to a manufacturer/device](https://krebsonsecurity.com/2016/10/who-makes-the-iot-things-under-attack/)
        - 59.3% are for cameras
        - 15.6% are for dvr/tv boxes
        - 3.1% are for speakers
        - 9.3% are for printers
        - 12.5% are for routers
        - a similar table appears in this [2017 paper in USENIX](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf)
- **Method 2**: The alternative is that network delay is more important
    - **rationale**: these activities are actually very simple, network delay may be a much larger part of the time than the actual bot processing time
        - scanning is essentially just trying to initialize TCP connections with a destination
            - send a SYN and wait a bit to see if you get a SYN ACK, rejection, or no response
        - dictionary attacks just iterate through a list of credentials to try and wait for a response
    - average network delay may be good enough

## Accurate times for the C&C infrastructure