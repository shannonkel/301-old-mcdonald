import plotly.graph_objects as go
import numpy as np
  
  
# creating random data through randomint
# function of numpy.random
np.random.seed(42)
  
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)
  
plot = go.Figure(data=[go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',)
])
  
# Add dropdown
plot.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]
)
  
plot.show()
