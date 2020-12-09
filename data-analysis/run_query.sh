# ------------------------------------------------------------
#             Step 1: set simulation parameters
# ------------------------------------------------------------
NUMBER_DEVICES=100

#proportions should sum to one, this is checked in the python script
PROPORTION_ALWAYS_ON=1
PROPORTION_PERIODIC_REBOOT=0

# these values are only relevant for devices that reboot periodically
REBOOT_LENGTH=600
REBOOT_PERIOD=36000

NUMBER_CREDENTIALS=62

SIMULATION_TIME=1000
SIMULATION_RUNS=1

STOP_WHEN_ALL_INFECTED=false

# ------------------------------------------------------------
#             Step 2: edit model files and run simulation 
#     (do not change this if you're just running simulations!)
# ------------------------------------------------------------

# for whatever reason, the verifier wont run with the given name
# this is solved by creating a copy with a new name
MODEL_NAME='model.xml'
OLD_NAME=''
for f in *.xml
do 
	OLD_NAME=$f
	cp "$f" $MODEL_NAME 
done

#call the python helper file to edit model system declaration
python set_num_devices.py $NUMBER_DEVICES $PROPORTION_ALWAYS_ON $PROPORTION_PERIODIC_REBOOT $REBOOT_LENGTH $REBOOT_PERIOD $NUMBER_CREDENTIALS $MODEL_NAME

for query in *.q
do 
	#create a copy of the query and edit parameters
	QUERY_NAME='query.q'
	cp $query $QUERY_NAME 
	sed -i "s/\[total_time<=[0-9]\+; [0-9]\+\]/\[total_time<=$SIMULATION_TIME; $SIMULATION_RUNS\]/" $QUERY_NAME
	if [ "$STOP_WHEN_ALL_INFECTED" = true ] ; then
		echo ' : current_number_bots==total_devices-1' >> $QUERY_NAME
	fi

	#make a folder to move all output CSVs, along with a copy of the model and query used
	OUTPUT_FOLDER=$(echo $query | cut -d'.' -f 1)-$(date "+%Y.%m.%d-%H.%M.%S")
	mkdir -p $OUTPUT_FOLDER
	cp $MODEL_NAME $OUTPUT_FOLDER
	cp $QUERY_NAME $OUTPUT_FOLDER

	#run the verifier query
	./verifier/verifyta.exe -H 29 -S 2 -O csv $MODEL_NAME $QUERY_NAME
	
	#move results to result folder
	mv **.csv $OUTPUT_FOLDER
	rm *.plot
	rm $QUERY_NAME
done

#remove the created model file (copies exist in the result folders)
rm $MODEL_NAME
