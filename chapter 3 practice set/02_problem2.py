letter = '''Dear <|name|>,
          You are selected!
          <|Date|>'''
print(letter.replace("<|name|>","Harry").replace("<|Date|>","13 Aug 2025"))