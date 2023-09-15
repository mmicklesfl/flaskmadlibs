"""Madlibs Stories."""

class Story:
    """Madlibs story."""

    def __init__(self, words, text):
        """Create story with words and template text."""
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        return text

# Original story
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. 
    It loved to {verb} {plural_noun}."""
)

# Halloween stories
frankenstein = Story(
    ["feeling", "body_part", "verb", "beverage", "dance_move"],
    """At the Halloween party, Frankenstein was feeling particularly {adjective}. 
    Frankenstein could feel a stitch come loose in his {body_part} every time he tried to {verb}.
    To everyone's surprise, when he drank some {beverage}, he started to do the {dance_move}!"""
)

trick_or_treat = Story(
    ["costume", "verb", "character", "candy", "adjective", "celebrity"],
    """On Halloween night, I decided to dress up as a {costume}. 
    As I walked, I would {verb} at every door. 
    {character}'s house gave out {candy} which were {adjective}! 
    But the best part of the night was seeing {celebrity} trick or treating too!"""
)

haunted_house = Story(
    ["room", "sound", "verb", "object", "emotion"],
    """I entered the haunted house and the first {room} had a strange {sound}. 
    I decided to {verb} and stumbled upon a floating {object}. 
    I was filled with {emotion} and couldn't wait to tell my friends!"""
)
