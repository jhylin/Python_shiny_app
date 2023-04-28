# ***Import all libraries or packages needed***
# Import Shiny ui, app
from shiny import ui, App
# Import shinywidgets
from shinywidgets import output_widget, render_widget
# Import plotly express
import shinyswatch
import plotly.express as px
# Set up requirement.txt file - Pandas & Plotly
import pandas as pd


# ***Specify data source***
# Likely need to convert Polars df into Pandas df - as per Shiny for Python docs
# Trial Pandas version first
df = pd.read_csv("pc_cov_pd.csv")


# User interface---
# Add inputs & outputs
app_ui = ui.page_fluid(
        shinyswatch.theme.darkly(),
        ui.div(
            ui.input_select(
                # Specify x variable input
                "x", label = "Select a molecular property for x axis:", 
                choices = ["Partition coefficients", 
                           "Complexity",
                           "Heavy atom count",
                           "Hydrogen bond donor count",
                           "Hydrogen bond acceptor count",
                           "Rotatable bond count",
                           "Molecular weight",
                           "Exact mass", 
                           "Polar surface area", 
                           "Total atom stereocenter count", 
                           "Total bond stereocenter count"]
                ),
            ui.input_select(
                # Specify y variable input
                "y", label = "Select a molecular property for y axis:",
                choices = ["Partition coefficients", 
                           "Complexity",
                           "Heavy atom count",
                           "Hydrogen bond donor count",
                           "Hydrogen bond acceptor count",
                           "Rotatable bond count", 
                           "Molecular weight",
                           "Exact mass", 
                           "Polar surface area", 
                           "Total atom stereocenter count", 
                           "Total bond stereocenter count"]
                )
            ),
        output_widget("my_widget")    
    )

# Server---
# Add plotting code within my_widget function within the server function
def server(input, output, session):
    @output
    @render_widget
    def my_widget():
        fig = px.scatter(
            df, x = input.x(), y = input.y(), 
            color = "Part_coef_group", 
            hover_name = "Compound name"
        )
        fig.layout.height = 400
        return fig
        
# Combine UI & server into Shiny app
app = App(app_ui, server)