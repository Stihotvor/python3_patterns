class Subscriber:
    def __init__(self, broker, topic_name, sub_name):
        self.broker = broker
        self.topic_name = topic_name
        self.sub_name = sub_name

    def subscribe(self):
        self.broker.subscribe(sub_name=self.sub_name, topic_name=self.topic_name)

    def pull(self):
        answer = self.broker.pull(sub_name =self.sub_name)
        return answer
