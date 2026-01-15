import streamlit as st
import random

# --- 1. SETTINGS & SCOREBOARD (Sabse upar) ---
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []
if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
if 'detective_wins' not in st.session_state:
    st.session_state.detective_wins = 0

# --- 2. SIDEBAR (Character & Game Selection) ---
st.sidebar.title("🎮 Game Hub Settings")
player_name = st.sidebar.text_input("Apna Naam Likho:", "Player 1")
avatar = st.sidebar.selectbox("Apna Avatar Chuno:", ["🐱", "🤖", "🥷", "🦄", "🦁"])

st.sidebar.markdown("---")
select_game = st.sidebar.radio("Kaunsa Game Khelna Hai?", ["🏠 Home", "🕵️ Number Detective", "✊ Rock Paper Scissors"])

# --- 3. HOME PAGE ---
if select_game == "🏠 Home":
    st.title(f"Welcome, {player_name} {avatar}!")
    st.write("Aapne abhi tak itne games jeete hain:")
    col1, col2 = st.columns(2)
    col1.metric("RPS Wins", st.session_state.rps_wins)
    col2.metric("Detective Wins", st.session_state.detective_wins)
    st.info("Sidebar se koi bhi game select karein aur khelna shuru karein!")

# --- 4. NUMBER DETECTIVE GAME ---
elif select_game == "🕵️ Number Detective":
    st.title("🕵️ Number Detective")
    st.write(f"Hello Detective {player_name}, main ek number soch raha hoon 1 se 100 ke beech mein.")
    
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.number_input("Guess lagao:", min_value=1, max_value=100, step=1)
    
    if st.button("Check Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.warning("Thoda upar! 📈")
        elif guess > st.session_state.secret_number:
            st.warning("Thoda niche! 📉")
        else:
            st.success(f"Balle Balle! 🎉 Aapne {st.session_state.attempts} baar mein dhoond liya!")
            st.session_state.leaderboard.append({"Game": "Detective", "Name": player_name, "Score": st.session_state.attempts})
            st.session_state.detective_wins += 1
            # Reset game for next time
            del st.session_state.secret_number

# --- 5. ROCK PAPER SCISSORS GAME ---
elif select_game == "✊ Rock Paper Scissors":
    st.title("✊ Rock Paper Scissors")
    user_move = st.selectbox("Apna move chuno:", ["Rock", "Paper", "Scissors"])
    
    if st.button("Play!"):
        ai_move = random.choice(["Rock", "Paper", "Scissors"])
        st.write(f"Computer ne chuna: **{ai_move}**")
        
        if user_move == ai_move:
            st.info("Match Draw ho gaya! 🤝")
        elif (user_move == "Rock" and ai_move == "Scissors") or \
             (user_move == "Paper" and ai_move == "Rock") or \
             (user_move == "Scissors" and ai_move == "Paper"):
            st.success("Yesss! Aap Jeet Gaye! 🏆")
            st.session_state.rps_wins += 1
            st.session_state.leaderboard.append({"Game": "RPS", "Name": player_name, "Score": "Win"})
        else:
            st.error("Oh ho! Computer jeet gaya. 🤖")

# --- 6. LEADERBOARD (Sidebar mein niche) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Global Leaderboard")
if not st.session_state.leaderboard:
    st.sidebar.write("Abhi tak koi record nahi hai.")
else:
    for entry in st.session_state.leaderboard[-5:]: # Sirf last 5 entries dikhayega
        st.sidebar.write(f"{entry['Name']} ({entry['Game']}): {entry['Score']}")