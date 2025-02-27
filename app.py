

import base64
import io
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_blueprint_components as dbc
import h5py

color_codes = {
    'b': 16711680,
    'g': 32640,
    'r': 255,
    'c': 12582720,
    'p': 12744675,
    'm': 12517567,
    'y': 49087,
    'o': 950271,
    'k': 0,
    'w': 16777215,
    'tab10:1': 11826975,
    'tab10:2': 950271,
    'tab10:3': 2924588,
    'tab10:4': 2631638,
    'tab10:5': 12412820,
    'tab10:6': 4937356,
    'tab10:7': 12744675,
    'tab10:8': 8355711,
    'tab10:9': 2276796,
    'tab10:10': 13614615,
    'tab20:1': 11826975,
    'tab20:2': 15255470,
    'tab20:3': 950271,
    'tab20:4': 7912447,
    'tab20:5': 2924588,
    'tab20:6': 9101208,
    'tab20:7': 2631638,
    'tab20:8': 9869567,
    'tab20:9': 12412820,
    'tab20:10': 14004421,
    'tab20:11': 4937356,
    'tab20:12': 9739460,
    'tab20:13': 12744675,
    'tab20:14': 13809399,
    'tab20:15': 8355711,
    'tab20:16': 13092807,
    'tab20:17': 2276796,
    'tab20:18': 9296859,
    'tab20:19': 13614615,
    'tab20:20': 15063710,
    'cb10:1': 11826975,
    'cb10:2': 950271,
    'cb10:3': 2924588,
    'cb10:4': 2631638,
    'cb10:5': 12412820,
    'cb10:6': 4937356,
    'cb10:7': 12744675,
    'cb10:8': 8355711,
    'cb10:9': 2276796,
    'cb10:10': 13614615,
    'aliceblue': 16775408,
    'antiquewhite': 14150650,
    'aqua': 16776960,
    'aquamarine': 13959039,
    'azure': 16777200,
    'beige': 14480885,
    'bisque': 12903679,
    'black': 0,
    'blanchedalmond': 13495295,
    'blue': 16711680,
    'bluegray': 13408614,
    'blueviolet': 14822282,
    'brown': 2763429,
    'burlywood': 8894686,
    'cadetblue': 10526303,
    'chartreuse': 65407,
    'chocolate': 1993170,
    'coral': 5275647,
    'cornflowerblue': 15570276,
    'cornsilk': 14481663,
    'crimson': 3937500,
    'cyan': 16776960,
    'darkblue': 9109504,
    'darkcyan': 9145088,
    'darkgray': 11119017,
    'darkgreen': 25600,
    'darkkhaki': 7059389,
    'darkmagenta': 9109643,
    'darkolivegreen': 3107669,
    'darkorange': 36095,
    'darkorchid': 13382297,
    'darkred': 139,
    'darksalmon': 8034025,
    'darkseagreen': 9419919,
    'darkslateblue': 9125192,
    'darkslategray': 5197615,
    'darkturquoise': 13749760,
    'darkviolet': 13828244,
    'darkwashedazure': 13397248,
    'deeppink': 9639167,
    'deepskyblue': 16760576,
    'dimgray': 6908265,
    'dodgerblue': 16748574,
    'firebrick': 2237106,
    'floralwhite': 15792895,
    'forestgreen': 2263842,
    'fuchsia': 16711935,
    'gainsboro': 14474460,
    'ghostwhite': 16775416,
    'gold': 55295,
    'goldenrod': 2139610,
    'gray': 8421504,
    'green': 32768,
    'greenyellow': 3145645,
    'heliotrope': 16737996,
    'honeydew': 15794160,
    'hotpink': 11823615,
    'humbrolgreen': 3394713,
    'indianred': 6053069,
    'indigo': 8519755,
    'ivory': 15794175,
    'khaki': 9234160,
    'lavender': 16443110,
    'lavenderblush': 16118015,
    'lawngreen': 64636,
    'lemonchiffon': 13499135,
    'lightblue': 15128749,
    'lightcoral': 8421616,
    'lightcyan': 16777184,
    'lightgoldenrodyellow': 13826810,
    'lightgray': 13882323,
    'lightgreen': 9498256,
    'lightpink': 12695295,
    'lightsalmon': 8036607,
    'lightseagreen': 11186720,
    'lightskyblue': 16436871,
    'lightslategray': 10061943,
    'lightsteelblue': 14599344,
    'lightyellow': 14745599,
    'lime': 65280,
    'limegreen': 3329330,
    'linen': 15134970,
    'magenta': 16711935,
    'maroon': 128,
    'mediumaquamarine': 11193702,
    'mediumblue': 13434880,
    'mediumorchid': 13850042,
    'mediumpurple': 14381203,
    'mediumseagreen': 7451452,
    'mediumslateblue': 15624315,
    'mediumspringgreen': 10156544,
    'mediumturquoise': 13422920,
    'mediumvioletred': 8721863,
    'midnightblue': 7346457,
    'mintcream': 16449525,
    'mistyrose': 14804223,
    'moccasin': 11920639,
    'navajowhite': 11394815,
    'navy': 8388608,
    'oldlace': 15136253,
    'olive': 32896,
    'olivedrab': 2330219,
    'orange': 42495,
    'orangered': 17919,
    'orchid': 14053594,
    'palegoldenrod': 11200750,
    'palegreen': 10025880,
    'paleturquoise': 15658671,
    'palevioletred': 9662683,
    'papayawhip': 14020607,
    'peachpuff': 12180223,
    'peru': 4163021,
    'pink': 13353215,
    'pistachio': 7521683,
    'plum': 14524637,
    'powderblue': 15130800,
    'purple': 8388736,
    'red': 255,
    'rosybrown': 9408444,
    'royalblue': 14772545,
    'saddlebrown': 1262987,
    'salmon': 7504122,
    'sandybrown': 6333684,
    'seagreen': 5737262,
    'seashell': 15660543,
    'sienna': 2970272,
    'silver': 12632256,
    'skyblue': 15453831,
    'slateblue': 13458026,
    'slategray': 9470064,
    'snow': 16448255,
    'springgreen': 8388352,
    'steelblue': 11829830,
    'sunset': 5066944,
    'tan': 9221330,
    'tangerineyellow': 52479,
    'teal': 8421376,
    'thistle': 14204888,
    'tomato': 4678655,
    'turquoise': 13688896,
    'wheat': 11788021,
    'white': 16777215,
    'whitesmoke': 16119285,
    'violet': 15631086,
    'yellow': 65535,
    'yellowgreen': 3329434,
}
line_codes = {
    'Ac-227':{
		'color':'maroon'
	},
	'Ag-108m':{
		'color':'olive'
	},
	'Am-243':{
		'color':'mediumturquoise'
	},
	'Am-242m':{
		'color':'mediumturquoise',
		'dash':'dash'
	},
	'Am-241':{
		'color':'mediumturquoise',
		'dash':'dashdot'
	},
	'Ar-39':{
		'color':'palegreen'
	},
	'Ba-133':{
		'color':'steelblue'
	},
	'Be-10':{
		'color':'royalblue'
	},
	'C-14':{
		'color':'blue'
	},
	'C-14-org':{
		'color':'blue'
	},
	'C-14-ind':{
		'color':'blue',
		'dash':'dash'
	},
	'C-14-inorg':{
		'color':'blue',
		'dash':'dot'
	},
	'Ca-41':{
		'color':'purple'
	},
	'Cd-113m':{
		'color':'lawngreen'
	},
	'Cl-36':{
		'color':'chocolate'
	},
	'Cm-243':{
		'color':'paleturquoise'
	},
	'Cm-242':{
		'color':'paleturquoise',
		'dash':'dash'
	}, 
	'Cm-244':{
		'color':'paleturquoise',
		'dash':'dot'
	}, 
	'Cm-245':{
		'color':'paleturquoise',
		'dash':'dash'
	}, 
	'Cm-246':{
		'color':'paleturquoise',
		'dash':'dashdot'
	}, 
	'Co-60':{
		'color':'springgreen'
	},
	'Cs-135':{
		'color':'green'
	},
	'Cs-137':{
		'color':'green',
		'dash':'dash'
	}, 
	'Eu-152':{
		'color':'peru'
	},
	'Eu-150':{
		'color':'peru',
		'dash':'dash'
	}, 
	'Gd-148':{
		'color':'yellow'
	},
	'H-3':{
		'color':'mediumblue'
	},
	'Ho-166m':{
		'color':'cornflowerblue'
	},
	'I-129':{
		'color':'dodgerblue'
	},
	'K-40':{
		'color':'saddlebrown'
	},
	'La-137':{
		'color':'cornsilk'
	},
	'Mo-93':{
		'color':'lime'
	},
	'Nb-93m':{
		'color':'tan'
	},
	'Nb-94':{
		'color':'tan',
		'dash':'dash'
	}, 
	'Ni-59':{
		'color':'magenta'
	},
	'Ni-63':{
		'color':'magenta',
		'dash':'dash'
	}, 
	'Np-237':{
		'color':'goldenrod'
	},
	'Pa-231':{
		'color':'darkolivegreen'
	},
	'Pb-210':{
		'color':'darkviolet',
		'dash':'dash'
	}, 
	'Pd-107':{
		'color':'thistle'
	},

	'Po-210':{
		'color':'darkviolet',
		'dash':'dot'
	},
	'Pu-239':{
		'color':'cyan'
	},
	'Pu-242':{
		'color':'cyan',
		'dash':'dash'
	}, 
	'Pu-238':{
		'color':'cyan',
		'dash':'dot'
	}, 
	'Pu-240':{
		'color':'cyan',
		'dash':'dash'
	}, 
	'Pu-241':{
		'color':'cyan',
		'dash':'dashdot'
	},

	'Ra-226':{
		'color':'darkviolet'
	},
	'Ra-228':{
		'color':'darkviolet',
		'dash':'dash'
	}, 
	'Rn-222':{
		'width':0.75
	},
	'Re-186m':{
		'color':'lightsalmon'
	},
	'Se-79':{
		'color':'slategray'
	},
	'Si-32':{
		'color':'moccasin'
	},
	'Sm-151':{
		'color':'blueviolet'
	},
	'Sn-126':{
		'color':'black'
	},
	'Sr-90':{
		'color':'gold'
	},
	'Tb-157':{
		'color':'plum'
	},
	'Tb-158':{
		'color':'plum',
		'dash':'dash'
	}, 
	'Tc-99':{
		'color':'navy'
	},
	'Th-230':{
		'color':'indigo'
	},
	'Th-228':{
		'color':'indigo',
		'dash':'dash'
	}, 
	'Th-229':{
		'color':'indigo',
		'dash':'dot'
	}, 
	'Th-232':{
		'color':'indigo',
		'dash':'dash'
	}, 
	'Ti-44':{
		'color':'orchid'
	},
	'U-238':{
		'color':'red'
	},
	'U-235':{
		'color':'red',
		'dash':'dash'
	}, 
	'U-234':{
		'color':'red',
		'dash':'dot'
	}, 
	'U-233':{
		'color':'red',
		'dash':'dash'
	},
	'U-236':{
		'color':'red',
		'dash':'dashdot'
	}, 
	'U-232':{
		'color':'red',
		'dash':'longdash'
	}, 
	'Zr-93':{
		'color':'lightgreen'
	}
 }
