# -*- coding:gb2312 -*-
import is3

from System.Collections.ObjectModel import ObservableCollection
from System.Windows.Media import Colors

##  ���ع��̺���
def LoadPrj():
    print("---Load Project---")
    #is3.mainframe.LoadProject('Example.xml')     #---> ���ع�������XML�ļ�,�滻ExamlpeΪ��Ӧ�������Ƶ�XML
    #is3.prj = is3.mainframe.prj
    #is3.MainframeWrapper.loadDomainPanels()
    return

##  ���ع�����ά   
def add3dview():
    print ("--- Add 3D map ---")
    #is3.addView3d('Map3D', 'Example.unity3d')    #--->  ����unity webplayer������.unity3d �ļ����滻�ļ���
    return

##  ���ع��̶�ά��ͼ
def addBaseMap():
    print("--- Add base map ---")
    #emap = is3.EngineeringMap('BaseMap',10835179,4992323,10835531,4992459, 0.1)    #--->  ���õ�ͼ���ƣ���ͼ����ʾ��Χ��XMin,YMin,XMax,YMax�����ο���ArcMap��  
    #emap.MapType = is3.EngineeringMapType.FootPrintMap                             #--->  ���õ�ͼ����Ϊƽ��ͼ�����Ϳ�ѡ FootPrintMap��ƽ�棩, GeneralProfileMap�����棩
    #emap.LocalTileFileName1 = 'Example.tpk'                                        #--->  ���õ�ͼ�ļ�ΪExample.tpk
    #emap.LocalGeoDbFileName = 'Example.geodatabase'                                #--->  ���õ�ͼ���ݿ��ļ�ΪExample.geodatabase

    #viewWP = is3.MainframeWrapper.addView(emap)                                    #--->  ��ӵ�ͼ��iS3��
    #addMapLayer(viewWP)                                                            #--->  ����ͼ���ݿ�������Ҫ����ʽ��ӵ���ͼ��
    return

##  ����ͼ��Ԫ����ӵ����̵�ͼ��
def addMapLayer(viewWP): 
    #layerDef = is3.LayerDef()
    #layerDef.Name = 'MonPoint'                                                     #--->  ԭ��ArcMap�ڴ��ʱ��Ӧ��ͼ������
    #layerDef.GeometryType = is3.GeometryType.Polygon                               #--->  ͼ��Ҫ�صı�����ʽ��Point���㣩,Polyline������ߣ�,Polygon(��)
    #layerDef.Color = Colors.Green                                                  #--->  ͼ��Ҫ�ص���ɫ
    #layerDef.FillStyle = is3.SimpleFillStyle.Solid
    #layerDef.EnableLabel = True
    #layerDef.LabelTextExpression = '[Name]'
    #layerWrapper = is3.addGdbLayer(viewWP, layerDef)
    return

def Load():
    LoadPrj()                                                                     #--->���ع���
    viewWP1 = addBaseMap()                                                        #--->���ع��̶�ά
    viewWP2 = add3dview()                                                         #--->���ع�����ά

Load()
