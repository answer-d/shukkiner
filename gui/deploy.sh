#!/bin/bash

aws s3 sync --delete dist/ s3://yama-shukkiner-gui
