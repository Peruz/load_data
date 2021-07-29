import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib.dates as mdates

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = '\\usepackage{amsmath, amssymb}'
plt.rcParams['font.size'] = 18
plt.rcParams['legend.fontsize'] = 18
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['xtick.major.size'] = 5.0
plt.rcParams['ytick.major.size'] = 5.0
plt.rcParams['xtick.minor.size'] = 3.0
plt.rcParams['ytick.minor.size'] = 3.0
plt.rcParams['xtick.major.width'] = 1.5
plt.rcParams['ytick.major.width'] = 1.5
plt.rcParams['xtick.minor.width'] = 0.5
plt.rcParams['ytick.minor.width'] = 0.5
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['legend.handlelength'] = 5.0
# plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.color'] = 'grey'
plt.rcParams['grid.linewidth'] = 1.5

fin = sys.argv[1]
# font = {'size': 12}
# matplotlib.rc('font', **font)
data = pd.read_csv(fin, parse_dates=True, index_col=0)
fig, ax = plt.subplots(figsize=(16, 10))
ax.plot(data.index, data['load_kg'], 'k')
plt.fill_between(data.index, ax.get_ylim()[0], data['load_kg'], color=(1, 0.2, 0.2, 0.2))
plt.minorticks_on()
# fig.autofmt_xdate()
# Use a more precise date string for the x axis locations in the toolbar.
# xmajorloc = mdates.DayLocator(bymonthday=[1, 10, 20])
xminorloc = mdates.WeekdayLocator(byweekday=range(0, 7))  # minor every day
xmajorloc = mdates.WeekdayLocator(byweekday=[0])  # major on the first week day
ax.xaxis.set_major_locator(xmajorloc)
ax.xaxis.set_minor_locator(xminorloc)
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
ax.grid(which='major', axis='both', linewidth=1.5, color='gray')
ax.xaxis.grid(True, 'minor', color='gray', alpha=0.3, ls='-', lw=1)
ax.yaxis.grid(True, 'minor', color='gray', alpha=0.3, ls='-', lw=1)
ax.set_ylabel('load kg')
plt.grid('minor')
plt.tight_layout()
fout = fin.replace('csv', 'svg')
plt.savefig(fout)
fout = fin.replace('csv', 'pdf')
plt.show()
