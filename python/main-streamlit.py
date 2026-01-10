import json
import random
import time

import m26
import streamlit as st

from faker import Faker

# Run the app with command: streamlit run app.py

# Initialize Session State in 'st.session_state'

# Fields for tab1
if "stock_prices" not in st.session_state:
    st.session_state["stock_prices"] = list()


# Fields for tab3: Pace Calculator, prefixed with 'pace_'
if "pace_cached_values" not in st.session_state:
    st.session_state["pace_cached_values"] = dict()
st.session_state["pace_calculation"] = str(st.session_state["pace_cached_values"])
if "pace_dist" not in st.session_state:
    st.session_state["pace_dist"] = "26.2"
if "pace_dist2" not in st.session_state:
    st.session_state["pace_dist2"] = ""
if "pace_etime" not in st.session_state:
    st.session_state["pace_etime"] = "3:47:31"

# Fields for tab4: Run/Walk Calculator, prefixed with 'rw_'
if "rw_cached_values" not in st.session_state:
    st.session_state["rw_cached_values"] = dict()
st.session_state["rw_calculation"] = str(st.session_state["rw_cached_values"])

if "rw_run_time" not in st.session_state:
    st.session_state["rw_run_time"] = "3:15"
if "rw_run_pace" not in st.session_state:
    st.session_state["rw_run_pace"] = "9:30"
if "rw_walk_time" not in st.session_state:
    st.session_state["rw_walk_time"] = "0:45"
if "rw_walk_pace" not in st.session_state:
    st.session_state["rw_walk_pace"] = "16:00"
if "rw_dist" not in st.session_state:
    st.session_state["rw_dist"] = "10.0"

# Fields for tab5: Streamlit Session State
if "clear_state_button" not in st.session_state:
    st.session_state["clear_state_button"] = False

# Global variables
fake = Faker()

# Helper Functions

def as_float(s):
    try:
        return float(s.strip())
    except ValueError:
        return 0.0

# Create the UI, using the st.session_state values.
# The values in the UI are mutable by user interaction in the browser,
# but not by changing the st.session_state values directly with code.
# See 'st.rerun()'below to trigger an update of the UI.

tab_names = "Stock Price Chart,Simulated Chat,Pace Calculator,Run/Walk Calculator,Streamlit Session State".split(",")
tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_names)

with tab1:
    st.header("Stock Price Chart")
    num_months = st.slider('Number of Months', min_value=10, max_value=100)
    if st.button('Line Chart'):
        st.session_state["stock_prices"] = [random.randint(450, 600) for _ in range(num_months)]
        st.line_chart(data=st.session_state["stock_prices"])

with tab2:
    st.header("Simulated Chatbot")

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Simulate an assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            # Simulate a streaming response for better user experience
            #assistant_response = f"You said: {prompt} ...interesting."
            assistant_response = fake.sentence()
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.chat_messages.append({"role": "assistant", "content": full_response})

with tab3:
    st.header("Pace Calculator")

    with st.form(key="pace_calc_form"):
        dist_input = st.text_input("Distance:", key="pace_dist")
        pace_unit_of_distance = st.selectbox(
            "Unit of Distance (miles, kilometers, yards)",("m", "k", "y"))
        etime_input = st.text_input("Elapsed Time (hh:mm:ss format):", key="pace_etime")
        dist2_input = st.text_input("Distance 2 (optional):", key="pace_dist2")
        calc_textarea = st.text_area("Calculation:", key="pace_calculation", height=370) # height is in pixels
        pace_calculate_button = st.form_submit_button("Calculate")

    if pace_calculate_button:
        dist1 = as_float(st.session_state["pace_dist"])
        dist2 = as_float(st.session_state["pace_dist2"])
        d1 = m26.Distance(dist1, pace_unit_of_distance)
        t1 = m26.ElapsedTime(st.session_state["pace_etime"].strip())
        s1 = m26.Speed(d1, t1)
        d2 = None
        if dist2 > 0:
            d2 = m26.Distance(dist2, pace_unit_of_distance)

        calculation = dict()
        calculation["dist1_miles"] = d1.as_miles()
        calculation["dist1_km"] = d1.as_kilometers()
        calculation["dist1_yards"] = d1.as_yards()
        calculation["pace_unit_of_distance"] = pace_unit_of_distance
        calculation["etime"] = t1.as_hhmmss()
        calculation["ppm"] = s1.pace_per_mile()
        calculation["mph"] = s1.mph()
        calculation["kph"] = s1.kph()
        calculation["yph"] = s1.yph()
        calculation["spm"] = s1.seconds_per_mile()
        if d2 is not None:
            calculation["dist2"] = dist2
            calculation["dist2_proj_time"]  = s1.projected_time(d2, "riegel") # Riegel algorithm
            calculation["dist2_proj_miles"] = d2.as_miles()

        # IMPORTANT: Trigger a redraw the UI with the current st.session_state values!
        st.session_state["pace_cached_values"] = json.dumps(calculation, sort_keys=False, indent=2)
        st.rerun()

with tab4:
    st.header("Run/Walk Calculator")

    with st.form(key="run_walk_calc_form"):
        run_time_input = st.text_input("Run Time:", key="rw_run_time")
        run_pace_input = st.text_input("Run Pace:", key="rw_run_pace")
        walk_time_input = st.text_input("Walk Time:", key="rw_walk_time")
        walk_pace_input = st.text_input("Walk Pace:", key="rw_walk_pace")

        rw_dist_input = st.text_input("Distance:", key="rw_dist")
        rw_unit_of_distance = st.selectbox(
            "Unit of Distance (miles, kilometers, yards)",("m", "k", "y"))

        calc_textarea = st.text_area("Calculation:", key="rw_calculation", height=300) # height is in pixels
        rw_calculate_button = st.form_submit_button("Calculate")

    if rw_calculate_button:
        dist = as_float(st.session_state["rw_dist"])
        d = m26.Distance(dist, rw_unit_of_distance)
        run_time = st.session_state["rw_run_time"].strip()
        run_pace = st.session_state["rw_run_pace"].strip()
        walk_time = st.session_state["rw_walk_time"].strip()
        walk_pace = st.session_state["rw_walk_pace"].strip()

        calculation = m26.RunWalkCalculator.calculate(
            run_time,
            run_pace,
            walk_time,
            walk_pace,
            dist)
        calculation["dist"] = dist
        calculation["proj_miles"] = d.as_miles()
        calculation["miles"] = d.as_miles()
        calculation["km"] = d.as_kilometers()
        calculation["yards"] = d.as_yards()
        calculation["unit_of_distance"] = rw_unit_of_distance

        # IMPORTANT: Trigger a redraw the UI with the current st.session_state values!
        st.session_state["rw_cached_values"] = json.dumps(calculation, sort_keys=False, indent=2)
        st.rerun()

with tab5:
    st.header("Streamlit Session State")

    for key in sorted(st.session_state.keys()):
        if key.startswith("FormSubmitter:"):
            pass
        else:
            st.write(f"{key}: {st.session_state[key]}")

    with st.form(key="ss_clear_state_form"):
        ss_clear_state_button = st.form_submit_button("Clear State")

    if ss_clear_state_button:
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
