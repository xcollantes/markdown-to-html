"""Convert MarkDown notation file to HTML file 
   specifically for xaviercollantes.me schema
"""

__author__ = "Xavier Collantes"

import os
import logging
import re


def converter(file_md):
  """
    file_md: Markdown notated file.
    
    Returns: File object of input file. 

    Raises: File not found.
  """  
  
  if not os.path.exists(file_md):
    raise FileNotFoundError

  out_filename = os.path.split(file_md)[-1].split('.')[-2] + '.html'
  
  flag_ordered_list = False
  flag_unordered_list = False

  # Open Output file
  with open(out_filename, 'w+') as out_file:
    print('Writing to file: %s' % out_filename)
	  
	# Open Markdown file
    with open(file_md, 'r') as md:

      for line in md:
        line = line.strip()  # Remove newline character
        if len(line)is not 0:  # Check for then skip empty lines
          print(len(line))
          #line = line.strip()
          
        
          # Character level parsing
          rules_style(line, out_file)

          parse_line = line.split()
          rules_header(parse_line, out_file)

          rules_links(line, out_file) 
          rules_images(line, out_file)
          #is_list_element(str(line), out_file)
          rules_ordered_lists(line, out_file, flag_ordered_list)
          #rules_p_tag(line, out_file)








        else:
          print('empty line')

      print('EOF: %s' % file_md)


def is_list_element(line, out_file):
  """Determines if line is part of list element.

  This detects sub lists and spaces accordingly. 
  TODO(xcollantes@): sub list detection.
  """
  is_list = re.match('^[0-9]\.|^\-|^\+|^\*', line)

  if is_list is not None:
    print(line)
    print('IS LIST: ', is_list)



def rules_ordered_lists(line, out_file, flag):
  """Convert to <ol> tag with subscript <li>
  
  This does not handle multi-level lists 
  greated than two levels deep.  
  """
  ordered_element = re.search('^[0-9]\..*', line)

  if ordered_element is not None:

    line_parse = re.search('^([0-9]).(.*)', line)
    number = line_parse.group(1)
    list_content = line_parse.group(2)

    print()
    if flag is False:
      print('')
      out_file.write('<ol class="number">\n<li>{}.&nbsp;{}</li>\n'.format(number, list_content))

    else:
      out_file.write('\s\s<li>{}</li>')

    #if flag is True:




def rules_style(line, out_file):
  """Translate Bold, Italics, Underline notation.
  """
  b_flag = False
  i_flag = False
  u_flag = False


def rules_images(line, out_file):
  """Convert to <img>
  """
  img_md = re.search('.*!\[(.*)\]\((.*)\)', line)
  
  if img_md is not None:
    alt_text = img_md.group(1)
    img_path = img_md.group(2)

    print('Found <img> tag with text as \"{}\" in path \"img_path\".'.format(alt_text, img_path))
    out_file.write('\n<img src=\"{}\" alt=\"{}\">\n'.format(img_path, alt_text))



def rules_header(line, out_file):
  """
    text: Line in file. 
	  out_file: Output file to write append to.
  """
  out_file.write('<h1>{}</h1>\n'.format(''.join(line[1:]))) if line[0] == '#' else 0
  out_file.write('<h2>{}</h2>\n'.format(''.join(line[1:]))) if line[0] == '##' else 0
  out_file.write('<h3>{}</h3>\n'.format(''.join(line[1:]))) if line[0] == '###' else 0
  out_file.write('<h4>{}</h4>\n'.format(''.join(line[1:]))) if line[0] == '####' else 0



def rules_links(line, out_file):
  """Construct <a> tag from links.
  """
  link = re.search('[^!]\[(.*)\]\((.*)\)', line)
  if link is None:
    return 0

  print('Found <a> tag with link \"{}\" directs to \"{}\".'.format(link.group(1), link.group(2)))
  out_file.write('<a href="{}">{}</a>\n'.format(link.group(2), link.group(1)))
    


converter('target.md')
