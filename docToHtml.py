"""Convert MarkDown notation file to HTML file 
   specifically for xaviercollantes.me schema
"""

__author__ = "Xavier Collantes"

import os
import logging


def converter(file_md):
  """
    file_md: Markdown notated file.
    
    Returns: File object of input file. 

    Raises: File not found.
  """  
  
  if not os.path.exists(file_md):
    raise FileNotFoundError

  out_filename = os.path.split(file_md)[-1].split('.')[-2] + '.html'
  
  # Open Output file
  with open(out_filename, 'w+') as out_file:
    print('Writing to file: %s' % out_filename)
	  
	# Open Markdown file
    with open(file_md, 'r') as md:

      for line in md:
        line = line.strip()  # Remove newline character
        if len(line)is not 0:  # Check for then skip empty lines
          print(len(line))
          line = line.strip()
          line = line.split()
        
          rules_header(line, out_file)
          #rules_style(line, out_file)
        else:
          print('empty line')

      print('EOF: %s' % out_filename)    


def rules_style(line, out_file):
  """Translate Bold, Italics, Underline notation.
  """
  b_flag = False
  i_flag = False
  u_flag = False




def rules_header(line, out_file):
  """
    text: Line in file. 
	out_file: Output file to write append to.
  """
  print(line)
  out_file.write('<h1>{}</h1>\n'.format(''.join(line[1:]))) if line[0] == '#' else 0
  out_file.write('<h2>{}</h2>\n'.format(''.join(line[1:]))) if line[0] == '##' else 0
  out_file.write('<h3>{}</h3>\n'.format(''.join(line[1:]))) if line[0] == '###' else 0
  out_file.write('<h4>{}</h4>\n'.format(''.join(line[1:]))) if line[0] == '####' else 0



def rules_links(line, out_file):
  """Construct <a> tag from links.
  """
  for element in line:
    if element == '<a':
      out_file.write()	

    


converter('target.md')
