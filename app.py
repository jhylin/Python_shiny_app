# Shiny in Python at alpha stage
#from shiny import App, render, ui
# post-alpha stage
from shiny import *

# Set up requirement.txt file - Pandas (?only work if changing polars df into pandas df), Plotly
#import plotly.express as px

# User interface
# Add inputs and outputs

# Inputs
app_ui = ui.input_select(
    "Molecular properties", # ID
    "Select a property:", # Label
    {
    "Partition coefficents",
    "Complexitys",
    "Molecular weights",
    "Polar surface areas"
    }
),
# Outputs
ui.output_plot

# Server
def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

# Combine UI & server into Shiny app
app = App(app_ui, server)
