# ***Import all libraries or packages needed***
# Import shiny ui, app
from shiny import ui, App
# Import shinywidgets
from shinywidgets import output_widget, render_widget
# Import shinyswatch to add themes
import shinyswatch
# Import plotly express
import plotly.express as px
# Import pandas
import pandas as pd
# **Set up requirement.txt file - adding pandas, plotly & shinyswatch**


# ***Specify data source***
df = pd.read_csv("pc_cov_pd.csv")


# User interface---
# Add inputs & outputs
app_ui = ui.page_fluid(
        # Add theme
        shinyswatch.theme.superhero(),
        # Add heading
        ui.h3("Molecular properties of compounds used in COVID-19 clinical trials"),
        # Place selection boxes & texts in same row
        ui.row(
            # Divide the row into two columns
            # Column 1 - selection drop-down boxes
            ui.column(
                4, ui.input_select(
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
                           "Total bond stereocenter count"],
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
                )),
            # Column 2 - texts
            ui.column(
                8, ui.p(
                        """
                        This is an example of using PubChem data on compounds used in COVID-19 clinical trials.
                        Source of this dataset can be accessed at: https://pubchem.ncbi.nlm.nih.gov/#tab=compound&query=covid-19%20clinicaltrials.
                        Part_coef_group means partition coefficient groups as shown in the legend on the right. By clicking on each
                        category will remove the data points in the scatter plot. Clicking on the same category will return the data points back to the plot.
                        Hover over each data point to see the compound name and relevant molecular properties."""
                        )              
                ),
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