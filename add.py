def add(*numbers):
    collector=0
    for i in numbers:
        collector=i+collector
    print("addition: ",collector)

add(12,1)