#!/bin/bash -x

if [ ! -d ../virtualenv ]; then
    virtualenv ../virtualenv
fi

. ../virtualenv/bin/activate

pip install -r qa/requirements.txt

npm install
if [ $? -ne 0 ]; then
    exit 1
fi

node index.js &
PID=$!
sleep 1
if [ `ps -efw | grep -v grep | grep -c $PID` -ne 1 ];then
    exit 1
fi

python qa/LiarsDiceQA/TestRunner.py
EXIT_STATUS=$?

kill $PID

exit $EXIT_STATUS
