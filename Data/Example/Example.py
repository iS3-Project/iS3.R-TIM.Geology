# -*- coding:gb2312 -*-
import is3

from System.Collections.ObjectModel import ObservableCollection
from System.Windows.Media import Colors

##  加载工程函数
def LoadPrj():
    print("---Load Project---")
    #is3.mainframe.LoadProject('Example.xml')     #---> 加载工程配置XML文件,替换Examlpe为对应工程名称的XML
    #is3.prj = is3.mainframe.prj
    #is3.MainframeWrapper.loadDomainPanels()
    return

##  加载工程三维   
def add3dview():
    print ("--- Add 3D map ---")
    #is3.addView3d('Map3D', 'Example.unity3d')    #--->  加载unity webplayer发布的.unity3d 文件，替换文件名
    return

##  加载工程二维底图
def addBaseMap():
    print("--- Add base map ---")
    #emap = is3.EngineeringMap('BaseMap',10835179,4992323,10835531,4992459, 0.1)    #--->  设置底图名称，底图的显示范围（XMin,YMin,XMax,YMax），参考自ArcMap内  
    #emap.MapType = is3.EngineeringMapType.FootPrintMap                             #--->  设置底图类型为平面图，类型可选 FootPrintMap（平面）, GeneralProfileMap（剖面）
    #emap.LocalTileFileName1 = 'Example.tpk'                                        #--->  设置底图文件为Example.tpk
    #emap.LocalGeoDbFileName = 'Example.geodatabase'                                #--->  设置底图数据库文件为Example.geodatabase

    #viewWP = is3.MainframeWrapper.addView(emap)                                    #--->  添加底图到iS3内
    #addMapLayer(viewWP)                                                            #--->  将底图数据库内容以要素形式添加到底图上
    return

##  将底图上元素添加到工程底图上
def addMapLayer(viewWP): 
    #layerDef = is3.LayerDef()
    #layerDef.Name = 'MonPoint'                                                     #--->  原先ArcMap内打包时对应的图层名称
    #layerDef.GeometryType = is3.GeometryType.Polygon                               #--->  图层要素的表现形式，Point（点）,Polyline（多段线）,Polygon(面)
    #layerDef.Color = Colors.Green                                                  #--->  图层要素的颜色
    #layerDef.FillStyle = is3.SimpleFillStyle.Solid
    #layerDef.EnableLabel = True
    #layerDef.LabelTextExpression = '[Name]'
    #layerWrapper = is3.addGdbLayer(viewWP, layerDef)
    return

def Load():
    LoadPrj()                                                                     #--->加载工程
    viewWP1 = addBaseMap()                                                        #--->加载工程二维
    viewWP2 = add3dview()                                                         #--->加载工程三维

Load()
