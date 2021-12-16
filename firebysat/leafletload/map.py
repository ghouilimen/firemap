from osgeo import gdal
import folium
from folium import plugins
import rasterio as rio
from rasterio.plot import show

#Open raster file
driver=gdal.GetDriverByName('GTiff')
driver.Register() 
in_path ='C:/Users/lenovo/Desktop/firebysat/leafletload/ncd/imgtest3.tif'
ds = gdal.Open(in_path) 
with rio.open(in_path) as src:
    print(src.crs)
    print(src.bounds)
   
if ds is None:
    print('Could not open')

#Get coordinates, cols and rows
geotransform = ds.GetGeoTransform()
cols = ds.RasterXSize 
rows = ds.RasterYSize 

#Get extent
xmin=geotransform[0]
ymax=geotransform[3]
xmax=xmin+cols*geotransform[1]
ymin=ymax+rows*geotransform[5]

#Get Central point
centerx=(xmin+xmax)/2
centery=(ymin+ymax)/2

#Raster convert to array in numpy
bands = ds.RasterCount
band=ds.GetRasterBand(1)
dataset= band.ReadAsArray(0,0,cols,rows)
dataimage=dataset
dataimage[dataimage[:,:]==-340282346638528859811704183484516925440.000]=0

#coloriage
src1=rio.open(in_path)
baands = src1.read()
print(baands)
#Visualization in folium
map= folium.Map(location=[centery, centerx], zoom_start=7,tiles='Stamen Terrain')
folium.raster_layers.ImageOverlay(
    image=dataimage,
    bounds=[[ymin, xmin], [ymax, xmax]],
    colormap=lambda x: (1, 0, x, x),#R,G,B,alpha
    
    

).add_to(map)

#Save html
map.save('./templates/index.html')