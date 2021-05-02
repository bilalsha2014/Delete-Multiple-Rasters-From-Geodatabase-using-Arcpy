import arcpy



# settings


gdb = r"C:\Users\gjain\Documents\ArcGIS\Default.gdb"


arcpy.env.workspace = gdb



# create a list of rasters in the folder


rasters = arcpy.ListRasters()



# loop through raster in list


for raster in rasters:


    try:


        arcpy.Delete_management(raster)


    except:


        print "Raster '{0}' could not be deleted".format(raster)

