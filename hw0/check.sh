#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Wrong Format"
	echo "You should type: bash ./check.sh [program_filename]."
	exit
elif [[ ! -f $1 ]]; then
	echo "The program does not exist."
	exit
fi

program=$1
n_tests=4
n_pass=0
testdata_dir=./testdata

echo 
echo "== My own test for HW0 =="

for((i=1;i<=${n_tests};i++)); do
	tmpFile=${testdata_dir}/tmp_${i}.out
	correctFile=${testdata_dir}/${i}.out
	dataIn=${testdata_dir}/${i}.in
	
	python3 ${program} < ${dataIn} > ${tmpFile}
	res=$(diff ${tmpFile} ${correctFile})
	
	if [[ -n ${res} ]]
	then
		echo "testcase #${i} failed"
		echo "${res}"
	else
		echo "testcase #${i} passed"
		n_pass=$((${n_pass}+1))
	fi
done

echo -n "$ "
if [[ ${n_pass} == ${n_tests} ]]; then
	echo "All testcases passed!!"
else
	echo "Only ${n_pass}/${n_tests} testcases passed..."
fi