from shiny import App, render, ui

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
