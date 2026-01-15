import streamlit as st
import random
import streamlit.components.v1 as components

# --- 🔊 THE VOICE ENGINE ---
def speak(text):
    # This allows the game to talk on both laptops and phones
    js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text}');
        window.speechSynthesis.speak(msg);
        </script>
    """
    components.html(js_code, height=0)

# --- 👤 PLAYER SETUP ---
st.sidebar.title("🎮 Character Creator")
player_name = st.sidebar.text_input("What is your name?", "Player 1")
char_emoji = st.sidebar.selectbox("Choose your avatar:", ["🐱", "🤖", "🦸", "🥷", "🦖"])

st.sidebar.markdown("---")
game_choice = st.sidebar.radio("Select a Game:", ["🏠 Home", "🔢 Number Detective", "✊ Rock Paper Scissors"])

# --- 🏠 HOME SCREEN ---
if game_choice == "🏠 Home":
    st.title(f"Welcome, {player_name} {char_emoji}!")
    st.write("This is your personalized Game Hub. Use the sidebar on the left to pick a game!")
    
    if st.button("Test My Voice"):
        speak(f"Welcome back, {player_name}! Which game are we playing today?")
        st.success("You should hear the computer talking now!")

# --- 🔢 GAME 1: NUMBER DETECTIVE ---
elif game_choice == "🔢 Number Detective":
    st.title("🔢 Number Detective")
    
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0

    st.write(f"I'm thinking of a number between 1 and 100. Can you find it, {player_name}?")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Check Guess"):
        st.session_state.tries += 1
        if guess < st.session_state.secret_number:
            st.warning("HIGHER! 📈")
            speak("Try a higher number")
        elif guess > st.session_state.secret_number:
            st.warning("LOWER! 📉")
            speak("Try a lower number")
        else:
            st.balloons()
            st.success(f"VICTORY! You found it in {st.session_state.tries} tries!")
            speak(f"Amazing job {player_name}! You are a genius.")
            if st.button("Reset Game"):
                del st.session_state.secret_number
                st.rerun()

# --- ✊ GAME 2: ROCK PAPER SCISSORS ---
elif game_choice == "✊ Rock Paper Scissors":
    st.title("✊ Rock Paper Scissors")
    st.write(f"{char_emoji} {player_name} vs 💻 The AI")

    user_move = st.selectbox("Pick your move:", ["Rock", "Paper", "Scissors"])
    
    if st.button("Fight!"):
        moves = ["Rock", "Paper", "Scissors"]
        ai_move = random.choice(moves)
        
        st.write(f"The AI chose: **{ai_move}**")
        
        if user_move == ai_move:
            st.info("It's a draw!")
            speak("We are equal this time.")
        elif (user_move == "Rock" and ai_move == "Scissors") or \
             (user_move == "Paper" and ai_move == "Rock") or \
             (user_move == "Scissors" and ai_move == "Paper"):
            st.success(f"{player_name} wins!")
            speak(f"The {char_emoji} wins this round!")
        else:
            st.error("The AI wins!")
            speak("I am the superior machine.")
            # Add this near the top with your other variables
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# When someone wins Number Detective, add this:
st.session_state.leaderboard.append({"Name": player_name, "Score": attempts})
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Leaderboard")
for entry in st.session_state.leaderboard:
    st.sidebar.write(f"{entry['Name']}: {entry['Score']} tries")
# Create a storage for scores if it doesn't exist yet
if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
if 'detective_best_score' not in st.session_state:
    st.session_state.detective_best_score = None
    if user_move == ai_move:
        st.info("It's a draw!")
    elif (user_move == "Rock" and ai_move == "Scissors") or \
         (user_move == "Paper" and ai_move == "Rock") or \
         (user_move == "Scissors" and ai_move == "Paper"):
        st.success("You Win!")
        # --- ADD THIS LINE BELOW ---
        st.session_state.rps_wins += 1 
    else:
        st.error("AI Wins!")
        st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Stats")
st.sidebar.write(f"👤 Player: **{player_name}**")
st.sidebar.write(f"✊ RPS Wins: **{st.session_state.rps_wins}**")

if st.session_state.detective_best_score:
    st.sidebar.write(f"🕵️ Best Detective Score: **{st.session_state.detective_best_score} tries**")
    # --- INITIALIZE SCORES (The Setup) ---
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
    # 1. SETUP THE SCOREBOARD (Run this first)
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
elif (user_move == "Rock" and ai_move == "Scissors") or \
         (user_move == "Paper" and ai_move == "Rock") or \
         (user_move == "Scissors" and ai_move == "Paper"):
        st.success("You Win!")
        # TRACK THE WIN
        st.session_state.rps_wins += 1 
        # ADD TO LEADERBOARD
        st.session_state.leaderboard.append({"Game": "RPS", "Player": player_name, "Score": "Win"})
elif (user_move == "Rock" and ai_move == "Scissors") or \
         (user_move == "Paper" and ai_move == "Rock") or \
         (user_move == "Scissors" and ai_move == "Paper"):
        st.success("You Win!")
        st.session_state.rps_wins += 1 
        st.session_state.leaderboard.append({"Game": "RPS", "Player": player_name, "Score": "Win"})
else:
        st.error("AI Wins!")
    