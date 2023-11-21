from Data.Dictionaries import Genres, Moods, Scales, Chord_Progressions, Instruments

def lowercase_all_dict_keys(module):
    """
    Converts all keys in all dictionaries within the specified module to lowercase.
    """
    filenames_to_process = ["Chord_Progressions", "Genres", "Instruments", "Moods", "Scales"]

    for key, value in vars(module).items():
        if key in filenames_to_process and isinstance(value, dict):
            new_dict = {k.lower(): v for k, v in value.items()}
            # Update the dictionary with lowercase keys
            vars(module)[key].clear()  # Clear the original dictionary
            vars(module)[key].update(new_dict)  # Update with lowercase keys
            
def print_scale(scale_name):
    for scale_category, scales in Scales.scales.items():
        if scale_name in scales:
            scale_data = scales[scale_name]
            print(f"Scale Name: {scale_name}")
            print(f"Scale Category: {scale_category}")
            print(f"Scale Notes: {', '.join(scale_data['Scale'])}")
            return
