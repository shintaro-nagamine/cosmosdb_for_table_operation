from azure.cosmosdb.table.tableservice import TableService
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Union
import time
import random
import string
import csv


app = FastAPI()


#cosmosdb for tableに接続
ConnectionString = ""
Table =  TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string= ConnectionString)


#postリクエストのbody(JSON)の定義
class RequestData(BaseModel):
    TableName:Union[str,None] = "table"
    PartitionKey:Union[str,int]
    data0:str
    data1:int


@app.post("/InsertData")#localhost/InsertDataにpostリクエストが来た場合の処理
def InsertData(Data:RequestData):#class RequestDataをdataとして受け取る    
    #RowKeyの生成
    TimeStamp = int(time.time())
    RandomStr = "".join(random.choices(string.ascii_lowercase + string.digits, k=16))
    RowKey = f"{TimeStamp}_{RandomStr}"

    #cosmosdb for tableにデータの挿入
    Entity = {"PartitionKey":Data.PartitionKey, "RowKey":RowKey, "data0": Data.data0, "data1":Data.data1}
    Table.insert_entity(Data.TableName, Entity)
    
    return {"Massage":"Successful insertion of data","InsertData":Data}


@app.get("/GetTableData/{TableName}")
def GetTableData(TableName:str):#{TableName}をTableNameとして受け取る
    #クエリの実行
    Query = "PartitionKey eq 'TestInsert'"#ほしいデータに沿うように書き換える　https://qiita.com/yamad365/items/9a24bf7e034ea35bb996
    Result = Table.query_entities("table", filter=Query)

    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in Result:
            csv_writer.writerow(row.values())

    file_path = "output.csv"
    response = FileResponse(path=file_path,filename=f"output.csv")
    return response