import plotly.express as px

def plot_data(df, countries):
    """
    Plot GDP data for the specified countries using Plotly.

    Parameters:
    - df (DataFrame): The combined GDP data with columns ['Date', 'GDP', 'Country']
    - countries (list): List of countries to plot

    Returns:
    - None
    """
    # Filter data for the selected countries
    filtered_df = df[df["Country"].isin(countries)]

    # Create the plot using Plotly
    fig = px.line(
        filtered_df,
        x="Date",
        y="GDP",
        color="Country",
        title="GDP Data from 2000 to 2022",
        labels={"GDP": "GDP (in current USD)", "Date": "Year"},
        line_shape="linear",
    )

    # Customize the figure layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Nominal GDP, Index, Jan 2000 = 100",
        legend_title="Country",
        template="plotly_white",
        width=900,
        height=600,
    )

    # Show the plot
    fig.show()