def get_line_style(name):
    line = dict(color=None, dash=None, width=2)
    if name in line_codes:
        line_code = line_codes[name]
        if 'color' in line_code:
            decimal_color = color_codes[line_code['color']]
            red =  decimal_color & 255
            green = (decimal_color >> 8) & 255
            blue =   (decimal_color >> 16) & 255
            line['color'] = f'rgb({red},{green},{blue})'
        if 'dash' in line_code:
            line['dash'] = line_code['dash']
        if 'width' in line_code:
            line['width'] = line_code['width']
    return line
    

global_file_1 = None
global_file_2 = None


app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
app.layout = html.Div([
    dcc.Store(id='file-data-1'),
    dcc.Store(id='file-data-2'),
    html.Div(children=[
        dcc.Upload(
            id='upload-data-1',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select an HDF5 File')
            ]),
            style={
                'width': '99%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px',
            },
            multiple=False
        ),        
        dcc.Upload(
            id='upload-data-2',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select an HDF5 File'),
                ' for comparison'
            ]),
            style={
                'width': '95%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px',
            },
            multiple=False
        )
    ], style={'display': 'grid', 'gridTemplateColumns': '2.5fr 1.5fr'}),
    html.Div([
        dbc.Tree(
            id='input',
            contents=[],
            style={'height': '400px', 'overflow': 'auto', 'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top'}
        ),
        html.Div(id='node-data', style={'width': '95%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'}),
    
    ], style={'display': 'flex'}),  # Use flex display to arrange children side by side
    html.Div(id='filename-1', style={'position': 'fixed', 'bottom': '10px', 'left': '10px', 'backgroundColor': 'lightgrey', 'padding': '5px', 'borderRadius': '5px'}),
    html.Div(id='filename-2', style={'position': 'fixed', 'bottom': '10px', 'right': '10px', 'backgroundColor': 'lightgrey', 'padding': '5px', 'borderRadius': '5px'})
])

