
import streamlit as st

# European roulette layout (clockwise physical order)
wheel_layout = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6,
    27, 13, 36, 11, 30, 8, 23, 10, 5, 24,
    16, 33, 1, 20, 14, 31, 9, 22, 18, 29,
    7, 28, 12, 35, 3, 26
]

def predict_roulette_landing(ball_rps, wheel_rps, time_until_drop):
    degrees_per_rotation = 360
    ball_degrees = ball_rps * degrees_per_rotation * time_until_drop
    wheel_degrees = wheel_rps * degrees_per_rotation * time_until_drop
    relative_degrees = (ball_degrees - wheel_degrees) % 360
    segment_size = 360 / len(wheel_layout)
    segment_index = int(relative_degrees // segment_size)
    predicted_number = wheel_layout[segment_index]
    return predicted_number, segment_index, round(relative_degrees, 2)

# Streamlit UI
st.set_page_config(page_title="Roulette Live Calculator", page_icon="🎯")

st.title("🎯 Live Roulette Prediction Calculator")
st.markdown("Predict the likely landing number using ball & wheel speeds.")

# Input sliders with upper limit increased to 100
ball_rps = st.slider("Ball Speed (revolutions per second)", 0.5, 100.0, 3.0, 0.1)
wheel_rps = st.slider("Wheel Speed (revolutions per second)", 0.1, 100.0, 0.5, 0.1)
time_until_drop = st.slider("Time Until Drop (seconds)", 1.0, 100.0, 3.2, 0.1)

# Prediction
predicted_number, segment_index, rel_angle = predict_roulette_landing(ball_rps, wheel_rps, time_until_drop)

# Output
st.subheader("Prediction Result")
st.metric("🎰 Predicted Number", predicted_number)
st.write(f"Segment Index: `{segment_index}`")
st.write(f"Relative Angle: `{rel_angle}°`")

st.info("⚠️ This simulation is educational and assumes ideal conditions. Real roulette wheels have random deflections.")
