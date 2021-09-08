set terminal epscairo
set output '500_devices_with_1_peiodicaly_rebooting_every_3000_time_units_2021-09-02_12:06:18.591917/model-fixed-speed.xml-q0.eps'
set title 'Simulations (1)'
set key outside center right enhanced Left reverse samplen 1
set grid xtics ytics lc rgb '#808080'
set xlabel 'time'
set ylabel 'value'
set style data points
set datafile separator ','
plot '500_devices_with_1_peiodicaly_rebooting_every_3000_time_units_2021-09-02_12:06:18.591917/model-fixed-speed.xml-q0-e0.csv' with lines lc rgb '#ff0000' title 'current_number_bots',\
	'500_devices_with_1_peiodicaly_rebooting_every_3000_time_units_2021-09-02_12:06:18.591917/model-fixed-speed.xml-q0-e1.csv' with lines lc rgb '#00ffff' title '2*((attempt_loops+scan_loops)*LIMIT+total_attempts+total_scans)'
