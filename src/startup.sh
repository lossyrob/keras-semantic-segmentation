#!/bin/bash

set -e

echo "Copy the NVidia drivers from the parent (because nvidia-docker-plugin doesn't work with ECS agent)"
find /hostusr -name "*nvidia*" -o -name "*cuda*" -o -name "*GL*" | while read path
do
  newpath="/usr${path#/hostusr}"
  mkdir -p `dirname $newpath` && \
    cp -a $path $newpath
done

cp -ar /hostlib/modules /lib

echo "/usr/lib64" > /etc/ld.so.conf.d/nvidia.conf
ldconfig

echo "Starting your essential task"
exec /bin/bash
