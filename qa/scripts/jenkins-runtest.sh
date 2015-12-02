#!/usr/bin/env bash

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

python qa/tests/tests.py
EXIT_STATUS=$?

kill $PID

exit $EXIT_STATUS
