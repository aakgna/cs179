import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Average Fare Based on Airport")

    starting_avg = pd.DataFrame({
        "Airport": ["ATL", "BOS", "CLT", "DEN", "DFW", "DTW", "EWR", "IAD", "JFK", "LAX", "LGA", "MIA", "OAK", "ORD", "PHL", "SFO"],
        "Avg(fare)": [276.28, 247.45, 283.13, 294.86, 263.24, 299.32, 271.40, 321.90, 328.48, 345.85, 261.39, 268.32, 511.32, 248.55, 307.12, 382.76]
    })

    destination_avg = pd.DataFrame({
        "Airport": ["ATL", "BOS", "CLT", "DEN", "DFW", "DTW", "EWR", "IAD", "JFK", "LAX", "LGA", "MIA", "OAK", "ORD", "PHL", "SFO"],
        "Avg(fare)": [278.11, 260.35, 286.93, 298.81, 271.55, 309.02, 284.02, 319.41, 325.56, 324.21, 260.94, 265.56, 507.21, 259.98, 320.31, 367.99]
    })


    fig_start = px.bar(starting_avg, x='Airport', y='Avg(fare)', title='Average Fare based on the starting Airport',
                 labels={'Avg(fare)': 'Average Fare ($)'})

    fig_start.update_layout(xaxis_title='Airport', yaxis_title='Average Fare ($)')
    
    st.plotly_chart(fig_start, use_container_width=True)

    st.table(pd.DataFrame(starting_avg, columns=["Airport", "Avg(fare)"]))

    
    fig_destination = px.bar(destination_avg, x='Airport', y='Avg(fare)', title='Average Fare based on the destination Airport',
                 labels={'Avg(fare)': 'Average Fare ($)'})

    fig_destination.update_layout(xaxis_title='Airport', yaxis_title='Average Fare ($)')
    
    st.plotly_chart(fig_destination, use_container_width=True)

    st.table(pd.DataFrame(destination_avg, columns=["Airport", "Avg(fare)"]))

if __name__ == "__main__":
    main()
