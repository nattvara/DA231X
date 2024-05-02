#!/bin/bash

if [ -L "google_docs_content" ]; then
    mv google_docs_content ..
    symlink_moved=1
else
    symlink_moved=0
fi

git clean -fdX

if [ "$symlink_moved" -eq 1 ]; then
    mv ../google_docs_content .
fi
