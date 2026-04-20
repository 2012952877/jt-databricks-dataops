from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

def clean_orders():
    print("开始执行跨境物流订单清洗任务...")
    
    # User A 乖乖补上了时区配置
    spark.conf.set("spark.sql.session.timeZone", "America/Mexico_City")
    
    data = [("MX-1001", "Delivered")]
    df = spark.createDataFrame(data, ["order_id", "status"])
    df.write.mode("append").saveAsTable("prd_catalog.mexico_orders.cleaned_data")

if __name__ == "__main__":
    clean_orders()