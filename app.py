


from dash import (
    Dash, html, ALL, dcc, callback, Input, Output, State, 
    clientside_callback, ClientsideFunction,
    _dash_renderer, page_registry, page_container, no_update, set_props
)
from flask import Flask, request, redirect, session, url_for
import json, os
import dash_mantine_components as dmc

from authlib.integrations.flask_client import OAuth

# Internal Imports
from components.header import header
from components.sidebar import sidebar
from utils.helpers import iconify
from appconfig import stylesheets

_dash_renderer._set_react_version("18.2.0")


 

# server = Flask(__name__)
# server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

app = Dash(
    __name__,  use_pages=True,
    external_stylesheets=stylesheets,
)

# server = app.server

# oauth = OAuth(server)



# app.layout = dmc.MantineProvider(
#     id="mantine-provider",
#     children = [
#         dmc.AppShell(
#             id="app-shell",
#             navbar={ "breakpoint": "md", "collapsed": {"mobile": True}},
#             children = [
#                 dcc.Location(id="url"),
#                 dmc.AppShellHeader(header()),
#                 dmc.AppShellNavbar(sidebar, withBorder=True),
#                 dmc.AppShellMain(page_container),
#             ]
#         )
#     ]   
# )
sidebar = dmc.Box(
    children = [
         dmc.NavLink(
            label="Home",
            leftSection=iconify(icon="solar:home-2-line-duotone", width = 20),
            href='/'
        ),
        dmc.NavLink(
            label="Autodrafter",
            leftSection=iconify(icon="hugeicons:analytics-02", width = 20),
            href='/autodrafter'
        ),
        dmc.NavLink(
            label="Secret",
            leftSection=iconify(icon="solar:lock-keyhole-minimalistic-unlocked-line-duotone", width = 20),
            href='/secret'
        ),

        ]
    )

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    children=[
        dmc.Box(
            sidebar, 
            id='sidebar', 

        ),
        dmc.Box(
            id='container',
            pos = 'relative',
            
            children = [
                dmc.ActionIcon(
                    style = {'position':'absolute', 'left':'0px', 'top':'0px' },
                    size="md",
                    variant = 'subtle',
                    id="hide-show-side-bar",
                    color='gray',
                    n_clicks=0,
                    children = iconify(icon = 'hugeicons:menu-02')
                ),
                page_container
            ]
        )
    ]
)



# @callback(
#    Output("sidebar", "style"),
#     Output("container", "style"),
#     Input("hide-show-side-bar", "n_clicks")
# )
# def display_output(n_clicks):
#     print(n_clicks) 
#     return no_update
    
# clientside_callback(
#     """function maximize_chart(n_clicks) {
#         console.log(n_clicks)
#         const no_update = window.dash_clientside.no_update
#         return no_update
     
#     }
#     """,
#      Output("sidebar", "style"),
#     Output("container", "style"),
#     Input("hide-show-side-bar", "n_clicks"),
#      prevent_intial_call = True
 
# )


clientside_callback(
    ClientsideFunction(
        namespace='helpers',
        function_name='hide_show_sidebar'
    ),
Output("sidebar", "style"),
Output("container", "style"),
Input("hide-show-side-bar", "n_clicks")
)

if __name__ == "__main__":
    app.run_server(debug=True, port= 8050)

