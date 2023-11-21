import tkinter as tk
import random
from Data.Dictionaries import Scales  # Import your scales dictionary

def generate_random_scale():
    # Get a random scale from your scales dictionary
    scale_categories = list(Scales.scales.keys())
    random_category = random.choice(scale_categories)
    scales_in_category = list(Scales.scales[random_category].keys())
    random_scale_name = random.choice(scales_in_category)
    random_scale_data = Scales.scales[random_category][random_scale_name]
    random_scale_notes = ", ".join(random_scale_data["Scale"])
    
    # Remove underscores from the scale type
    scale_type = random_category.replace("_", " ")
    
    # Display the random scale and its notes in a label
    scale_label.config(text=f"Random Scale: {random_scale_name}\nScale Type: {scale_type}\nNotes: {random_scale_notes}")

# Create the main window
root = tk.Tk()
root.title("Random Scale Generator")

# Set the window size to a fixed value (width x height)
window_width = 500
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Create a button to generate a random scale
generate_button = tk.Button(root, text="Generate Random Scale", command=generate_random_scale)
generate_button.pack(pady=10)

# Create a label to display the random scale and its notes
scale_label = tk.Label(root, text="", font=("Helvetica", 18))
scale_label.pack()

# Start the Tkinter main loop
root.mainloop()
