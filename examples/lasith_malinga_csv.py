import numpy as np
import pandas as pd
from plots.pitch_densitymap import pitch_densitymap
from plots.pitch_heatmap import pitch_heatmap

df = pd.read_csv('../data/lasith_malinga_csv.csv')

# Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX and stumpsX for plotting
df['pitchX'] = -df['pitchX']
df['stumpsX'] = -df['stumpsX']

# Filter to balls with tracking enabled
balls = df[df['pitchY'] > 0]

# Split balls for RHB and LHB and select pitch co-ords
xy_rh = np.array(balls[balls.rightHandedBat == True][['pitchX', 'pitchY']])
xy = np.array(balls[['pitchX', 'pitchY']])
speeds = balls.ballSpeed * 3.6

title = 'Lasith Malinga'
subtitle_1 = 'Deliveries'
subtitle_2 = 'IPL'
legend_title = 'Speeds'

# pitch_densitymap(xy_rh, title=title, subtitle_1=subtitle_1, subtitle_2=subtitle_2)
pitch_heatmap(xy, speeds, title, subtitle_1, subtitle_2, legend_title, min_balls=6)
