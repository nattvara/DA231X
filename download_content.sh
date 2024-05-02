#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_google_docs_content>"
    exit 1
fi

DOCS_PATH="$1"

if [ ! -d "$DOCS_PATH" ]; then
    echo "The directory '$DOCS_PATH' does not exist."
    exit 1
fi

download_docs() {
    for doc in "$DOCS_PATH"/*.gdoc; do
        if [ -f "$doc" ]; then
            doc_id=$(grep 'doc_id' "$doc" | sed -n 's/.*"doc_id":"\([^"]*\)".*/\1/p')
            text_file="content/$(basename "${doc%.*}").tex"

            echo "Downloading $doc to $text_file"
            curl -s "https://docs.google.com/document/d/${doc_id}/export?format=txt" -L -o "$text_file"
        fi
    done
}

mkdir -p content
download_docs
