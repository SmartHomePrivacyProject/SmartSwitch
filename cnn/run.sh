#!/usr/bin/env bash

for m in jmim mi
do
  for b in 0.25
  do 
      for r in 20 
      do
	python3 edit_file.py "$b" "$m" "$r"
	nnictl create --config ./config.yml
        echo bin: "$b", method: "$m"
        sleep 4h
        nnictl stop
        fuser -k 8080/tcp
        sleep 3
      done
  done
done
