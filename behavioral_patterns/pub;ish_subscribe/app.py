from publisher import Publisher
from subscriber import Subscriber


class Broker:
    def __init__(self):
        self.topics = set()
        self.subscriptions = {}
        self.message_queue = {}

    def create_topic(self, topic_name):
        self.topics.add(topic_name)

    def subscribe(self, sub_name, topic_name):
        if topic_name in self.topics:
            self.subscriptions[topic_name] = sub_name
            self.message_queue[sub_name] = []
        else:
            raise Exception('Topic does not exist')

    def publish(self, topic_name, msg):
        if (topic_name in self.topics) and self.subscriptions[topic_name]:
            self.message_queue[self.subscriptions[topic_name]].append(msg)
        else:
            raise Exception('Topic or subscription does not exist')

    def pull(self, sub_name):
        if self.message_queue.get(sub_name):
            if len(self.message_queue[sub_name]) == 0:
                return []
            else:
                return self.message_queue[sub_name].pop(0)
        else:
            raise Exception('Subscription does not exist')


if __name__ == '__main__':
    topic = 'topic'
    subscription = 'sub'
    mb = Broker()
    pub = Publisher(broker=mb, topic_name=topic)
    sub = Subscriber(broker=mb, topic_name=topic, sub_name=subscription)
    pub.create_topic()
    print(mb.topics)
    sub.subscribe()
    print(mb.subscriptions)
    print(mb.message_queue)
    pub.publish('Hi there')
    message = sub.pull()
    print(message)