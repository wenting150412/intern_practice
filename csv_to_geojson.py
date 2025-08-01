import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 讀取 CSV 檔案（預設為逗號分隔）
df = pd.read_csv('D:/Ting/javascript/Taichung_cesspool.csv', encoding='utf-8')

# 去除欄位名稱前後多餘空白
df.columns = df.columns.str.strip()

# 建立 geometry 欄位
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]

# 建立 GeoDataFrame，指定 EPSG:4326（WGS84）
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

# 輸出為 GeoJSON（含所有屬性）
output_file = 'D:/Ting/javascript/Taichung_cesspool.geojson'
gdf.to_file(output_file, driver='GeoJSON')

print(f"已儲存為：{output_file}")