def open_hdf5(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    buffer = io.BytesIO(decoded)
    return h5py.File(buffer, 'r')

def hdf5_to_tree(hdf5_group):
    def create_node(name, obj):
        node = {'id': name, 'label': name}
        if isinstance(obj, h5py.Group):
            node['childNodes'] = [create_node(k, v) for k, v in obj.items()]
        return node
    return [create_node(k, v) for k, v in hdf5_group.items()]

def get_id_node(group,path):
    name = list(group.keys())[path[0]]
    if len(path) == 1:
        return name
    return name+'/'+get_id_node(group[name],path[1:])

@app.callback(
    [Output('input', 'contents',allow_duplicate=True),
     Output('filename-1', 'children',allow_duplicate=True),
     Output('file-data-1', 'data',allow_duplicate=True),],
    Input('upload-data-1', 'contents'),
    State('upload-data-1', 'filename'),
    prevent_initial_call=True
)
def update_tree_1(contents, filename):
    global global_file_1
    if contents is None:
        return [], "", None
    global_file_1 = open_hdf5(contents)
    tree_data = hdf5_to_tree(global_file_1)
    return tree_data, f"Loaded file: {filename}",contents

@app.callback(
    [Output('filename-2', 'children',allow_duplicate=True),
     Output('file-data-2', 'data',allow_duplicate=True)],
    Input('upload-data-2', 'contents'),
    State('upload-data-2', 'filename'),
    prevent_initial_call=True
)
def update_tree_2(contents, filename):
    global global_file_2
    if contents is None:
        return "",None
    global_file_2 = open_hdf5(contents)
    return f"Loaded file for comparison: {filename}", contents

@app.callback(
    [Output('input', 'contents',allow_duplicate=True),
     Output('filename-1', 'children',allow_duplicate=True),
     Output('file-data-1', 'data',allow_duplicate=True),
     Output('node-data', 'children',allow_duplicate=True),],
    Input('filename-1', 'n_clicks'),
    prevent_initial_call=True
)
def clear_file_1(n_clicks):
    if 'filename-1' in [p['prop_id'] for p in dash.callback_context.triggered][0]:
    #if n_clicks:
        global global_file_1
        global_file_1 = None
        return [], "", None, ""
    return dash.no_update

@app.callback(
    [Output('filename-2', 'children',allow_duplicate=True),
     Output('file-data-2', 'data',allow_duplicate=True),
     Output('node-data', 'children',allow_duplicate=True),],
    Input('filename-2', 'n_clicks'),
    prevent_initial_call=True
)
def clear_file_2(n_clicks):
    if 'filename-2' in [p['prop_id'] for p in dash.callback_context.triggered][0]:
    #if n_clicks:
        global global_file_2
        global_file_2 = None
        return "",  None, ""
    return dash.no_update

@app.callback(
    Output('graph', 'figure',allow_duplicate=True),
    Input('checkbox-log', 'value'),
    Input('graph', 'figure'),
    prevent_initial_call=True,
)
def toggle_log_x(value,fig):
    if 'log-x' in value:
        fig['layout']['xaxis']['type'] = 'log'
    else:
        fig['layout']['xaxis']['type'] = 'linear'
    if 'log-y' in value:
        fig['layout']['yaxis']['type'] = 'log'
    else:
        fig['layout']['yaxis']['type'] = 'linear'
    return fig



@app.callback(
    Output('node-data', 'children',allow_duplicate=True),
    Input('input', 'clicked_node'),
    prevent_initial_call=True
)
def display_node_data(clicked_node):
    if not clicked_node:
        return ''
    #global global_file
    node_id = get_id_node(global_file_1,clicked_node['path'])
    isnode = isinstance(global_file_1[node_id],h5py.Dataset)
    node_data = f'Attributes of {"node" if isnode else "group"}' if global_file_1[node_id].attrs else ''
    for attr in global_file_1[node_id].attrs:
        node_data += f'\n{attr}: {global_file_1[node_id].attrs[attr]}'
    if isnode:
        node_data += f'\n\nData: \n{global_file_1[node_id][()]}'
    
    if global_file_2 and node_id in global_file_2:
        if global_file_2[node_id].attrs:
            node_data += '\nAttributes in comparison file:'
            for attr in global_file_2[node_id].attrs:
                node_data += f'\n{attr}: {global_file_2[node_id].attrs[attr]}'
        if isinstance(global_file_2[node_id],h5py.Dataset):
            node_data += f'\n\Data in comparison file: \n{global_file_2[node_id][()]}'
    
    if 'time_dependent' in global_file_1[node_id].attrs and global_file_1[node_id].attrs['time_dependent'] and (isnode or 'IndexLists' in global_file_1[node_id].attrs):
        time_data_1 = global_file_1['time'][()]
        if global_file_2 and 'time' in global_file_2:
            time_data_2 = global_file_2['time'][()] if global_file_2 else None
        else:
            time_data_2 = None
        if 'unit' in global_file_1[node_id].attrs:
            unit = global_file_1[node_id].attrs['unit']
        else:
            unit = None
        if 'unit' in global_file_1['time'].attrs:
            time_unit = global_file_1['time'].attrs['unit']
        else:
            time_unit = 'years AD'
        if isnode:
            data = [{'x': time_data_1, 'y': global_file_1[node_id][()], 'type': 'line', 'name': node_id}]
            if time_data_2 is not None and node_id in global_file_2:
                data.append({'x': time_data_2, 'y': global_file_2[node_id][()], 'mode': 'lines','line':dict(color='black',dash='dot'), 'name': f"{node_id} (Compare)"})            
            legend = dict(yanchor="top",y=0.99,xanchor="right",x=0.99)
        else:
            data = []
            for index in global_file_1['IndexLists'][global_file_1[node_id].attrs['IndexLists'][0]]:
                y_data_1 = global_file_1[node_id][index][()]
                name = index.decode() # Since variable length strings are stored as byte sequences in HDF5
                line = get_line_style(name)
                data.append({'x': time_data_1, 'y': y_data_1, 'mode': 'lines', 'line': line, 'name': name})
                if time_data_2 is not None and node_id in global_file_2 and index in global_file_2[node_id]:
                    y_data_2 = global_file_2[node_id][index][()]
                    line = get_line_style(name)
                    line['width'] = 1
                    data.append({'x': time_data_2, 'y': y_data_2, 'mode': 'lines', 'line': line, 'name':name+' (Compare)'})#,'showlegend':False})
            legend = None

        return html.Div([
            html.H5(f'Selected node: {node_id}'),
            dcc.Graph(id='graph',
                      figure = {
                          'data': data,
                          'layout': {
                              'yaxis': {
                                  'type': 'linear', # Set y-axis scale
                                  'title': {'text':f'{clicked_node["label"]} ({unit})'}
                                },
                               'xaxis': {
                                  'type': 'log', # Set x-axis scale
                                  'title': {'text':f'Time ({time_unit})'}
                                },
                               'margin':dict(r=20, t=20),  
                               'legend':legend,                
                          }
                      }, 
                      config= {'displaylogo': False,
                               'scrollZoom': True,
                               'showLink': True,
                               'plotlyServerURL':"https://chart-studio.plotly.com",
                               'modeBarButtonsToAdd':['v1hovermode'],
                               'toImageButtonOptions': {
                                    'format': 'svg', # one of png, svg, jpeg, webp
                                    'filename': 'chart',
                                    'height': 500,
                                    'width': 700,
                                    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
                                }
                               }
                      ),
            html.Div(
                    children=[
                        dcc.Checklist(
                            [{
                                "label": html.Div(['10',html.Sup(html.I('x'))], style={'color': 'black', 'font-size': 12}),
                                "value": "log-x",
                            },
                            {
                                "label": html.Div(['10',html.Sup(html.I('y'))], style={'color': 'black', 'font-size': 12}),
                                "value": "log-y",
                            }],
                            value=['log-x'],
                            id='checkbox-log',
                            labelStyle={"display": "flex", "align-items": "center"},
                        ),
                    ],
                ),
            html.Pre(node_data),
        ])
    return html.Div([
        html.H5(f'Selected node: {node_id}'),
        html.Pre(node_data)
    ])



if __name__ == '__main__':
    app.run_server(debug=True)
    
