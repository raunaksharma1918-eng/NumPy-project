import numpy as np
import streamlit as st

# ----------------------------
# Initialize session state
# ----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1       # 1 = X, -1 = O
    st.session_state.result = None

symbols = {0: " ", 1: "X", -1: "O"}

# ----------------------------
# Winner checking logic
# ----------------------------
def check_winner(b):
    # Rows & columns
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    # Diagonals
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    # Draw
    if not 0 in b:
        return "DRAW"

    return None


# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🎮 Tic-Tac-Toe (NumPy + Streamlit)")

# Status message
if st.session_state.result:
    if st.session_state.result == "DRAW":
        st.success("😎 Ohoo, it's a draw!")
    else:
        st.success(f"🏆 {st.session_state.result} wins!")
else:
    turn = "X" if st.session_state.current == 1 else "O"
    st.info(f"It's **{turn}**'s turn")

# 3×3 grid of buttons
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        with cols[j]:
            cell_value = symbols[st.session_state.board[i, j]]
            # Always give a boolean to disabled:
            is_disabled = (st.session_state.board[i, j] != 0) or (st.session_state.result is not None)
            if st.button(cell_value or " ", key=f"{i}-{j}", disabled=is_disabled):
                st.session_state.board[i, j] = st.session_state.current
                result = check_winner(st.session_state.board)
                if result:
                    st.session_state.result = result
                else:
                    st.session_state.current *= -1
                st.rerun()      # <-- updated for Streamlit >=1.26

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None
    st.rerun()          # <-- updated
