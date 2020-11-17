//This file was generated from (Academic) UPPAAL 4.1.24 (rev. 29A3ECA4E5FB0808), November 2019

/*

*/
//NO_QUERY

/*

*/
<----- MODEL VERIFICATION ----->

/*
Deadlocks never occur
*/
A[] !deadlock

/*
A deadlock implies that all devices have been infected
*/
A[] deadlock imply current_number_bots==total_devices-1

/*

*/
//NO_QUERY

/*

*/
<----- INFECTION REACHABILITY ----->

/*
All devices will always be infected in every possible scenario
*/
A<> current_number_bots==total_devices-1

/*
It is possible for every device to eventually be infected
*/
E<> current_number_bots==total_devices-1

/*

*/
//NO_QUERY

/*

*/
<----- INFECTION TIMES ----->

/*
All devices are always infected by 50 time units
*/
A[] total_time==50 imply current_number_bots==total_devices-1

/*
The probability all devices are compromised in 100 time units
*/
Pr[total_time<=100; 100] (<>current_number_bots==total_devices-1)

/*
The probability all devices are compromised in 50 time units
*/
Pr[total_time<=50] (<>current_number_bots==total_devices-1)

/*
The probability all devices are compromised in 25 time units
*/
Pr[total_time<=25] (<>current_number_bots==total_devices-1)

/*
The expected number of compromised devices in 10 time units (generated with 100 simulation runs)
*/
E [total_time<=10; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 20 time units (generated with 100 simulation runs)
*/
E [total_time<=20; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 25 time units (generated with 100 simulation runs)
*/
E [total_time<=25; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 30 time units (generated with 100 simulation runs)
*/
E [total_time<=30; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 40 time units (generated with 100 simulation runs)
*/
E [total_time<=40; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 50 time units (generated with 100 simulation runs)
*/
E [total_time<=50; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 60 time units (generated with 100 simulation runs)
*/
E [total_time<=60; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 70 time units (generated with 100 simulation runs)
*/
E [total_time<=70; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 80 time units (generated with 100 simulation runs)
*/
E [total_time<=80; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 90 time units (generated with 100 simulation runs)
*/
E [total_time<=90; 100] (max: current_number_bots)

/*
The expected number of compromised devices in 100 time units (generated with 100 simulation runs)
*/
E [total_time<=100; 100] (max: current_number_bots)

/*
The probability bot 1 has been infected by 50 time units
*/
Pr[<=50] (<>in_botnet[1])

/*
The probability bot 2 has been infected by 50 time units
*/
Pr[<=50] (<>in_botnet[2])

/*
The probability bot 3 has been infected by 50 time units
*/
Pr[<=50] (<>in_botnet[3])

/*
The probability bot 4 has been infected by 50 time units
*/
Pr[<=50] (<>in_botnet[4])

/*
The probability bot 5 has been infected by 50 time units
*/
Pr[<=50] (<>in_botnet[5])

/*
The probability bot 1 has been infected by 25 time units
*/
Pr[<=25] (<>in_botnet[1])

/*
The probability bots 1 and 2 have been infected by 25 time units
*/
Pr[<=25] (<>in_botnet[1] && in_botnet[2])

/*
The probability bots 1, 2 , and 3 have been infected by 25 time units
*/
Pr[<=25] (<>in_botnet[1] && in_botnet[2] && in_botnet[3])

/*
simulate 100 runs for 100 time units each and plot the number of infected bots against simulation time
*/
simulate [total_time<=100; 100] {current_number_bots}

/*
simulate 100 runs for 100 time units each and plot when each bot becomes infected
*/
simulate [total_time<=100; 100] {in_botnet[1], in_botnet[2], in_botnet[3], in_botnet[4], in_botnet[5]}

/*

*/
//NO_QUERY

/*

*/
<----- Network Traffic ----->

/*
Probability that at least 75 messages are sent over the network in 32 time units (which is the expected time the infect all 5 devices)
*/
Pr[<=32] (<> total_messages>75)

/*
Simulate 100 runs for either 100 time units, or until every bot is infected, and plot the number of network scans and login attempts
*/
simulate [total_time<=100; 100] {total_scans, total_attempts} : current_number_bots==total_devices-1

/*
Simulate 100 runs for either 100 time units, or until every bot is infected, and plot the number of messages sent over the network
*/
simulate [total_time<=100; 100] {total_messages} : current_number_bots==total_devices-1

/*

*/
//NO_QUERY
