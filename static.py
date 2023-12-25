# Import necessary libraries
import streamlit as st

# Define movie categories and questions
categories = {
    "experience": "",
    "genre": "",
    "movie": "",
    "theatre": "",
    "show_timings": "",
    "tickets": ""
}

twoD_genre = [
    "Action",
    "Comedy",
    "Drama",
    "Sci-fi"
]

threeD_genre = [
    "Action",
    "Comedy",
    "Drama",
    "Sci-fi"
]

action = [
    "Avengers Endgame",
    "John wick 4",
    "Creed 3",
    "Top Gun Maverick"
]

comedy = [
    "Johnny English : Reborn",
    "The Dictator",
    "Barbie",
    "We are the Millers"
]

drama = [
    "Ghosted",
    "Once Upon a Time in Hollywood",
    "Oppenheimer",
    "The Red Notice"
]

scifi = [
    "Avatar: The Way of Water",
    "SpiderMan - Across the Spiderverse",
    "Thor: Love and Thunder",
    "Blue Beetle"
]

theatre = [
    "Aero Theatre",
    "Vista Theatre",
    "Regal Cinemas",
    "Universal Cinemas"
]

show_timings = [
    "11:00AM",
    "2:00PM",
    "6:00PM",
    "9:00PM"
]

tickets = [
    1,
    2,
    3,
    4,
    5,
    6
]

if 'experience' not in st.session_state:
    st.session_state['experience'] = ''
if 'genre' not in st.session_state:
    st.session_state['genre'] = ''
if 'movie' not in st.session_state:
    st.session_state['movie'] = ''
if 'theatre' not in st.session_state:
    st.session_state['theatre'] = ''
if 'show_timings' not in st.session_state:
    st.session_state['show_timings'] = ''
if 'tickets' not in st.session_state:
    st.session_state['tickets'] = ''

def click_button_experience(experience):
    st.session_state['experience'] = experience

def click_button_genre(genre):
    st.session_state['genre'] = genre

def click_button_movie(movie):
    st.session_state['movie'] = movie

def click_button_theatre(theatre):
    st.session_state['theatre'] = theatre

def click_button_show_timings(show_timings):
    st.session_state['show_timings'] = show_timings

def click_button_tickets(ticket):
    st.session_state['tickets'] = ticket

# Streamlit app
def movie_booking_chatbot():
    st.title("Movie Booking Chatbot")

    # User greeting
    user_input = st.text_input("Say 'hi' to start the chatbot:")

    if user_input.lower() == 'hi':
        st.text("Hello! I'm the movie booking chatbot. Choose your movie experience.")
        st.button('2D', on_click=click_button_experience, args=['2D'])
        st.button('3D', on_click=click_button_experience, args=['3D'])
        st.text(st.session_state['experience'])

        if len(st.session_state['experience']) != 0:
            st.text("Choose a genre.")
            if st.session_state['experience'].lower() == '2d':
                for genre in twoD_genre:
                    st.button(genre, on_click=click_button_genre, args=[genre])
            else:
                for genre in threeD_genre:
                    st.button(genre, on_click=click_button_genre, args=[genre])

            st.text(st.session_state['genre'])

            if len(st.session_state['genre']) != 0:
                st.text("Choose a movie.")
                movies = action if st.session_state['genre'].lower() == 'action' else \
                    comedy if st.session_state['genre'].lower() == 'comedy' else \
                    drama if st.session_state['genre'].lower() == 'drama' else scifi
                for movie in movies:
                    st.button(movie, on_click=click_button_movie, args=[movie])

                st.text(st.session_state['movie'])

                if len(st.session_state['movie']) != 0:
                    st.text("Choose a theatre.")
                    for t in theatre:
                        st.button(t, on_click=click_button_theatre, args=[t])

                    st.text(st.session_state['theatre'])

                    if len(st.session_state['theatre']) != 0:
                        st.text("Choose a show timing.")
                        for timing in show_timings:
                            st.button(timing, on_click=click_button_show_timings, args=[timing])

                        st.text(st.session_state['show_timings'])

                        if len(st.session_state['show_timings']) != 0:
                            st.text("Choose the number of tickets.")
                            for ticket in tickets:
                                st.button(str(ticket), on_click=click_button_tickets, args=[ticket])

                            st.text(st.session_state['tickets'])
                            st.text("Your booking details:")
                            st.text(f"Experience: {st.session_state['experience']}")
                            st.text(f"Genre: {st.session_state['genre']}")
                            st.text(f"Movie: {st.session_state['movie']}")
                            st.text(f"Theatre: {st.session_state['theatre']}")
                            st.text(f"Show Timing: {st.session_state['show_timings']}")
                            st.text(f"Number of Tickets: {st.session_state['tickets']}")

if __name__ == "__main__":
    movie_booking_chatbot()
