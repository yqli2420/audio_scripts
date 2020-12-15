#!/bin/bash

#echo $PWD
src=$1

function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(cat /dev/urandom | head -n 10 | cksum | awk -F ' ' '{print $1}')
    echo $(($num%$max+$min))
}

thread_num=16
[ ! -p tmp ] && mkfifo tmp
exec 9<>tmp

for ((i=0; i<thread_num;i++)); do
  echo 1>&9
done

snrs=(10 15 20)
for f in $(ls $src)
do
(read -u 9)
{
  echo $f
  rnd=$(rand 0 600) #4216后边的音频都是44k,存在问题
  rnd1=$(rand 0 2)
  #na= ${rnd}".wav"
  echo $rnd
  echo ${snrs[${rnd1}]}
  python3 create_mixed_audio_file.py --clean_file data/92spk_cut/${f}  --noise_file data/all_noise_norm/${rnd}.wav --output_mixed_file data/92spk_noise_all/${snrs[${rnd1}]}-${f} --snr ${snrs[${rnd1}]}
  echo 1>&9
} &
done
