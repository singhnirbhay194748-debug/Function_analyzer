
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

st.set_page_config(
    page_title="Interactive Signal Generator",
    page_icon="📈",
    layout="wide"
)

st.title("Interactive Signal Generator")
st.write(
    "Explore basic signals and understand how "
    "amplitude, frequency, and phase affect them."
)

# User controls
wave_type = st.selectbox(
    "Select Signal Type",
    ["Sine", "Cosine", "Square", "Triangular", "Sawtooth"]
)

amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
frequency = st.slider("Frequency (Hz)", 0.5, 10.0, 2.0, 0.5)
phase_deg = st.slider("Phase (degrees)", 0, 360, 0, 15)

# Sampling and time axis
sampling_rate = 1000
duration = 2
t = np.arange(0, duration, 1 / sampling_rate)

# Convert phase from degrees to radians
phase = np.deg2rad(phase_deg)
angle = 2 * np.pi * frequency * t + phase

# Generate the selected signal
if wave_type == "Sine":
    x = amplitude * np.sin(angle)
elif wave_type == "Cosine":
    x = amplitude * np.cos(angle)
elif wave_type == "Square":
    x = amplitude * signal.square(angle)
elif wave_type == "Triangular":
    x = amplitude * signal.sawtooth(angle, width=0.5)
else:
    x = amplitude * signal.sawtooth(angle)

# Display signal properties
c1, c2, c3 = st.columns(3)
c1.metric("Amplitude", f"{amplitude:.1f}")
c2.metric("Frequency", f"{frequency:.1f} Hz")
c3.metric("Time Period", f"{1 / frequency:.2f} s")

# Plot the waveform
fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(t, x, linewidth=1.5)
ax.set_title(f"{wave_type} Wave")
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Amplitude")
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2 / frequency)
st.pyplot(fig)
plt.close(fig)

st.success("Signal generated successfully!")

with st.expander("Understand the mathematics"):
    st.latex(
        r"x(t) = A\\sin(2\\pi ft + \\phi)"
    )
    st.write("A = amplitude")
    st.write("f = frequency in hertz")
    st.write("φ = phase angle in radians")
    st.write("Time period T = 1/f")
