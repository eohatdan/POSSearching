def sentence():					# Sentence 
    result = "<sentence>"
    #  result = result + subject(articlex="the", adjectivex="big", nounx="dog")
    result = result + subject(pronounx='she')
    result = result + predicate(verbx = 'bit',pronounx='me',adverbx=('quickly'))
    result = result + "</sentence>"
    return result
def subject(articlex='',adjectivex='',nounx='',pronounx=''):
    # print("Entering subject: " + articlex + ' ' + adjectivex + ' ' + nounx + ' ' + pronounx) # Debug
    result = "<subject>"
    if nounx != '':
        result = result + nounPhrase(articlex=articlex,adjectivex=adjectivex,nounx=nounx)
    if pronounx != '':
        result = result + pronoun(pronounx=pronounx)
    result = result + "</subject>"
    return result
def predicate(adverbx='',verbx='',nounx='',pronounx='',articlex='',adjectivex=''):
    result = "<predicate>"
    if verbx != '':
        result = result + verbPhrase(adverbx=adverbx,verbx=verbx)
    if nounx != '':
        result = result + objectPhrase(nounx='',pronounx='',articlex='',adjectivex='')
    if pronounx != '':
        result = result + objectPhrase(pronounx=pronounx)
    result = result + "</predicate>"
    return result
def objectPhrase(articlex="",adjectivex="",nounx="",pronounx=""):
    result="<objectPhrase>"
    if nounx != '':
        result = result + nounPhrase(articlex, adjectivex, nounx)
    if pronounx != '':
        result = result + pronoun(pronounx)
    result = result + "</objectPhrase>"
    return result
def nounPhrase(articlex="",adjectivex="",nounx=""):
    result = "<nounPhrase>"
    if articlex != '':
        result = result + article(articlex)
    if adjectivex != '':
        result = result + adjective(adjectivex)
    if nounx != '':
        result = result + noun(nounx)
    result = result + "</nounPhrase>"
    return result
def noun(text, number="",gender=""):
    result = "<noun"
    if number != '':
        result = result + " number='" + number + "'"
    if gender != '':
        result = result + " gender='" + gender + "'"
    result = result + ">" + text + "</noun>"
    return result  
def pronoun(pronounx="", numberx="",genderx=""):
    # print('Entering pronoun:' + pronounx + ' ' + numberx + ' ' + genderx )  # Debug.
    result = "<pronoun"
    if numberx != '':
        result = result + " number='" + numberx + "'"
    if genderx != '':
        result = result + " gender='" + genderx + "'"
    result = result + ">"
    if pronounx != '':
        result = result + pronounx 
    result = result + "</pronoun>"
    return result
def article(text, number="",gender=""):
    result = "<article"
    if number != '':
        result = result + " number='" + number + "'"
    if gender != '':
        result = result + " gender='" + gender + "'"
    result = result + ">" + text + "</article>"
    return result
def adjective(text, number="",gender=""):
    result = "<adjective"
    if number != '':
        result = result + " number='" + number + "'"
    if gender != '':
        result = result + " gender='" + gender + "'"
    result = result + ">" + text + "</adjective>"
    return result
def verbPhrase(adverbx="",modalx="",verbx=""):
    result = "<verbPhrase>"
    if adverbx != '':
        result = result + adverb(adverbx)
    if modalx != '':
        result = result + modal(modalx)
    if verbx != '':
        result = result + verb(verbx)
    result = result + "</verbPhrase>"
    return result
def adverb (text, adverbx=""):
    result = "<adverb>" + text + "</adverb>"
    if adverbx != "":
        result = result + "," + adverb(adverbx)
    return result
def modal(text,modalx=""):
    result = "<modal>" + text + "</modal>"
    if modalx != '':
        result = result + modal(modalx)
    return result
def verb(text, tensex="", moodx ="", numberx = "", genderx=""):
    result = "<verb"
    if tensex != '':
        result = result  + "tense="+tensex
    if moodx != '':
        result = result + "mood="+ moodx
    if numberx != '':
        result = result + "number=" + numberx
    if genderx != '':
        result = result + "gender=" + genderx
    result = result + ">" + text + "</verb>"
    return result
def mySentenceSearch (root): 									 # mySentenceSearch
  pattern = './/subject//noun'
  if root.find(pattern) != None:
    print(root.find(pattern).text)
  pattern = './/subject//pronoun'
  if root.find(pattern) != None:
    print(root.find(pattern).text)
    
  pattern = './/predicate//verb'
  if root.find(pattern) != None:
    print(root.find(pattern).text)
    
  pattern = './/objectPhrase//noun'
  if root.find(pattern) != None:
    print(root.find(pattern).text)
  pattern =   './/objectPhrase//pronoun'
  if root.find(pattern) != None:
    print(root.find(pattern).text)
  return
	
	
	