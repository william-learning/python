#!/usr/bin/env bash
git init
git add .
git commit -m "Commit Message"
git remote add origin https://github.com/williamsoftwarecode/python.git
git remote set-url https://github.com/williamsoftwarecode/python.git
git pull origin master --allow-unrelated-histories
git push origin master