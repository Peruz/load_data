flintec_process -f irrigation.csv -b bad_datetimes.csv --mavg_side 2 --mavg_max_missing_weight 90 -o irrigation_raw.csv
flintec_plot -f irrigation_raw.csv
inkscape irrigation_raw.svg -z -e irrigation_raw.png -d 300
inkview irrigation_raw.svg
