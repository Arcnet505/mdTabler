#!/user/bin/env python3 -tt
"""
Tool for converting copied tables to Markdown table format
"""

# Imports
import argparse
from pathlib import Path

# Formats
jira_headers = "||{}||"
jira_body = "|{}|"
md_table = "| {} |"

# Function declarations
def parse_table(infile, delimeter, outfile, jira):
    table = []

    with open(infile, 'r') as f:
        headers = True
        for line in f:
            if headers:
                line = line.strip()
                if jira:
                    table += jira_headers.format(line.replace(delimeter, '||'))
                else:
                    table(md_table.format(line.replace(delimeter, ' | ')))
                    columns = line.count(delimeter) + 1
                    table += '| --- ' * columns + '|'
                headers = False
            else:
                line = line.strip()
                if jira:
                    table += jira_body.format(line.replace(delimeter, '|'))
                else:
                    table += md_table.format(line.replace(delimeter, ' | '))
            

def pargs():
    # Parse CLI arguments
    global verbose

    parser = argparse.ArgumentParser(description="Tool for converting copied tables to markdown format")
    parser.add_argument('-i', '--input', required=True, help="The input file to read in.")
    parser.add_argument('-d', '--delimeter', required=True, help="The delimeter of the copied table. Format: $'delimeter', e.g. $' \\t'")
    parser.add_argument('-o', '--output', help="The file to output the markdown table to.")
    parser.add_argument('-j', '--jira', action='store_true',  help="Convert the table to Jira markdown format.")
    args = parser.parse_args()

    infile = args.input
    delimeter = args.delimeter
    outfile = args.output
    jira = args.jira
    
    tmp = Path(infile)

    if not tmp.exists():
        print("Error: ", infile, "VM not found")
        exit(1)

    if tmp.is_dir():
        print("Error: ", infile, "is a directory")
        exit(2)

    # TODO: Check if outfile exists and do not overwrite

    return infile, delimeter, outfile, jira

def main():
    infile, delimeter, outfile, jira = pargs()

    parse_table(infile, delimeter, outfile, jira)

# Main body
if __name__ == '__main__':
    main()
