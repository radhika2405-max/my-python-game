import streamlit as st
import random

# --- 1. SETUP (Sabse upar hona chahiye) ---
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []
if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
if 'rps_move_count' not in st.session_state:
    st.session_state.rps_move_count = 0

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🎮 Mega Game Hub")
player_name = st.sidebar.text_input("Apna Naam Likho:", "Player 1")
select_game = st.sidebar.selectbox("Khelne ke liye game chuno:", 
    ["🏠 Home", "✊ Rock Paper Scissors", "🎂 Birthday Predictor", "🔢 Memory Challenge"])

# --- 3. HOME PAGE ---
if select_game == "🏠 Home":
    st.title(f"Welcome, {player_name}! ✨")
    st.subheader("Aapke Stats:")
    st.write(f"🏆 Rock Paper Scissors Wins: {st.session_state.rps_wins}")
    st.info("Sidebar se game select karein aur khelna shuru karein!")

# --- 4. ROCK PAPER SCISSORS (Max 5 Moves) ---
elif select_game == "✊ Rock Paper Scissors":
    st.title("✊ Rock Paper Scissors")
    
    if st.session_state.rps_move_count < 5:
        st.write(f"Move Number: **{st.session_state.rps_move_count + 1} / 5**")
        user_move = st.selectbox("Apna move chuno:", ["Rock", "Paper", "Scissors"])
        
        if st.button("Play!"):
            st.session_state.rps_move_count += 1
            ai_move = random.choice(["Rock", "Paper", "Scissors"])
            st.write(f"Computer ne chuna: **{ai_move}**")
            
            if user_move == ai_move:
                st.info("Match Draw! 🤝")
            elif (user_move == "Rock" and ai_move == "Scissors") or \
                 (user_move == "Paper" and ai_move == "Rock") or \
                 (user_move == "Scissors" and ai_move == "Paper"):
                st.success("Yesss! Aap Jeet Gaye! 🏆")
                st.session_state.rps_wins += 1
                st.session_state.leaderboard.append({"Name": player_name, "Game": "RPS", "Score": "Win"})
            else:
                st.error("Oh ho! AI Jeet gaya! 🤖")
    else:
        st.warning("🎮 Game Over! 5 moves khatam ho gaye.")
        if st.button("Restart Game"):
            st.session_state.rps_move_count = 0
            st.rerun()

# --- 5. BIRTHDAY DATE PREDICTOR (Math Trick) ---
elif select_game == "🎂 Birthday Predictor":
    st.title("🔮 Magic Birthday Predictor")
    st.write("Ye steps follow karein aur main aapki birth date guess karunga!")
    st.markdown("""
    1. Apne **Birth Month** ka number lo (Jan=1, Feb=2...).
    2. Usse **Multiply by 5** karo, phir **Add 6**.
    3. Usse **Multiply by 4** karo, phir **Add 9**.
    4. Usse **Multiply by 5** karo, phir apni **Birth Date** (1-31) add karo.
    """)
    
    final_result = st.number_input("Calculation ka final result yahan likho:", step=1, value=0)
    
    if st.button("Predict My Birthday!"):
        magic_number = final_result - 165
        month = magic_number // 100
        date = magic_number % 100
        
        if 1 <= month <= 12 and 1 <= date <= 31:
            st.balloons()
            st.success(f"Aapka Birthday **{date}/{month}** ko aata hai! ✨")
        else:
            st.error("Calculation check karein, result sahi nahi lag raha!")

# --- 6. MEMORY CHALLENGE (Logical Game) ---
elif select_game == "🔢 Memory Challenge":
    st.title("🔢 Memory Challenge")
    
    if 'mem_num' not in st.session_state:
        st.session_state.mem_num = random.randint(1000, 9999)
        st.session_state.show_num = True

    if st.session_state.show_num:
        st.write("Is number ko yaad rakho:")
        st.subheader(f"🔢 {st.session_state.mem_num}")
        if st.button("Maine yaad kar liya!"):
            st.session_state.show_num = False
            st.rerun()
    else:
        guess = st.number_input("Number kya tha? Likho:", step=1, value=0)
        if st.button("Check Answer"):
            if guess == st.session_state.mem_num:
                st.success("Sahi Jawab! 🔥")
                st.session_state.mem_num = random.randint(1000, 9999)
                st.session_state.show_num = True
            else:
                st.error(f"Galat! Sahi number {st.session_state.mem_num} tha.")
                if st.button("Try Again"):
                    st.session_state.show_num = True
                    st.rerun()

# --- 7. LEADERBOARD (Sidebar mein niche) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Leaderboard")
if not st.session_state.leaderboard:
    st.sidebar.write("Abhi tak koi wins nahi hain.")
else:
    for entry in st.session_state.leaderboard[-5:]:
        st.sidebar.write(f"⭐ {entry['Name']} - {entry['Game']}")