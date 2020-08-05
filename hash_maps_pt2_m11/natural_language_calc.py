def nlp_calculator(statement):
  final =''
  statement = list(statement.split())
  
  function, val1, val2 = statement[0], statement[1],statement[3]
  
  if '-' in val1 and val1!='one-hundred':
    temp = val1.split('-')
    val1 = add(translator[temp[0]],translator[temp[1]])
  else:
    val1 = int(translator[val1])
    
    
  if '-' in val2 and val2!='one-hundred':
    temp = val2.split('-')
    val2 = add(translator[temp[0]],translator[temp[1]])
  else:
    val2 = int(translator[val2])
  
  function = translator[function]  
 
  print(type(val1),val2)
  result = function(val1,val2)

  if result<0:
    final="negative "
    result*=-1
    
  if str(result) in translator:
    return(final+translator[str(result)])
  elif 20<=result<=99:
    tens = translator[str((result//10)*10)]
    ones = translator[str(result%10)]
    return(final+tens+'-'+ones)
    
  
  
  return(final)
  
  
  
def add(a,b):
  return a + b

def subtract(a,b):
  return b-a

def divide(a,b):
  return a//b
   
def multiply(a,b):
  return a*b
    
translator = {
  "add": add,
  "divide":divide,
  "multiply":multiply,
  "subtract":subtract,
  "one":1,
  "two":2,
  'three':3,
  "four":4,
  "five":5,
  'six':6,
  "seven":7,
  "eight":8,
  'nine':9,
  'ten':10,
  'eleven':11,
  'twelve':12,
  'thirteen':13,
  'fourteen':14,
  'fifteen':15,
  'sixteen':16,
  'seventeen':17,
  'eightteen':18,
  'nineteen':19,
  'twenty':20,
  'thrirty':30,
  'forty':40,
  'fifty':50,
  'sixty':60,
  'seventy':70,
  'eighty':80,
  'ninety':90,
  'one-hundred':100,
  "1":'one',
  '2':'two',
  '3':'three',
  '4':'four',
  '5':'five',
  '6':'six',
  '7':'seven',
  '8':'eight',
  '9':'nine',
  '10':'ten',
  '11':'eleven',
  '12':'twelve',
  '13':'thirteen',
  '14':'fourteen',
  '15':'fifteen',
  '16':'sixteen',
  '17':'seventeen',
  '18':'eightteen',
  '19':'nineteen',
  '20':'twenty',
  '30':'thirty',
  '40':'forty',
  '50':'fifty',
  '60':'sixty',
  '70':'seventy',
  '80':'eighty',
  '90':'ninety',
  '0':''
  
}


print(nlp_calculator("subtract twenty-two from fifty-two"))