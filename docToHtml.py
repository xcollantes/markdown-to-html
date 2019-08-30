"""Convert MarkDown notation file to HTML file 
   specifically for xaviercollantes.me schema
"""

__author__ = "Xavier Collantes"

import os
import re

def converter(file_md, header_html, post_html):
  """
    file_md: Markdown notated file.
    
    Returns: File object of input file. 

    Raises: File not found.

    Drawbacks: Does not accept all official Markdown rules yet.
  """  
  
  if not os.path.exists(file_md):
    raise FileNotFoundError
	
  if header_html is not None and not os.path.exists(header_html):
    raise FileNotFoundError
	
  if header_html is not None and not os.path.exists(post_html):
    raise FileNotFoundError

  out_filename = os.path.split(file_md)[-1].split('.')[-2] + '.html'
  
  global flag_is_ol_list
  _set_is_ol_list(False)

  global flag_is_ul_list
  _set_is_ul_list(False)

  global flag_is_paragraph
  _set_is_paragraph(False)

  global temp_output
  temp_output = ''

	# Open Markdown file
  with open(file_md, 'r') as md:

    for line in md:
      line = line.strip()  # Remove newline character
      
      # Structure level parsing
      rules_ordered_lists(line, temp_output, flag_is_ol_list)
      rules_unordered_lists(line, temp_output, flag_is_ul_list)

      rules_p_tag(line, temp_output, flag_is_paragraph)
      rules_header(line.split(' '), temp_output)



    if flag_is_ul_list is True:
      append_to_temp('</ul>\n\n')

    if flag_is_ol_list is True:
      append_to_temp('</ol>\n\n')


  print('*** OUTPUT FILE ***\n%s' % temp_output)

  for temp_line in temp_output.splitlines():
    print('TEMP: %s' % temp_line)

  temp_output = re.sub('[!]\[(.*)\]\((.*)\)', img_tag_regex, temp_output)
  temp_output = re.sub('\[(.*)\]\((.*)\)', a_tag_regex, temp_output)
  
  for temp_line in temp_output.splitlines():    
    print('FINL: %s' % temp_line)


  # Final output to HTML file
  with open(out_filename, 'w+') as out:
  
    if header_html is not None:
      with open(header_html, 'r') as header:
        out.write(header.read() + '\n\n')	

    for temp_output_line in temp_output.splitlines():
      out.write(('\t' * 4) + temp_output_line + '\n')

    if post_html is not None:
      with open(post_html, 'r') as footer:
        out.write(footer.read() + '\n\n')


def a_tag_regex(match):
  return '<a href="{}">{}</a>'.format(match.group(2), match.group(1))


def img_tag_regex(match):
  return '<img src=\"{}\" alt=\"{}\">'.format(match.group(2), match.group(1))



def append_to_temp(element):
  """Temp level output file append. 

  element: string to be added. 

  This holds the structure of parsed data coming from
  Markdown.  Character level parsing to be performed
  on this object called temp_output.  
  """
  global temp_output


  temp_output = temp_output + str(element)


def _set_is_ul_list(state):
  global flag_is_ul_list
  flag_is_ul_list = state


def rules_unordered_lists(line, out_file, is_list):
  """Convert to <ul> tag with subscript <li>
  
  This does not handle multi-level lists 
  greated than one level deep.  
  """
  ul_regex = '^[-+\*](.*)'
  content_ul_regex = '^[-+\*](\s)?(.*)'
  ordered_element = re.search(ul_regex, line)

  if is_list is False and ordered_element is not None:

    line_parse = re.search(content_ul_regex, line)
    list_content = line_parse.group(2)

    # line_parse = re.search('^([0-9]).(.*)', line)
    # number = line_parse.group(1)
    # list_content = line_parse.group(2)

    append_to_temp('<ul class="bullet">\n  <li>{}</li>\n'.format(list_content))

    _set_is_ul_list(True)

    #out_file.write('LIST: ' + str(is_list) + '... OE: Y ' + ordered_element.string + '\n\n')

  if is_list is True and ordered_element is not None:
    line_parse = re.search(content_ul_regex, line)
    list_content = line_parse.group(2)

    append_to_temp('  <li>{}</li>\n'.format(list_content))
    #out_file.write('LIST: ' + str(is_list) + '... OE: Y ' + ordered_element.string + '\n\n')

  if is_list is True and ordered_element is None:
    append_to_temp('</ul>\n\n')
    _set_is_ul_list(False)

  else:
    return 0


def _set_is_ol_list(state):
  global flag_is_ol_list
  flag_is_ol_list = state


def rules_ordered_lists(line, out_file, is_list):
  """Convert to <ol> tag with subscript <li>
  
  This does not handle multi-level lists 
  greated than one level deep.  
  """
  ordered_element = re.search('^[0-9]\..*', line)

  if is_list is False and ordered_element is not None:

    line_parse = re.search('^([0-9]).(.*)', line)
    number = line_parse.group(1)
    list_content = line_parse.group(2)

    # line_parse = re.search('^([0-9]).(.*)', line)
    # number = line_parse.group(1)
    # list_content = line_parse.group(2)

    append_to_temp('<ol class="number">\n  <li>{}.&nbsp;{}</li>\n'.format(number, list_content))

    _set_is_ol_list(True)

  if is_list is True and ordered_element is not None:
    line_parse = re.search('^([0-9]).(.*)', line)
    number = line_parse.group(1)
    list_content = line_parse.group(2)

    append_to_temp('  <li>{}.&nbsp;{}</li>\n'.format(number, list_content))

  if is_list is True and ordered_element is None:
    append_to_temp('</ol>\n\n')
    _set_is_ol_list(False)

  else:
    return 0


def _set_is_paragraph(state):
  global flag_is_paragraph
  flag_is_paragraph = state


def rules_p_tag(line, temp_output, flag):
  """Parse untagged text as <p> tag

  If not a free text, then push as is to temp_output. 
  """
  check_header = re.search('^\#{1,}', line)
  check_links = re.search('[^!]\[(.*)\]\((.*)\)', line)
  check_image = re.search('.*!\[(.*)\]\((.*)\)', line)
  check_list = re.search('^([0-9]|[-+\*])', line)

  if len(line) is 0 and flag_is_paragraph:
    append_to_temp('</p>\n\n')
    _set_is_paragraph(False)

  if check_header is None and check_list is None and len(line) is not 0:
    if flag_is_paragraph:
      append_to_temp('  {}\n'.format(line))
    else:
      append_to_temp('<p>\n  {}\n'.format(line))
      _set_is_paragraph(True)

  if (check_header or check_list) and flag_is_paragraph:
    append_to_temp('</p>\n\n') 
    _set_is_paragraph(False)


def rules_header(line, out_file):
  """
    text: Line in file. 
	  out_file: Output file to write append to.
  """
  if len(line) is 0:
    return 0

  append_to_temp('<h1>{}</h1>\n'.format(' '.join(line[1:]))) if line[0] == '#' else 0
  append_to_temp('<h2>{}</h2>\n'.format(' '.join(line[1:]))) if line[0] == '##' else 0
  append_to_temp('<h3>{}</h3>\n'.format(' '.join(line[1:]))) if line[0] == '###' else 0
  append_to_temp('<h4>{}</h4>\n'.format(' '.join(line[1:]))) if line[0] == '####' else 0

