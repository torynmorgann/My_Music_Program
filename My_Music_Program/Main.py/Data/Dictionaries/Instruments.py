# Dictionary mapping genres to lists of typical instruments
instruments = {
    "Rock": ["Electric Guitar", "Bass Guitar", "Drums", "Keyboard"],
    "Jazz": ["Saxophone", "Trumpet", "Double Bass", "Piano", "Drum Set"],
    "Classical": ["Violin", "Cello", "Piano", "Flute", "Clarinet"],
    "Pop": ["Acoustic Guitar", "Electric Guitar", "Bass Guitar", "Drums", "Keyboard"],
    "Electronic": ["Synthesizer", "Drum Machine", "Sampler", "Bass Synth"],
    "Blues": ["Acoustic Guitar", "Harmonica", "Piano", "Bass Guitar", "Drums"],
    "Hip Hop": ["Sampler", "Drum Machine", "Turntables", "Synthesizer"],
    "Reggae": ["Electric Guitar", "Bass Guitar", "Drums", "Keyboard", "Percussion"],
    # Add more genres and corresponding instruments as needed
}

def get_instruments_for_genre(genre):
    """ 
    Function to get the list of instruments for a given genre. 
    Returns a list of instruments or an empty list if the genre is not found.
    """
    return instruments.get(genre, [])
