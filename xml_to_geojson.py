import xmltodict
import geopandas as gpd
from shapely.geometry import Point

with open("D:/Ting/路燈資料/中區路燈_.xlsx", 'r', encoding='utf-8') as file:
    xml_content = file.read()

# 解析 XML 成 Python 字典
data = xmltodict.parse(xml_content)

# 擷取 <Record> 資料
records = data['ArrayOfRecord']['Record']

# 若只有 1 筆資料也要包成 list
if isinstance(records, dict):
    records = [records]

# 建立 GeoDataFrame 的資料列表
features = []
for record in records:
    try:
        lon = float(record['Longitude'])
        lat = float(record['Latitude'])
        features.append({
            'PRE_NO': record['PRE_NO'],
            'UNIT': record['UNIT'],
            'ROUTE': record['ROUTE'],
            'REASON': record['REASON'],
            'geometry': Point(lon, lat)
        })
    except Exception as e:
        print(f"發生錯誤於 PRE_NO={record.get('PRE_NO', '未知')}：{e}")

# 轉為 GeoDataFrame 並指定 EPSG:4326（WGS84）
gdf = gpd.GeoDataFrame(features, geometry='geometry', crs='EPSG:4326')

# 儲存為 GeoJSON
output_file = 'output.geojson'
gdf.to_file(output_file, driver='GeoJSON')

print(f"已成功儲存為 {output_file}")
