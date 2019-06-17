# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.1.0
# 20:44:19  Dec 15, 2018
# ----------------------------------------------
import sys
import glob
#import jem
"""
from jem.material import add_material,does_material_exist
from jem.modeler3d import create_box,create_rectangle,import_gds
from jem.boundarysetup import assign_lumped_port
from jem.analysis_setup import insert_frequency_sweep, insert_analysis_setup

from  jem.jem import unit
from  jem.jem import parse_tech_file
import xml.etree.ElementTree as ET
"""
########################################################

def em_export(oDesign, fileName):
    oModule=oDesign.GetModule("Solutions")
    try:
        oModule.ExportNetworkData("",["Setup1:Sweep1"],3,fileName,["All"],True,50,"S",-1,0,10,True,True,False)
    except:
        print(fileName, 'is not available')
    #oModule.ExportNetworkData("",["Setup1:Sweep1","Setup1:Sweep2"],3,fileName,["All"],True,50,"S",-1,0,15,True,True,False)
########################################################

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
#sys.path.append("/app/export/jflin/hfss")

oDesktop.RestoreWindow()

oProject = oDesktop.GetActiveProject()


#dsn_list=tl_list + bl_list
ds_list=oProject.GetTopDesignList()
print(ds_list)

for dsn in ds_list:
    oDesign=oProject.SetActiveDesign(dsn)
    fileName='touchstone2/'+dsn+'.snp'
    em_export(oDesign, fileName)

# Save should operate on oProject


oDesktop.RestoreWindow()

######################################################################################
# Import GDS file  


if __name__=="__main__":
    print("run test mode")
