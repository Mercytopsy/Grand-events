#!/bin/bash

(
coverage run -p --source='.' tests/raveTest.py;
coverage combine; coverage report; coverage html)