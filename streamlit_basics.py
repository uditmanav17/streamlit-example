import math
import time
from collections import namedtuple

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# below comments can be used as markdown cell

st.title("My first Demo App")

st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)

# using magic
"""
# My first app (with magic)
Here's our first magical attempt at using data to create a table:
"""

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

df


"""
# Drawing Line Chart
"""
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

"""
# Plotting a Map (via check box)
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

if st.checkbox("Show Magic"):
    st.map(map_data)

"""
# Selectors
"""

option2 = st.selectbox("Which number do you like best?", df["second column"])
"You selected: ", option2

st.sidebar.markdown("# Sidebar Selector")
option = st.sidebar.selectbox("Which number do you like best?", df["first column"])
st.sidebar.write("You selected: ", option)

"""
# Beta columns to have columns side by side
"""
left_column, right_column = st.beta_columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Woohoo!")

"""
# Beta expander to hide huge content
"""
expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


"""
# Showing Progress
"""
"Starting a long computation..."

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"...and now we're done!"
# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))
