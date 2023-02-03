# Generate random toots so that Twitter doesn't block uploads from Bubo-2T

from random import choice
class RandomToots():
    openers = ('Whoop!','Hey!','Look!','Toot!','Toot toot!','Beep Boop', 'It\'s another toot',
    'Incoming message...','')
    hashtags = '#robotics'
    messages = ('Here is a great pic!','I just took this.','Smile!','I took this snap.','I just took this pic.',
    'I just took this photo.','I just took this picture','I just took this photograph','I just met these fine folks',
    'I just snapped this.','Look who I just met.','Look who I took a picture of.','Look who I found.')
    def __init__(self):
        pass

    def generate(self):

        opener_text = choice(self.openers)
        hashtag = self.hashtags
        message = choice(self.messages)
        return opener_text + '\n' + message + '\n' + hashtag

    def test(self):
        message = self.generate().replace('\n',' ')
        return message

def main():
    test_toot = RandomToots()
    print(test_toot.generate())

def test():
    test_toot = RandomToots()
    for _ in range(100):
        print(test_toot.test())

if __name__ == '__main__':
    # main()
    test()