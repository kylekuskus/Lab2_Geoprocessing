
# coding: utf-8

# 

# In[36]:

#Kyle Kusuda 
#Reclassification of a given shapefile from bounds given by a reclassification table.

#import sys
#sys.path.append('C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\bin')
#sys.path.append('C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\arcpy')
#sys.path.append('C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\ArcToolbox\\Scripts')
import arcpy
#arcpy.env.workspace = r"C:\\Users\\kylek_000\\Documents\\geog458 digital\\Lab2_data"
#arcpy.env.overwriteOutput = True

#Parameters

mytable = arcpy.GetParameterAsText(0)                        #Input shapefile
infield = arcpy.GetParameterAsText(1)                        #Infield double
outfield = arcpy.GetParameterAsText(2)                       #Outfield for values (needs to be made)
reclasstable = arcpy.GetParameterAsText(3)                   #Reclasstable with boundaries and the values to be set
notfoundvalue =  arcpy.GetParameterAsText(4)                 #Iterate through each row in shapefile to assign value
outfile = arcpy.GetParameterAsText(5)

#The output file, which will be manipulated further.
outfile = arcpy.CopyFeatures_management(mytable, outfile)

#def reclassify(mytable, infield, outfield, reclasstable, notfoundvalue):
#New field where reclassified values will be added
arcpy.AddField_management(outfile, outfield, "DOUBLE")

with arcpy.da.UpdateCursor(outfile, [infield, outfield]) as uCur:
    #Go through each row in shapefile
    for row in uCur:

        #Go through reclasstable to find the cooresponding value to put in outfield
        with arcpy.da.SearchCursor(reclasstable, ["lowerbound", "upperbound", "value"]) as sCur:
            for bounds in sCur:
                #set outfield to notfoundvalue
                row[1] = notfoundvalue
                uCur.updateRow(row)

                #changes outfield if infield is within bounds
                if row[0] >= bounds[0] and row[0] <= bounds[1]:
                    row[1] = bounds[2]
                    uCur.updateRow(row)
                    break



# In[31]:

#shape = "C:\\Users\\kylek_000\\Documents\\geog458 digital\\Lab2_data\\King.shp"
#field = "PopDens12"
#outfield = "test2"
#reclass = "C:\\Users\\kylek_000\\Documents\\geog458 digital\\Lab2_data\\ReclassTableExample.dbf"
#notfound = "9999"

#reclassify(shape, field, outfield, reclass, notfound)


# In[ ]:



