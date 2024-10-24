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
def label(label, icon='ets-icons:info-alt-duotone' ):
    return dmc.Group(
    mt = 15,
    gap = 0,
    children = [
        iconify('lets-icons:info-alt-duotone', color = '#80b3ff'), 
        dmc.Text(label, c = '#404040')

    ]
)
options_style  = {'label':{'color':'gray'}}
c = dmc.CheckboxGroup(
            id="checkbox-group",
            label=label('The main purpose of the study is to assess'),
            styles = {'label':{'color':'red'}},
            # description="is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,",
            # withAsterisk=True,
            # mb=10,
            children=dmc.Group(
                [
                    dmc.Checkbox(label="Safety", value="Safety", size="sm", styles =options_style),
                    dmc.Checkbox(label="Efficacy", value="Efficacy", size="sm", styles =options_style),
                    dmc.Checkbox(label="Tolerability", value="Tolerability", size="sm", styles =options_style)
                ],
                pl=25,
            ),
            value=["Safety", "Efficacy"],
        )

r =  dmc.Box(
        children = [
            label("The ICF should reference a"),
            dmc.RadioGroup(
                pl = 25,
            children=dmc.Group([dmc.Radio(l, value=k, styles =options_style) for k, l in [["Study Drug", "Study Drug"], ["Study Product", "Study Product"]]]),
            id="radiogroup-simple",
            value="Study Drug",
            size="md",
            # mb=10,
        )
        ]
    )



s = dmc.Box(
    children  = [
        label( 'have | may have;ICF should state that the subjects ________ the indication.'),
        dmc.Group(
            
            dmc.ChipGroup(
                [
                    dmc.Chip("Have", value="Have",  variant='light',styles =options_style),
                    dmc.Chip("May have", value="May have",  variant='light', styles =options_style),
                ],
                multiple=False,
               
       
                value="Have",
                deselectable=True,
                id="chipgroup-deselect",
            ),
             pl = 25,
            justify="flex-start",
        )
    ]
)


seg =  dmc.Box(
        children = [
        label('Are in-home visits an option for this study?'),
        dmc.SegmentedControl(
            size = 'xs',
             ml = 25,
            id="segmented",
            value="No",
            data=[
                {"value": "Yes", "label": "Yes"},
                {"value": "No", "label": "No"},
     
            ],
            
        )
        ]
    )
t =  dmc.Box(
    children = [
         label('Are in-home visits an option for this study?'),
        dmc.TextInput( pl = 25,  placeholder='Blood samples, study data and samples')
    ]
)




grid = dmc.Grid(
    gutter=20,
    align = 'stretch',
    h= '100%',
    # style = {"border": "2px solid red", "align-items":"stretch"},
    children=[
        dmc.GridCol(dmc.Box([ r,s,t],  p = 10, style = {"boxShadow": "rgba(0, 0, 0, 0.05) 0px 1px 2px 0px", "borderRadius":10}),  span = { 'base': 12, 'md': 6, 'lg': 6, 'xl':6 }),
        dmc.GridCol(dmc.Box([ seg,c], p = 10, style = {"boxShadow": "rgba(0, 0, 0, 0.05) 0px 1px 2px 0px", "borderRadius":15}),  span = { 'base': 12, 'md': 6, 'lg': 6, 'xl':6 }),
    ],

)

g = dmc.SimpleGrid(
    cols={ 'base': 1, 'md': 2, 'lg': 2, 'xl':2 },
    spacing={"base": 10, "sm": "xl"},
    verticalSpacing={"base": "md", "sm": "xl"},
    children=[
            dmc.Box([ r,s,t],  p = 10, style = {"boxShadow": "rgba(0, 0, 0, 0.05) 0px 1px 2px 0px", "borderRadius":10}),
        dmc.Box([ seg,c], p = 10, style = {"boxShadow": "rgba(0, 0, 0, 0.05) 0px 1px 2px 0px", "borderRadius":15})

    ],
)

layout = dmc.Center(
        p = 50,
        # style = {"border": "2px solid blue",},
        h = '100vh',
        
    children = [
            dmc.Paper(
            w = '90%',
            radius = 'md',
            p = '20px',
            style = {"boxShadow": "rgba(17, 17, 26, 0.1) 0px 0px 16px"},
            styles = {'content':{'height':'100%'}},
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
                            
                            description=dmc.Box("Upload Word Doc"),
                            icon=iconify(icon="mynaui:upload-solid"),
                            progressIcon=iconify(icon="mynaui:upload-solid"),
                            completedIcon=iconify(icon="mynaui:upload-solid"),
                            
                            children=[
                                dmc.Center(
                                        dcc.Upload(
                                            style = {'border': '1px dashed rgb(206, 212, 218)',  'borderRadius': '5px', 'maxWidth': '420px'},
                            id='uploader',
                            children=dmc.Stack(id='contents', 
                                               style = {'padding': '1rem 1rem 3.125rem'},
                            children=[
                                iconify('fa6-solid:upload', width = 60, color = '#80b3ff'),
                                dmc.Text('Drag and drop files here to upload.', className='upload-text'),
                                dmc.Button(
                                  
                                    "Select File",
                                      style = {
                                          'position': 'absolute',
                                            'bottom': '-1.2rem',
                                            'width': '15.625rem'
                                    },
                                    id='upload-button',
                                    radius='lg',
                                )
                            ], align='center',)
                        ), 
                        h = '80%'

                                )
                           
                            ],
                        ),
                        dmc.StepperStep(
                            label="Second step",
                            description="Blue Prompts",
                            icon=iconify(icon="fluent:form-multiple-48-regular"),
                            progressIcon=iconify(icon="fluent:form-multiple-48-regular"),
                            completedIcon=iconify(icon="si:fact-check-line"),
                            children=[
                                g
                            ],
                        ),
                        dmc.StepperStep(
                            label="Third step",
                            description="Another Form",
                            icon=iconify(icon="fluent:form-multiple-48-regular"),
                            progressIcon=iconify(icon="fluent:form-multiple-48-regular"),
                            completedIcon=iconify(icon="si:fact-check-line"),
                            children=[
                                dmc.Text("Step 1 content: Create an account", ta="center")
                            ],
                        ),
                        dmc.StepperStep(
                            label="Fourth step",
                            description="Another Form",
                         icon=iconify(icon="fluent:form-multiple-48-regular"),
                            progressIcon=iconify(icon="fluent:form-multiple-48-regular"),
                            completedIcon=iconify(icon="si:fact-check-line"),
                            children=[dmc.Text("Step 2 content: Verify email", ta="center")],
                        ),
                        dmc.StepperStep(
                            label="Final step",
                            description="Review Selection",
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
                    mt="-35px",
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