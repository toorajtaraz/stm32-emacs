#!/bin/bash
usage() {
  echo "USAGE stm32prj_init [PATH TO PROJECT]";
}

project_path=$1
[[ $# -ne 1 ]] && usage && exit 1;
[[ ${#project_path} -eq 0 ]] && usage && exit 1;

#Check if the provided path exists
[[ ! -d "$project_path" ]] && echo "This project does not exists!" && exit 2;

cd "${project_path}/Debug"
NUMCPUS=`grep -c '^processor' /proc/cpuinfo`
eval "make clean"
eval "bear -- make -j$NUMCPUS"
cp ./compile_commands.json ../
cd ..

python $HOME/.doom.d/stm32/correct_cdb.py "${project_path}/compile_commands.json"
