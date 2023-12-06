# Assiging-batches-to-orders-sequentially


Problem Statement:
Imagine a warehouse where the available items are stored as per different batches as indicated in the BATCH table.
Customers can purchase multiple items in a single order as indicated in ORDERS table.

Write an SQL query to determine items for each order are taken from which batch. 
Assume that items are sequencially taken from each batch starting from the first batch.



INPUT	
	
BATCH	
BATCH_ID	QUANTITY
B1	5
B2	12
B3	8
	
ORDERS	
ORDER_NUMBER	QUANTITY
O1	2
O2	8
O3	2
O4	5
O5	9
O6	5
![image](https://user-images.githubusercontent.com/84965287/232353286-8782ae24-f87d-4817-b584-4643cd38ab91.png)

EXPECTED OUTPUT		
		
ORDER_NUMBER	BATCH_ID	QUANTITY
 	B1	2
O2	B1	3
O2	B2	5
O3	B2	2
O4	B2	5
O5	B3	8
O5	NULL	NULL
O6	NULL	NULL
![image](https://user-images.githubusercontent.com/84965287/232353302-2bb200ec-b8d7-487a-9bef-441ca470888c.png)



