# Preliminary Results and Data Analysis
This folder the data and analysis for the preliminary results discussed in the progress presentation.

## File Breakdown
- **Mirai_botnet_progress_presentation_snapshot.xml** is the botnet model that was used to gather the data for the progress presentation
#### Data
- **total_scans.txt** contains data points for 100 simulation runs, where each each data point is a simulation time followed by the number of network scans that had been performed by that time in the simulation
- **total_attack_attempts.txt** contains data points for 100 simulation runs, where each each data point is a simulation time followed by the number of login attempts that had occurred by that time in the simulation
- **total_messages.txt** contains data points for 100 simulation runs, where each each data point is a simulation time followed by the number of messages that had been sent by that time in the simulation
- **botnet1times.txt, botnet2times.txt, botnet3times.txt, botnet4times.txt, and botnet5times.txt** each contain data points for 100 simulation runs. Each data point specifies a time and whether or not a specific device is part of the botnet (0 for uninfected, 1 for infected). The device the data points are for is indicated by the file name (botnet1times is for device 1, botnet2times is for device 2, etc.). This data is used to determine when devices are expected to be infected.
#### Analysis
- **preliminary-results.xlsx** contains that data and graphing for expected botnet size change over time, and messages sent through the network.
- **pairwise_kolmogorov_smirnov_test.py** reads in all the botnet*x*times.txt files the performs a KS test on every pair of devices to determine is their infection times are drawn from the same sample (indicating that it does not matter which devices are infected first)
- **expectation_from_UPPAAL_output.py** parses the UPPAAL graph csv format to generate an expected value and confidence interval. The file parsing looks for the last data point in each simulation run to generate expectation, so this should only be used when you are graphing totals and want to know the expected total value over many runs