This folder contains the scalability testing done on linux VM

## contents
- **results** contains the results of running several simulations with different model parameters
- **verifier** contains the version of UPPAAL's verifier used to obtain our simulation results
- **model-fixed-speed.xml** is the version of the model with a fixed speed network
- **model-variable-speed-.xml** is the version of the model with a variable speed network
- **run_query.py** is a python script used to run one experiemnt with a set of parameters defined at the top of the script
- **run_queries.py** is a python script used to run multiple experiemnts with parameters for each defined in a list of dictionaries
- **set_num_devices.py** is a python file containing the functionality to edit the model xml files with desired parameters. This does NOT start a simulation with those parameters

## suggested workflow
1. type 'gedit run_query.py' and edit parameters at the top of the file as needed
2. type 'python3 run_query.py' to run the simulation

A timestamped folder is created with the simulation results

## reading results
Each simulation run with **run_query.py** or **run_queries.py** creates a folder with a name describing the parameters set and a timestamp for when the simulation began. Each folder contains:
- **sim_time**: contains the numbers of seconds the simulation took to complete
- **query.q**: contains the query executed on the model with UPPAAL's verifier
- **model.xml**: contains the botnet model on which the query was run
- **model.xml-q0-e0.csv**: contains information for the number of devices in the botnet at any given time
- **model.xml-q0-e1.csv**: contains the total number of messages passed around the system at any given time
- **model.xml-q0-e0.plot**: is the plot information that UPPAAL generates from the csv files