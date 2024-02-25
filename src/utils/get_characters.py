import re

def get_characters(str):
  str_without_spaces = re.sub(r'\s', '', str)
    
  numbers = re.findall(r"\d", str_without_spaces)
  letters = re.findall(r"[a-zA-Z]", str_without_spaces)
  special_characters = re.findall(r"[^a-zA-Z0-9]", str_without_spaces)

  characters = {
    'numbers': {
      'list': numbers,
      'count': len(numbers),
    },
    'letters': {
      'list': letters,
      'count': len(letters),
    },
    'special_characters': {
      'list': special_characters,
      'count': len(special_characters),
    },
  }

  return characters