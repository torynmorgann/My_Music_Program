# Dictionary mapping genres to typical scales
GenreScales = {
    "Rock": ["Pentatonic Minor", "Blues Scale", "Mixolydian Mode"],
    "Jazz": ["Dorian Mode", "Mixolydian Mode", "Bebop Scale"],
    "Classical": ["Major Scale", "Harmonic Minor", "Melodic Minor"],
    "Pop": ["Major Scale", "Natural Minor Scale"],
    "Blues": ["Blues Scale", "Pentatonic Minor"],
    # Add more genres and scales as needed
}

# Dictionary mapping genres to typical chord progressions
GenreChordProgressions = {
    "Rock": ["I-IV-V", "ii-V-I"],
    "Jazz": ["ii-V-I", "I-vi-ii-V"],
    "Classical": ["I-IV-V-I", "ii-V-I"],
    "Pop": ["I-V-vi-IV", "I-IV-V"],
    "Blues": ["I-IV-V", "I-IV-I-V"],
    # Add more genres and progressions as needed
}

# You can also include other mappings like genre to tempo, rhythm patterns, etc.

def get_scales_for_genre(genre):
    """ Function to get the list of scales for a given genre. """
    return GenreScales.get(genre, [])

def get_chord_progressions_for_genre(genre):
    """ Function to get the list of chord progressions for a given genre. """
    return GenreChordProgressions.get(genre, [])

# Add more functions as needed for different musical elements
