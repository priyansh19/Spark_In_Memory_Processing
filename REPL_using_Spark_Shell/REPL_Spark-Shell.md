# :memo: Working with REPL in Spark-Shell:

Steps to run a simple spark job:

- Open Spark-shell 
```
> spark-shell
```
- Now write aprogram to initialise no.'s from 1 t0 50000 and filter them from range 1 to 10.
```scala
scala> val test_data = 1 to 50000
test_data: scala.collection.immutable.Range.Inclusive = Range(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19...)

scala> val samplespark = sc.parallelize(test_data,2)
samplespark: org.apache.spark.rdd.Rdd[Int] = ParallelCollectionRDD[2] at parallelize at <console>:26

scala> samplespark.filter(_ < 10).collect()
res1: Array[Int] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9) 
```
