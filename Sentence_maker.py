# Based on the-python-mega-course in Udemy
# This ones check if there is a question-word in a sentence
# if there's, it'll add a questionmark in the end of the sentence
# if not, nothing will change
# adding sentence to showing later
# all sentences will start with a uppercase letter.


def sentence_maker(phrase):
    questionWords = ("how", "why", "when", "what")
    low = phrase.lower()
    capitalized = low.capitalize()
    if low.startswith(questionWords):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    syote = input("Say something: ")
    if syote == "/exit":
        break
    else:
        results.append(sentence_maker(syote))

print(" ".join(results))
