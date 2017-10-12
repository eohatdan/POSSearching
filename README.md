# POSSearching
What is POSSearching?

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

Why might one want to do POSSearching?

Why would want to do POS searching?  The hypothetical answer is to increase search precision.
The 'hypothetical' refers to the fact that this result is yet to be tested.
Without including POS information, erroneous results can be obtained.  For example, suppose we
are interested in all sentences that match the regular expression '/.*boy\s.*hit\s.*ball.*/.
This expression would match the sentence, 'The boy hit the ball.'  However, it would also match
'My boy was a hit at the ball.' or 'There was a tennis player whose ball boy was hit by a ball.'

