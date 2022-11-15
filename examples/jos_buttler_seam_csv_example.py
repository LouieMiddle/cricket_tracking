import numpy as np
import pandas as pd
from plots.pitch_heatmap import pitch_heatmap

# Import Jos Buttler data
df = pd.read_csv('../data/jos_buttler_seam_csv.csv')

# Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX and stumpsX for plotting
df['pitchX'] = -df['pitchX']
df['stumpsX'] = -df['stumpsX']

xy = np.array(df[['pitchX', 'pitchY']])
runs = df.batterRuns

title = 'Jos Buttler'
subtitle_1 = 'Batting Strike Rate Zones IPL against seam'
subtitle_2 = 'From {0} balls faced with tracking enabled | Minimum 12 balls per zone'.format(len(xy))
legend_title = 'Strike Rate'

pitch_heatmap(xy, runs, title, subtitle_1, subtitle_2, legend_title, measure='strike_rate')
