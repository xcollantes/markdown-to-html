"""Command-line implementation of MD to HTML reading flags.
"""

__author__ = "Xavier Collantes"


import argparse
from docToHtml import converter

argparser = argparse.ArgumentParser(description='Convert MarkDown notation file to HTML file \
  specifically for xaviercollantes.me schema')
argparser.add_argument('-m', '--md-file', dest='mark_down', default='sample_markdown.md', 
  help='Markdown file to be converted.')
argparser.add_argument('-c', '--class-file', dest='class_config',
  help='In-line HTML class configuration file.')
argparser.add_argument('-t', '--header', dest='header_html',
  help='HTML code prepended to generated code from Markdown.')
argparser.add_argument('-f', '--footer', dest='footer_html',
  help='HTML code appended to generated code from Markdown.')

args = argparser.parse_args()


def main():
  file_to_convert = args.mark_down
  converter(file_to_convert, args.header_html, args.footer_html)


if __name__ == '__main__':
  main()
