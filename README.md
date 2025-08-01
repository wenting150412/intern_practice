關於不同原始檔轉成geojson，都盡可能的讓他們擁有通用性，而不會因為欄位名稱而有所限制  
xlsx2geojson：努力把原始各種不同的經緯度系統都轉換成 EPSG:4326 的經緯度系統，而原始的經緯度系統包括台灣平面經緯度 "TWD97 橫麥卡托 TM2" 等等。當有些資料是空值也把他們轉換成null，否則geojson的格式會錯誤而無法讀取。也盡可能讓她是廣泛性使用的，不會被資料所限制  
xml2geojson：目前沒有遇到平面經緯度的問題，所以單純只有廣泛性的將xml轉成geojson而已  

cesium_v2：建立 3d tiles（載入台中建築物） 
https://wenting150412.github.io/intern_practice/cesium_v2_building.html

cesium_v3：建立 3d tiles（所有縣市之建築物，且擁有點選不同縣市以呈現該縣市之建築物，但尚未將建築物固定在地形的地圖上）
https://wenting150412.github.io/intern_practice/cesium_v3_building.html

cesium_v4：延續cesium_v3，新增偵測使用者的定位並顯示該使用者所在縣市之建築物
https://wenting150412.github.io/intern_practice/cesium_v4_position.html

cesium_v5：載入資料
https://wenting150412.github.io/intern_practice/cesium_v5_data.html
