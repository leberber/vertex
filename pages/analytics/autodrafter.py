from dash import  ( 
    Output, Input, callback, clientside_callback, ClientsideFunction, State, ctx,
    register_page, dcc
)
import dash_mantine_components as dmc
from utils.helpers import iconify


register_page(__name__, path="/")

min_step = 0
max_step = 5
active = 1

layout = dmc.Center(
        p = 50,
        style = {"border": "2px solid blue",},
        h = '100vh',
        
    children = [
            dmc.Paper(
            w = '90%',
            radius = 'md',
            p = '20px',
            style = {"boxShadow": "rgba(17, 17, 26, 0.1) 0px 0px 16px"},
            h = '100%',
            children = [
                
                dmc.Stepper(
                    id="stepper-custom-icons",
                    style = {"width": "100%", "height": "100%"},
                    active=active,
                    #  orientation="vertical",
                    children=[
                        dmc.StepperStep(
                            maw = '200px',
                            label="First step",
                            description=dmc.Box("Upload File this a good wy  to  ohhte"),
                            icon=iconify(icon="material-symbols:account-circle"),
                            progressIcon=iconify(icon="material-symbols:account-circle"),
                            completedIcon=iconify(icon="mdi:account-check"),
                            children=[
                                dmc.Text("Step 1 content: Create an account", ta="center")
                            ],
                        ),
                        dmc.StepperStep(
                            label="First step",
                            description="Upload File",
                            icon=iconify(icon="material-symbols:account-circle"),
                            progressIcon=iconify(icon="material-symbols:account-circle"),
                            completedIcon=iconify(icon="mdi:account-check"),
                            children=[
                                dmc.Text("Step 1 content: Create an account", ta="center")
                            ],
                        ),
                        dmc.StepperStep(
                            label="First step",
                            description="Upload File",
                            icon=iconify(icon="material-symbols:account-circle"),
                            progressIcon=iconify(icon="material-symbols:account-circle"),
                            completedIcon=iconify(icon="mdi:account-check"),
                            children=[
                                dmc.Text("Step 1 content: Create an account", ta="center")
                            ],
                        ),
                        dmc.StepperStep(
                            label="Second step",
                            description="Verify email",
                            icon=iconify(icon="ic:outline-email"),
                            progressIcon=iconify(icon="ic:outline-email"),
                            completedIcon=iconify(
                                icon="material-symbols:mark-email-read-rounded"
                            ),
                            children=[dmc.Text("Step 2 content: Verify email", ta="center")],
                        ),
                        dmc.StepperStep(
                            label="Final step",
                            description="Get full access",
                            icon=iconify(icon="material-symbols:lock-outline"),
                            progressIcon=iconify(icon="material-symbols:lock-outline"),
                            completedIcon=iconify(icon="material-symbols:lock-open-outline"),
                            children=[dmc.Text("Step 3 content: Get full access", ta="center")],
                        ),
                        dmc.StepperCompleted(
                            children=[
                                dmc.Text(
                                    "Completed, click back button to get to previous step",
                                    ta="center",
                                )
                            ]
                        ),
                    ],
                ),
                dmc.Group(
                    justify="center",
                    mt="-50px",
                    children=[
                        dmc.Button("Back", id="back-custom-icons", variant="default"),
                        dmc.Button("Next step", id="next-custom-icons"),
                    ],
                ),
            ]
        )
    ]
)


@callback(
    Output("stepper-custom-icons", "active"),
    Input("back-custom-icons", "n_clicks"),
    Input("next-custom-icons", "n_clicks"),
    State("stepper-custom-icons", "active"),
    prevent_initial_call=True,
)
def update_with_icons(back, next_, current):
    button_id = ctx.triggered_id
    step = current if current is not None else active
    if button_id == "back-custom-icons":
        step = step - 1 if step > min_step else step
    else:
        step = step + 1 if step < max_step else step
    return step