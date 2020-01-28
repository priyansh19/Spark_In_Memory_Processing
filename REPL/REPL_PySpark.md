# :memo: Working with REPL in PySpark:

Steps to run a simple spark job:

- Open CMD and type 
```
> pyspark
```
- Now write a program in python to insert a sample.txt file and perform following operations:
	
	- Count the total no. of lines in the text file
	- Display the content of the first line of txt file
```python
>>> textfile = sc.textFile(D:\sample.txt")
>>> textfile.count()
6
>>> textfile.first()
u'Priyansh Gupta'
>>> line = textfile.filter(lambda line: "Priyansh Gupta" in line)
>>> line.count()
2

```
