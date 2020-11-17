# SYSC5500-project
This is the term project for SYSC5500 (Designing Secure Networking and Computer Systems) at Carleton University for the Fall 2020 semester. The main goal of the project is to model the Mirai botnet based on the behavior described in two papers [[1](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf), [2](https://ieeexplore.ieee.org/document/8170867)] and observe how different factors in a network of IoT devices affect botnet propagation.

## Contributors
- Alvi Jawad
- Luke Newton 

## Repository Structure
- the **project-proposal** folder contains our original project proposal and associated files
- the **progress-presentation** folder contains the progress presentation delivered halfway through the project, along with a snapshot of the model and data analysis at the time of the presentation
- **Mirai_botnet_0.9.xml** is our Timed Automata based model of the Mirai botnet for use in [UPPAAL](http://www.uppaal.org/)
- **botnet-model<span></span>-ideas.md** contains a list of what data is interesting to collect from the model, and possible extensions to the project
- **Slide_Format_DarkRED.pptx** is the formatting for the slides of the progress and final presentations

## References
1. M. Antonakakis, T. April, M. Bailey, M. Bernhard, E. Bursztein, J. Cochran, Z. Durumeric, J. A. Halderman, L. Invernizzi, M. Kallitsis, D. Kumar, C. Lever, Z. Ma, J. Mason, D. Menscher, C. Seaman, N.
Sullivan, K. Thomas, and Y. Zhou, “[Understanding the mirai botnet](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf),” in 26th USENIX Security Symposium (USENIX Security 17), (Vancouver, BC), pp. 1093–1110, USENIX Association, Aug. 2017
2. G. Kambourakis, C. Kolias and A. Stavrou, "[The Mirai botnet and the IoT Zombie Armies](https://ieeexplore.ieee.org/document/8170867)," MILCOM 2017 - 2017 IEEE Military Communications Conference (MILCOM), Baltimore, MD, 2017,
pp. 267-272, doi: 10.1109/MILCOM.2017.8170867.