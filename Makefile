.PHONY: all download compile clean

DOCS_PATH=./google_docs_content

all: download compile

download:
	./download_content.sh $(DOCS_PATH)

compile:
	./compile_latex.sh

clean:
	./clean.sh
