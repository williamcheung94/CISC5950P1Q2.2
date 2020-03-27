#!/bin/bash
name=$1
#for i in {1..10}
#do
#if (($i==1)); then
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-test/project1/NBA/data/NBA1_6/input
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-test/project1/NBA/data/NBA1_6/output
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/NBA/data/NBA1_6/input
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal -p shot_logs.csv /mapreduce-test/project1/NBA/data/NBA1_6/input
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /mapreduce-test/project1/NBA/data/mapper1a.py -mapper "/mapreduce-test/project1/NBA/data/mapper1a.py $name" \
-file /mapreduce-test/project1/NBA/data/reducer1a.py -reducer /mapreduce-test/project1/NBA/data/reducer1a.py \
-input /mapreduce-test/project1/NBA/data/NBA1_6/input* -output  /mapreduce-test/project1/NBA/data/NBA1_6/output
/usr/local/hadoop/bin/hdfs dfs -cat /mapreduce-test/project1/NBA/data/NBA1_6/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-test/project1/NBA/data/NBA1_6/input
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-test/project1/NBA/data/NBA1_6/output
../../../stop.sh
#fi
#done
