import os
import pandas as pd
import geopandas as gpd

elements = os.listdir()

pd.set_option('display.max_colwidth', None)

for element in elements:
    if os.path.isdir(element):
        LinkPath = element + "\\Link.shp"
        if os.path.exists(LinkPath):
            # Shapefile을 읽습니다.
            gdf = gpd.read_file(LinkPath)

            idx = 0
            # Shapefile 데이터를 출력합니다.
            for geom in gdf['geometry']:
                print(str(idx), end=" : ")
                if geom is not None:
                    # print(str(idx) + " : " + geom.wkt.strip())
                    print("\n\t", end="")
                    for point in geom.coords:
                        longitude, latitude = point
                        print(f"({latitude}, {longitude})", end=(" >> "))
                else:
                    print("None", end="")
                idx += 1
                print()

