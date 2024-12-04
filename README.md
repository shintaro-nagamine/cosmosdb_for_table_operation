# cosmosdb for table 操作API
## 概要
WiCON2023 RiCASのIoTデバイスにあるセンサ情報をcosmosdb for tableにデータを挿入、抽出する用に作成したAPI  
またDCON2023 CANDIにて本APIを流用した  
リクエストbodyの定義、変数"Entity",変数"Query"を変更することで移植可能

## 環境
### 使用モジュール
```
azure-cosmosdb-table    1.0.6
fastapi                 0.115.5
pydantic                2.9.2
uvicorn                 0.32.0
```

### インストール
```bash
pip install azure-data-tables
pip install fatapi
pip install pydantic
pip install uvicorn
```

## APIサーバーの起動
```bash
uvicorn cosmosdb_api:app --host 0.0.0.0 --port 80
```
