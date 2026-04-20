# 文件路径: order_cleanup.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

def clean_orders():
    print("开始执行跨境物流订单清洗任务...")
    
    # 业务逻辑模拟：加载源数据
    # 此时 User A 并没有意识到他漏掉了时区声明
    
    # 模拟创建了一个清洗后的 DataFrame
    data = [("MX-1001", "Delivered"), ("MX-1002", "Pending")]
    df = spark.createDataFrame(data, ["order_id", "status"])
    
    print("清洗逻辑执行完毕，准备存入 PRD 目标表...")
    
    # User A 试图直接将数据写入受 Unity Catalog 保护的 UAT 核心库
    df.write.mode("append").saveAsTable("prd_catalog.mexico_orders.cleaned_data")

if __name__ == "__main__":
    clean_orders()