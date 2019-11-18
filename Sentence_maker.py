def sentence_maker(phrase):
    questionWords = ("how", "why", "when", "what")
    low = phrase.lower()
    capitalized = low.capitalize()
    if low.startswith(questionWords):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)