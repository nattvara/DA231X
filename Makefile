.PHONY: all download compile clean

DOCS_PATH=./content

all: download compile

download:
	./download_content.sh $(DOCS_PATH)

compile:
	./compile_latex.sh

clean:
	@git clean -fdX
