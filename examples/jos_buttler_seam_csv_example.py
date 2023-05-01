import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plots.pitch_heatmap import pitch_heatmap


def filter_by_pitch_x_pitch_y(data):
    data = data[(data['pitchX'] >= -2) & (data['pitchX'] <= 2)]
    data = data[(data['pitchY'] >= 0) & (data['pitchY'] <= 14)]
    return data


# Import Jos Buttler data
df = pd.read_csv('../data/jos_buttler_seam_csv.csv')

# Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX for plotting
df['pitchX'] = -df['pitchX']

df = filter_by_pitch_x_pitch_y(df)
seam = ['FAST_SEAM', 'MEDIUM_SEAM', 'SEAM']
df = df[df['batter'] == 'Jos Buttler']
df = df[df['bowlingStyle'].isin(seam)]
df = df[df['rightArmedBowl'] == True]

xy = np.array(df[['pitchX', 'pitchY']])
runs = df.batterRuns

title = 'A Batter'
subtitle_1 = 'All IPL deliveries against right arm seam for a single batter'
subtitle_2 = 'From {0} balls faced with tracking enabled'.format(len(xy))
legend_title = 'Strike Rate'

pitch_heatmap(xy, runs, title, subtitle_1, subtitle_2, legend_title, min_balls=6, show_markers=True,
              measure='strike_rate')

plt.show()
