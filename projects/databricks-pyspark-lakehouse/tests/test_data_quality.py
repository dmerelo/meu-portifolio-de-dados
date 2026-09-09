def test_no_null_customer_ids(spark):
    data = [("1", "a@example.com"), ("2", "b@example.com")]
    df = spark.createDataFrame(data, ["customer_id", "email"])

    assert df.filter("customer_id IS NULL").count() == 0


def test_customer_ids_are_unique(spark):
    data = [("1",), ("2",)]
    df = spark.createDataFrame(data, ["customer_id"])

    assert df.count() == df.select("customer_id").distinct().count()
