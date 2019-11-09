from kafka import KafkaProducer
import json
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print(producer)
producer.send('test', {'foo': 'bar'})
