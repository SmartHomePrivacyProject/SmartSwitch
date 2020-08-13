#!/usr/bin/env bash

for m in mi
do
  for b in 0.25
  do 
    for eps in 0.0005
    do
      for r in 8.0 
      do
	python3 edit_file.py "$b" "$m" "$r" "$eps" 0.05
	nnictl create --config ./config.yml
        echo bin: "$b", method: "$m", ratio: "$r", eps: "$eps"
        sleep 2h
        nnictl stop
        fuser -k 8080/tcp
        sleep 3
      done
    done
  done
done
