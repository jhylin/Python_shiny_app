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
            # Column 1 - selection drop-down boxes x 2
            ui.column(
                4, ui.input_select(
                # Specify x variable input
                "x", label = "x axis:", 
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
                "y", label = "y axis:",
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
            # Column 2 - add texts regarding plots
            ui.column(
            8,
            ui.p("Select different molecular properties as x and y axes to produce a scatter plot."),
            ui.tags.ul(
                ui.tags.li(
                    """
                    Part_coef_group means groups of partition coefficient (xlogp) as shown in the legend on the right""" 
                ), 
                ui.tags.li(
                    """
                    Toggle each partition coefficient category by clicking on the group names"""
                ), 
                ui.tags.li(
                    """
                    Hover over each data point to see compound name and relevant molecular properties"""
                )
            )),
        # Output as a widget (interactive plot)
        output_widget("my_widget"), 
        # Add texts for data source
        ui.row(
            ui.p(
                """
                Data curated by PubChem, accessed from: https://pubchem.ncbi.nlm.nih.gov/#tab=compound&query=covid-19%20clinicaltrials (last access date: 30th Apr 2023)""" 
            )         
        ) 
    )
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