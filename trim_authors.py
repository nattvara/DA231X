"""
This script will trim the author entry of references with an absurd amount of authors.

The latex template doesn't handle that well and produce a silly amount of authors in the bibliography.

Usage:

python trim_authors.py
"""

import re

def trim_authors(bib_content):
    bib_entries = bib_content.split('@')
    processed_entries = []

    for entry in bib_entries:
        if not entry.strip():
            continue
        if "author" in entry.lower():
            author_line_match = re.search(r'\bauthor\s*=\s*{(.+?)}', entry, re.IGNORECASE | re.DOTALL)
            if author_line_match:
                authors = author_line_match.group(1)
                authors_list = authors.split(' and ')
                if any("team" in author.lower() for author in authors_list) and len(authors_list) > 10:
                    team_term = next((author for author in authors_list if "team" in author.lower()), None)
                    if team_term:
                        authors_list = [author for author in authors_list if "team" not in author.lower()]
                        reduced_authors = ' and '.join([team_term] + authors_list[:9])  # Adjust to include team_term in the 10
                    else:
                        reduced_authors = ' and '.join(authors_list[:10])
                    modified_authors = re.sub(r'{(.+?)}', '{' + reduced_authors + '}', author_line_match.group(0))
                    entry = entry.replace(author_line_match.group(0), modified_authors)
        processed_entries.append(entry)

    return '@' + '@'.join(processed_entries)

bib_file_path = 'references.bib'
with open(bib_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

trimmed_content = trim_authors(content)

with open(bib_file_path, 'w', encoding='utf-8') as file:
    file.write(trimmed_content)

print("Bib file has been updated with trimmed author lists.")
