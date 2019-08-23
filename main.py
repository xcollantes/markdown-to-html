__author__ = "Xavier Collantes"


import argparse
from docToHtml import converter

argparser = argparse.ArgumentParser(description='Convert MarkDown notation file to HTML file \
  specifically for xaviercollantes.me schema')
argparser.add_argument('-m', '--md-file', dest='mark_down', default='sample_markdown.md', 
  help='Markdown file to be converted.')
argparser.add_argument('-c', '--class-file',
  help='In-line HTML class configuration file.')

args = argparser.parse_args()


def main():
  file_to_convert = args.mark_down
  converter(file_to_convert)


if __name__ == '__main__':
  main()
