app.layout = html.Div(children=[
    html.H1(children='Compliance Dashboard'),

    html.Div(children='''Overview of compliance metrics.'''),

    dcc.Graph(
        id='compliance-graph',
        figure=px.bar(df, x='Department', y='Compliance', title='Compliance by Department')
    ),

    dcc.Graph(
        id='violations-graph',
        figure=px.pie(df, names='Department', values='Violations', title='Violations by Department')
    )
])
