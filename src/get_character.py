import re

def get_characters(str):
  str_without_spaces = re.sub(r'\s', '', str)
  str_without_zero_width_space = re.sub(r'\u200b', '', str_without_spaces)
    
  numbers = re.findall(r"\d", str_without_zero_width_space)
  letters = re.findall(r"[a-zA-Z]", str_without_zero_width_space)
  special_characters = re.findall(r"[^a-zA-Z0-9]", str_without_zero_width_space)

  characters = {
    'numbers': {
      'count': len(numbers),
      'list': numbers,
    },
    'letters': {
      'count': len(letters),
      'list': letters,
    },
    'special_characters': {
      'count': len(special_characters),
      'list': special_characters,
    },
  }

  return characters