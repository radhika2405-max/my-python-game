import streamlit as st
import random

# --- 1. SETUP ---
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []
if 'rps_wins' not in st.session_state:
    st.session_state.rps_wins = 0
if 'rps_move_count' not in st.session_state:
    st.session_state.rps_move_count = 0

# --- 2. SIDEBAR ---
st.sidebar.title("🎮 Mega Game Hub")
player_name = st.sidebar.text_input("Apna Naam Likho:", "Player 1")
select_game = st.sidebar.selectbox("Game Select Karein:", 
    ["🏠 Home", "✊ Rock Paper Scissors", "🎂 Birthday Predictor", "🔢 Memory Challenge"])

# --- 3. HOME PAGE ---
if select_game == "🏠 Home":
    st.title(f"Welcome, {player_name}! ✨")
    st.subheader("Aapka Scorecard:")
    st.write(f"🏆 Total Rock Paper Scissors Wins: {st.session_state.rps_wins}")
    st.info("Sidebar se koi bhi game chuno aur khelna shuru karo!")

# --- 4. ROCK PAPER SCISSORS (Max 5 Moves) ---
elif select_game == "Rock Paper Scissors":
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
                st.error("AI Jeet gaya! 🤖")
    else:
        st.warning("🎮 Game Over! 5 moves khatam ho gaye hain.")
        if st.button("Restart Game"):
            st.session_state.rps_move_count = 0
            st.rerun()

# --- 5. BIRTHDAY DATE PREDICTOR ---
elif select_game == "🎂 Birthday Predictor":
    st.title("🔮 Magic Birthday Predictor")
    st.write("Dhyan se ye steps follow karein, aur main aapki birth date guess karunga!")
    st.markdown("""
    1. Apne **Birth Month** ka number lo (Jan=1, Feb=2...).
    2. Usse **Multiply by 5** karo, phir **Add 6**.
    3. Usse **Multiply by 4** karo, phir **Add 9**.
    4. Usse **Multiply by 5** karo, phir apni **Birth Date** (1-31) add karo.
    """)
    # FIX: Line 65 is here
    final_result = st.number_input("Final Result yahan likho:", step=1, value=0)
    
    if st.button("Predict My Birthday!"):
        magic_number = final_result - 165
        month = magic_number // 100
        date = magic_number % 100
        if 1 <= month <= 12 and 1 <= date <= 31:
            st.balloons()
            st.success(f"Aapka Birthday **{date}/{month}** ko aata hai! ✨")
        else:
            st.error("Calculation check karein, shayad result galat likha hai!")

# --- 6. MEMORY CHALLENGE ---
elif select_game == "🔢 Memory Challenge":
    st.title("🔢 Memory Challenge")
    if 'mem_num' not in st.session_state:
        st.session_state.mem_num = random.randint(1000, 9999)
    st.write("Is number ko yaad rakho:")
    st.subheader(f"🔢 {st.session_state.mem_num}")
    guess = st.number_input("Number kya tha?", step=1, value=0)
    if st.button("Check Memory"):
        if guess == st.session_state.mem_num:
            st.success("Sahi Jawab! 🔥")
            st.session_state.mem_num = random.randint(10000, 99999)
        else:
            st.error(f"Galat! Sahi number {st.session_state.mem_num} tha.")

# --- 7. LEADERBOARD ---
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Leaderboard")
for entry in st.session_state.leaderboard[-5:]:
    st.sidebar.write(f"⭐ {entry['Name']} - {entry['Game']}")