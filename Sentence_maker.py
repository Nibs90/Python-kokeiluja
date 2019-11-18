#This ones check if there is a question-word in a sentence
#if there's, it'll add a questionmark in the end of the sentence
#if not, nothing will change

def sentence_maker(phrase):
    questionWords = ("how", "why", "when", "what")
    low = phrase.lower()
    capitalized = low.capitalize()
    if low.startswith(questionWords):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)