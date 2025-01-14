 # ������� 4. ��������� �������� � ��� �� �������. ���������� ����� ������ � Kafka ��� �������� �������� ��������������� �����:

1. ��������� Kafka: �������� ���� (��������, random_numbers) ��� �������� ������. 

2. �������� Python-�������� � �������������� ���������� Kafka-Python, ������� ������ ������� ���������� ��������� � Kafka-����. ��������� ������ ��������� ��� ��������� ����� �� 0 �� 100 � ������� JSON.

3. �������� Python-�������� � �������������� ���������� Kafka, ������� ������ ��� ��������� � �������� ������� � ������� �� �� �����.

4. ��������� ��������: ������������ ���������� ������ ��������� �������� (�� ���������� ������), ����� �������� ������� �� Kafka �����, �������� �� ����� � ������� ������ � ��������� ��������� � ����� Kafka-���� (��������, predicted_sums).


���������

1. ������������ �����������

git clone https://github.com/Niktyav/MLModel_in_prod
cd MLModel_in_prod/exam

2. ������ Kafka �������� ����� Docker Compose

docker-compose up -d




Topics:   
![img sel_transormed.png](./img/topics.png)   

Topic "random_numbers" � 3 ����������:   
![img sel_transormed.png](./img/topic_rnd.png)   
Topic "predicted_sums" � 3 ����������:   
![img sel_transormed.png](./img/topic_pred.png)   


��������� docker-compose:
![img sel_transormed.png](./img/docker.png)   
��������� docker-compose:
![img sel_transormed.png](./img/compose.png)   