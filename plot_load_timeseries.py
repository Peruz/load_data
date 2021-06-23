import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib.dates as mdates


fin = sys.argv[1]
font = {'size': 12}
matplotlib.rc('font', **font)
data = pd.read_csv(fin, parse_dates=True, index_col=0)
fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(data.index, data['load_kg'], 'k')
plt.fill_between(data.index, ax.get_ylim()[0], data['load_kg'], color=(1, 0.2, 0.2, 0.2))
plt.minorticks_on()
fig.autofmt_xdate()
# Use a more precise date string for the x axis locations in the toolbar.
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.grid(which='major', axis='both', linewidth=1.5, color='gray')
ax.xaxis.grid(True, 'minor', color='gray', alpha=0.3, ls='-', lw=1)
ax.yaxis.grid(True, 'minor', color='gray', alpha=0.3, ls='-', lw=1)
ax.set_ylabel('load kg')
plt.grid('minor')
plt.tight_layout()
fout = fin.replace('csv', 'pdf')
plt.savefig(fout)
plt.show()
