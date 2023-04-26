# ***Import all libraries or packages needed***
# Import Shiny ui, app
from shiny import ui, App
# Import shinywidgets
from shinywidgets import output_widget, render_widget
# Import plotly express
import plotly.express as px
# Set up requirement.txt file - Pandas & Plotly


# ***Specify data source***
# Likely need to convert Polars df into Pandas df

# User interface
# Add inputs and outputs

# Inputs & outputs
app_ui = ui.page_fluid(
    ui.div(
        ui.input_select(
            "MP1", label = "Select property 1:", 
            choices=["Partition coefficents", "Complexitys"]
        ),
        ui.input_select(
            "MP2", label = "Select property 2:",
            choices=["Molecular weights", "Polar surface areas"]
        )
    ),
    output_widget("my_widget")    
)

# Server
# Add in plot function within the server function
def server(input, output, session):
    @output
    @render_widget
    def my_widget():
        fig = px.scatter(
            df_name, MP1 = input.MP1(), MP2 = input.MP2(), 
            #marginal = "rug"
        )
        fig.layout.height = 280
        return fig
        
# Combine UI & server into Shiny app
app = App(app_ui, server)