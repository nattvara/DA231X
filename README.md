# DA231X Report

For the compiled report see [main.pdf](main.pdf).

## Build the latex project

Clone the repo

```bash
git clone git@github.com:nattvara/DA231X.git && cd DA231X
```

Link the content

```bash
ln -s [PATH TO CONTENT IN GOOGLE DRIVE] google_docs_content
```

build the report

```bash
make
```

## Commands

Only download the new contnet

```bash
make download
```

Only compile the latex

```bash
make compile
```
