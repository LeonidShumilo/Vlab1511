import gdal
import numpy 

def  get_count_equel(tif_path,chislo,ker):
    raster=gdal.Open(tif_path)
    xsize=raster.RasterXSize
    ysize=raster.RasterYSize
    s=0
    #print(xsize*ysize)
    for i in range(0,xsize,ker):
        for j in range(0,ysize,ker):
            if i+ker>=xsize:
                ker_realx=ker-((i+ker)-xsize)
                #print(xsize,i+ker,ker_realx)
            else:
                ker_realx=ker
            if j+ker>=ysize:
                ker_realy=ker-((j+ker)-ysize)
            else:
                ker_realy=ker
            band=raster.GetRasterBand(1).ReadAsArray(i,j,ker_realx,ker_realy).astype(numpy.float32)
            #print(band.shape)
            s=s+numpy.sum(band==chislo)
            
    s=float(s)*900.0/1000000.0	
    return s
print("Declining productivity [km squared]:")
print("Forest to grassland")
print(get_count_equel('/tmp/unzipped/main_degrad.tif',12,1000))
print("Forest to cropland")
print(get_count_equel('/tmp/unzipped/main_degrad.tif',13,1000))
print("Forest to other")
print(get_count_equel('/tmp/unzipped/main_degrad.tif',16,1000))

print("Moderate decline in productivity [km squared]:")
print("Forest to grassland")
print(get_count_equel('/tmp/unzipped/moderate_degrad.tif',12,1000))
print("Forest to cropland")
print(get_count_equel('/tmp/unzipped/moderate_degrad.tif',13,1000))
print("Forest to other")
print(get_count_equel('/tmp/unzipped/moderate_degrad.tif',16,1000))
