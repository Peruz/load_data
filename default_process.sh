flintec_process -f irrigation.csv -b bad_datetimes.csv -t 6:30 16:00 --mavg_side 600 --mavg_max_missing_weight 98 --mavg_central_weight 5 --mavg_side_weight 1
flintec_plot -f irrigation_processed.csv
inkscape irrigation_processed.svg -z -e irrigation_processed.png -d 300
inkscape irrigation_processed.svg
python plot_load_timeseries.py irrigation_processed.csv 
