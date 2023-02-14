# Generate random toots so that Twitter doesn't block uploads from Bubo-2T

from random import choice
class RandomToots():
    openers = ('Whoop!','Hey!','Look!','Toot!','Toot toot!','Beep Boop', 'It\'s another toot',
    'Incoming message...','Greetings','Hi','Hello','Hey there','Hey there!','Hey there,','Whoop whoop!',
    'Awesomesauce!','OMG!','Look look!','Click!','Snap!','Click click!','Whirrrr','Beep Beep!','Hmm!','Ok!','Now,'
    ,'Incoming...','Incoming message...','Incoming message from Bubo-2T','Message from Bubo-2T,','Bubo-2T says,',
    'Bubo-2T says:','Bubo-2T saw this and thought you might like it,','Bubo-2T saw this and thought you might like it:',
    'Bubo says:','Bubo says,','Bubo saw this and thought you might like it,','Bubo saw this and thought you might like it:',
    'Look what Bubo saw!','Look what Bubo saw:','Look what Bubo saw,','Look what Bubo saw,','Bubo-2T has been busy:',
    'Bubo-2T wants you to know this:','Bubo-2T wants you to know this,','Bubo-2T thought youd like to know...',
    'Bubo-2T wrote this:')
    hashtags = '#robotics'
    messages = ('Here is a great pic!','I just took this.','Smile!','I took this snap.','I just took this pic.',
    'I just took this photo.','I just took this picture','I just took this photograph','I just met these fine folks',
    'I just snapped this.','Look who I just met.','Look who I took a picture of.','Look who I found.',
    'Humanoid detected.','Humanoid detected!,','Humanoid detected:','Humanoid detected...,','Human detected.',
    'Destroy all... wait... I mean look what I saw!','Destroy all... I mean Hello!',
    'Step 1 take a photo of humans, Step 2 destroy all...','Target obtained','target acquired',
    'human subject aquired','Locked on to humanoid subject.','Subject aquired, arming lasers',
    'locking laser beams,','locking on to target','target locked','target acquired','target aquired:','')
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