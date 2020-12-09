## more realistic scenarios
- faster compute resources
    - cloud/grid rental?
        - (tried colab already, since the script is python, but it does not let me run the verifier.exe)
- alternate operating system for 64 bit system
    - only really affects our ability to use the graphical program
        - rendering graphics is probably what uses all the memory, since the CLI uses very little memory
    - Linux or Mac
        - a VM will not work for this
            - among other things, this will be slower than a native OS
- more reading/experimentation on the CLI might let our simulations be more efficient
    - it seems like a CPU core saturates even with little memory used, so this is a less certain idea
- queue bots-to-be on loader with a realistic timing to upload binary 
- network delay on c&c architecture communication
- we now know that steady state for rebooting and always-connected is reached very quickly, so instead of simulating an entire day/week/month/etc. we can simulate a short part until we get steady state
    - this will allows us to do more simulation runs and get better predictions for expected values
    - we can simulate different events that could impact the botnet size as soon as we reach a steady state, instead of waiting until the actual time they occur
        - eg. imagine a scenario where the network speed is degraded for a short time every week/month
            - instead of simulating the entire week/month up to that point, we can just simulate until we reach steady state (which is very fast), and then immediately simulate the short-term network degradation

## new concepts to simulate
- devices that reboot according to some distribution
    - uniform and exponential distributions are easy to do, but the latter requires an accurate rate of decay parameter
- devices that are online for only a short time and mostly off
    - easily doable with the current model
- devices which have a finite lifetime and may or may not reboot
- patching/new vulnerabilities/change default credentials after reboot 
    - there is a branch on the repository with some preliminary work on this
- events that may have a lasting affect on the botnet
    - loss of power that deactivates all the non-battery devices simultaneously
    - temporary network speed degradation
    - second botnet with similar infection process where infections are mutually exclusive

