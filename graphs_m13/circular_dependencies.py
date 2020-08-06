dependencies = {
  "name": "my_cool_software",
  "version": "1.0.0",
  "dependencies": {
    "xmllib": { 
      "version": "0.2.3",
      "name": "xmllib",
      "dependencies" : {
          "parser": {
            "name": "parser",
            "version": "1.2.1"
          },
          
        }
      },
      "parser": {
        "name": "parser",
        "version": "1.4.6"
       }
    }
}

def flatten_dependencies(dependencies):
  final = {}
  duplicates = []
  
  def get_nested_dependencies(dependencies):
    
    for key in dependencies['dependencies']:
      print(key)
      if 'dependencies' in dependencies['dependencies'][key].keys():
        get_nested_dependencies(dependencies['dependencies'][key])
        
        
      if dependencies['dependencies'][key]['name'] in final.keys() and dependencies['dependencies'][key]['version']==final[dependencies['dependencies'][key]['name']]:
        break
      elif dependencies['dependencies'][key]['name'] not in final.keys() and dependencies['dependencies'][key]['name'] not in duplicates:
        final[dependencies['dependencies'][key]['name']]=dependencies['dependencies'][key]['version']
        duplicates.append(dependencies['dependencies'][key]['name'])
      else:
        if dependencies['dependencies'][key]['name'] in final.keys():
          new_key = dependencies['dependencies'][key]['name']+'@'+final[dependencies['dependencies'][key]['name']]
          val = final[dependencies['dependencies'][key]['name']]
          final.pop(dependencies['dependencies'][key]['name'])
          final[new_key]=val
         
        new_key =  dependencies['dependencies'][key]['name'] +'@'+dependencies['dependencies'][key]['version']
        
        final[new_key] = dependencies['dependencies'][key]['version']
        
        
        
  get_nested_dependencies(dependencies)
  return(final)
  
  


flatten_dependencies(dependencies)  

