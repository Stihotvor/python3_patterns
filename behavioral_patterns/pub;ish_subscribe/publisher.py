class Publisher:
    def __init__(self, broker, topic_name):
        self.broker = broker
        self.topic_name = topic_name

    def create_topic(self):
        self.broker.create_topic(topic_name=self.topic_name)

    def publish(self, msg):
        self.broker.publish(topic_name=self.topic_name, msg=msg)
