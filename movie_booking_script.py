import pandas as pd

# Sample data for concept and description pairs
data = {
    'Concept': [
        'Booking a Movie Ticket',
        'Cinema Lobby Experience',
        'Cinema Hall Ambiance',
        'Outdoor Movie Night',
        'Virtual Reality Movie Experience',
        'Movie Streaming at Home',
        'Film Festival Exploration',
        'Vintage Movie Theater',
        'Sci-Fi Movie Marathon',
        'Family Movie Night',
        'Solo Movie Adventure',
        'Art House Cinema Visit',
        'Animated Movie Extravaganza',
        'Thriller Movie Night',
        'Classic Hollywood Films',
        'Romantic Movie Date',
        'Movie Premiere Excitement',
        'Movie Director Behind the Scenes',
        'Movie Ticket Giveaway Event',
        'Film Critic Review Session',
        'Behind the Scenes Documentary',
        'Musical Movie Spectacle',
        'Historical Epic Movie',
        'Summer Blockbuster Premiere'
    ],
    'Description': [
        'You are sitting comfortably on your couch, browsing through a sleek movie ticket booking app on your smartphone...',
        'Upon arriving at the cinema, you are greeted by a vibrant lobby filled with the aroma of buttered popcorn...',
        'Stepping into the cinema hall, you are enveloped in a cocoon of dimmed lights and the soft rustle of fellow moviegoers...',
        'Underneath a starry night sky, you unfold your camping chair at an outdoor movie night event in the community park...',
        'Immerse yourself in a virtual reality movie experience, where you become part of the cinematic world...',
        'Settling into your favorite spot on the sofa, you navigate through a user-friendly movie streaming platform on your smart TV...',
        'Embark on a cinematic adventure at a film festival, where a diverse selection of films awaits your exploration...',
        'Transport yourself to a bygone era as you step into a vintage movie theater with its classic architecture and red velvet seats...',
        'Embark on a sci-fi movie marathon, where futuristic worlds and technological wonders unfold on the screen...',
        'Gather the family for a cozy movie night, complete with blankets, pillows, and a selection of favorite films...',
        'Embark on a solo movie adventure, selecting a film that resonates with your current mood and preferences...',
        'Explore the artistic charm of an art house cinema, where independent and thought-provoking films take center stage...',
        'Dive into an animated movie extravaganza, filled with colorful characters and heartwarming storytelling...',
        'Prepare for an evening of suspense and excitement with a thriller movie night, featuring gripping plot twists...',
        'Indulge in the timeless charm of classic Hollywood films, featuring iconic actors and cinematic masterpieces...',
        'Plan a romantic movie date night, complete with a candlelit setting, comfortable seating, and a romantic film selection...',
        'Feel the excitement of attending a movie premiere, where the red carpet is rolled out, and stars grace the event...',
        'Get a glimpse behind the scenes as a movie director brings a cinematic vision to life, orchestrating every detail...',
        'Join a movie ticket giveaway event, where lucky winners receive exclusive passes to the latest blockbuster...',
        'Participate in a film critic review session, discussing the nuances of storytelling, cinematography, and performances...',
        'Experience the making of a movie with a behind-the-scenes documentary, revealing the challenges and triumphs of filmmaking...',
        'Immerse yourself in a musical movie spectacle, where song and dance elevate the cinematic experience...',
        'Embark on a journey through a historical epic movie, featuring grand landscapes, epic battles, and timeless stories...',
        'Celebrate the arrival of summer with a blockbuster premiere, where high-energy films captivate audiences...'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add 'text' column
df['text'] = f"###Human:\ngenerate a midjourney prompt for {df['Concept']}\n\n###Assistant:\n{df['Description']}"

# Write DataFrame to CSV file
df.to_csv('concept_description_pairs.csv', index=False)

print("CSV file created successfully.")
