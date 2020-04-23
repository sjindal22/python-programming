import json

def validateJson(json_data):

  try:
    json.loads(json_data)

  except ValueError as err:
    return False
  
  return True


print(validateJson("""{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""))
print(validateJson("""{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""))

json_data = """{ 
   "glossary":{ 
      "title":"exampleglossary",
      "GlossDiv":{ 
         "title":"S",
         "GlossList":{ 
            "GlossEntry":{ 
               "ID":"SGML",
               "SortAs":"SGML",
               "GlossTerm":"StandardGeneralizedMarkupLanguage",
               "Acronym":"SGML",
               "Abbrev":"ISO8879:1986",
               "GlossDef":{ 
                  "para":"Ameta-markuplanguage,usedtocreatemarkuplanguagessuchasDocBook.",
                  "GlossSeeAlso":[ 
                     "GML",
                     "XML"
                  ]
               },
               "GlossSee":"markup"
            }
         }
      }
   }
}"""

print(validateJson(json_data))
