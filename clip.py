'''
lastools_delete_duplicate_points_MJB_170424.py

This toolbox is used to run LASTools "lasduplicate" on an entire directory rather than single files.

'''
##############################################
import arcpy, os, shutil, re

arcpy.env.overwriteOutput = True

inFolder = arcpy.GetParameterAsText(0)
clipPoly = arcpy.GetParameterAsText(1)


# Set LasTools path

arcpy.gp.toolbox = r"C:\install\LAStools\ArcGIS_toolbox\LAStools.tbx"
#arcpy.ImportToolbox( r"C:\install\LAStools\ArcGIS_toolbox\LAStools.tbx", 'lastools')

inFiles = [os.path.join(inFolder, fn) for fn in next(os.walk(inFolder))[2]if fn.endswith('.las')]

for f in inFiles:
    arcpy.gp.lasclip(f, clipPoly, "false", "false", "6")
   

	
arcpy.AddMessage("\n"+ "Your sample message here!" + "\n")









