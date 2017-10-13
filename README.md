# POSSearching
### What is POSSearching?

POS Searching is a kind of searching that includes Part Of Speech (POS) information.
For example, return an index to all sentences having the word 'you' as the subject.
Only those sentences that have been parsed and encoded in XML and have the pronoun, 'you'
will be returned.

The searching can be extended to other parts of speech and can include more elaborate syntactic
structure information (called structure paths, or "spaths").  For example, we might want an index to all predicates having having an object
that is the noun, 'ball'.

The spaths can be combined so that multiple POS's can be specified: return an index to all
sentences have 'boy' as the noun of the subject and 'ball' as the noun of a predicate object.
Such a sentence might be "The boy hit the ball."

### Why might one want to do POSSearching?

Why would want to do POS searching?  The hypothetical answer is to increase search precision.
The 'hypothetical' refers to the fact that this result is yet to be tested.
Without including POS information, erroneous results can be obtained.  For example, suppose we
are interested in all sentences that match the regular expression '/.*boy\s.*hit\s.*ball.*/.
This expression would match the sentence, 'The boy hit the ball.'  However, it would also match
'My boy was a hit at the ball.' or 'There was a tennis player whose ball boy was hit by a ball.'

### Development Notes

I am using two separate development tools:
  1.) oXygen XML editor
  2.) Jupyter Notebook
I use the oXygen XML editor to create the data structure files for sentences and questions and to
generate the .xsd files to validate the structure.  I also use XQuery to try out queries against 
the test sentences.

I use Jupyter Notebook to develop what I call form-class functions.  These functions implement the
various form-classes used to generate sentences and questions.  Example: nounPhrase is a function that
generates the XML structure for a nounPhrase.  The function call:

nounPhrase(articlex='the', adjectivex= 'little', nounx='boy')

generates the following XML:
```` xml
<nounPhrase>
     <article>the</article>
     <adjective>little</adjective>
     <noun>boy</noun>
</nounPhrase>
````
 All the form-classes are written as Python functions and are stored in a module file (language.py).
 
 

