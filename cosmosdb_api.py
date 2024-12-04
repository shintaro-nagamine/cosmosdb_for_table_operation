from azure.data.tables import TableServiceClient

# Azureストレージ接続文字列
connection_string = "DefaultEndpointsProtocol=https;AccountName=shintaro-storage;AccountKey=pYcAXcLHAVTAu5UtJ2GcrpndSg3lMuqMG6AeHzAGLyBfpKL6afyZyHtsyjiEZyIMWntVSYncpOAuACDbZsU2Wg==;TableEndpoint=https://shintaro-storage.table.cosmos.azure.com:443/;"

# TableServiceClientの作成
service_client = TableServiceClient.from_connection_string(connection_string)

# テーブルのリストを取得
tables = service_client.list_tables()

for table in tables:
    print(table.name)
