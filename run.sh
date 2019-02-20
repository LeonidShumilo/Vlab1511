mkdir /tmp/unzipped
tar xfv data/ldn_data.tar  -C  /tmp/unzipped
gdal_calc.py -A /tmp/unzipped/Ukraine_LPD.tif -B /tmp/unzipped/Ukraine_map_7_cl_trans_00_16_no_city.tif --outfile=/tmp/unzipped/main_degrad.tif --calc="B*(A==1)+0*(A!=1)"
gdal_calc.py -A /tmp/unzipped/Ukraine_LPD.tif -B /tmp/unzipped/Ukraine_map_7_cl_trans_00_16_no_city.tif --outfile=/tmp/unzipped/moderate_degrad.tif --calc="B*(A==2)+0*(A!=2)"
:> data/count.txt
python count.py  >> data/count.txt
