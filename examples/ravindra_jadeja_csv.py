import numpy as np
import pandas as pd
from plots.pitch_densitymap import pitch_densitymap

# Import Moeen Ali data
df = pd.read_csv('../data/ravindra_jadeja_csv.csv')

# Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX and stumpsX for plotting
df['pitchX'] = -df['pitchX']
df['stumpsX'] = -df['stumpsX']

# Filter to balls with tracking enabled
balls = df[df['pitchY'] > 0]

# Split balls for RHB and LHB and select pitch co-ords
xy_rh = np.array(balls[balls.rightHandedBat == True][['pitchX', 'pitchY']])

title = 'Ravindra Jadeja'
subtitle_1 = 'Deliveries to Right-handers'
subtitle_2 = 'IPL'

pitch_densitymap(xy_rh, title=title, subtitle_1=subtitle_1, subtitle_2=subtitle_2)
