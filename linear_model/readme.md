#### attention
1. 继承：  
   ```text
   python3直接写成 super().方法名（参数）
   python2必须写成 super（父类，self）.方法名（参数）
   ```
2. data read  
   自己编写的data_read继承pytorch的父类后一般输出为tuple[Any,Any]是为了将train_data和labels对应的相结合，方便后续打乱，然后未打乱之前是train_data[0]可以直接读取一个data_read和pytorch，打乱后:   
   ```python
   data_iter = iter(train_loader)#取一个batch
   or
   for i, (images, labels) in enumerate(params.train_loader):
   ```