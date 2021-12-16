from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse




# Create your views here.

def index(request):
    return render(request,'index.html')

def fwi(request):
    
        data=Dataset(r'..\media\ncd\FWI.GPM.EARLY.v5.Daily.Default.20210614.nc')

        lats = data.variables['lat']
        lons = data.variables['lon']
        time = data.variables['time']
        fwi = data.variables['GPM.EARLY.v5_FWI']

        mp= Basemap(projection ='merc' ,
                    llcrnrlon = 42.8,
                    llcrnrlat = -2 ,
                    urcrnrlon = 105.37 ,
                    urcrnrlat = 38.73 ,
                    resolution ='i')

        lon,lat=np.meshgrid(lons, lats)
        x,y = mp(lon, lat)

        c_scheme= mp.pcolor( x,y , np.squeeze(fwi[0,:,:]), cmap= 'jet')
        mp.drawcoastlines()
        mp.drawstates()
        mp.drawcountries()

        cbar= mp.colorbar(c_scheme, location='right' , pad='10%')

        plt.title('Average temperature on 01-01-1962')
        plt.show()
