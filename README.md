# rabbitmq-practice
RabbitMQ 실습

### ID / PW : keonmin / 123
sudo rabbitmqctl add_user keonmin 123
sudo rabbitmqctl set_user_tags keonmin administrator

### 접속 (포트포워딩 필요)
localhost:15672

### 현재 큐에 있는 메시지 수 체크
sudo rabbitmqctl list_queues

### 참고링크
- [RabbitMQ 정의 및 설치방법(in Ubuntu)](https://t-okk.tistory.com/169)
- [tutorial - "Hello world!" 실습 (python)](https://t-okk.tistory.com/170)
- [Python에서 RabbitMQ 사용 방법](https://velog.io/@es_seong/RabbitMQ-with-Python)