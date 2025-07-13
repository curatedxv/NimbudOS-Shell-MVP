#!/bin/bash
docker build -t nimbus-chrome .
docker run -d -p 9222:9222 --name nimbus-browser nimbus-chrome
