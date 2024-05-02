#!/bin/bash

download_single_doc() {
    local doc="$1"
    local doc_id=$(grep 'doc_id' "$doc" | sed -n 's/.*"doc_id":"\([^"]*\)".*/\1/p')
    local text_file="content/$(basename "${doc%.*}").tex"

    echo "Downloading $doc to $text_file"
    curl -s "https://docs.google.com/document/d/${doc_id}/export?format=txt" -L -o "$text_file"
}

download_docs_in_dir() {
    local docs_path="$1"
    for doc in "$docs_path"/*.gdoc; do
        if [ -f "$doc" ]; then
            download_single_doc "$doc"
        fi
    done
}

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_google_docs_directory_or_filename>"
    exit 1
fi

INPUT="$1"

if [ -d "$INPUT" ]; then
    mkdir -p content
    download_docs_in_dir "$INPUT"
elif [ -f "$INPUT" ]; then
    mkdir -p content
    download_single_doc "$INPUT"
else
    echo "The input '$INPUT' is neither a valid directory nor a valid file."
    exit 1
fi
