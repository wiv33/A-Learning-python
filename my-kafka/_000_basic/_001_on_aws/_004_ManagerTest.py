import unittest

from ._002_manager import KafkaManager


class ManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = KafkaManager()
        self.topics = 'test-python'
        self.msg = "\With all this stuff going down at the moment with MJ i've started listening to his music, " \
                   "watching the odd documentary here and there, watched The Wiz and watched Moonwalker again. " \
                   "Maybe i just want to get a certain insight into this guy who i thought was really cool " \
                   "in the eighties just to maybe make up my mind whether he is guilty or innocent." \
                   " Moonwalker is part biography, part feature film " \
                   "which i remember going to see at the cinema when it was originally released. " \
                   "Some of it has subtle messages about MJ's feeling towards the press and also" \
                   " the obvious message of drugs are bad m'kay.<br /><br />Visually impressive but" \
                   " of course this is all about Michael Jackson so unless you remotely like MJ in anyway then" \
                   " you are going to hate this and find it boring. " \
                   "Some may call MJ an egotist for consenting to the making of this movie BUT MJ and most of" \
                   " his fans would say that he made it for the fans which if true is really nice of him.<br /><br />" \
                   "The actual feature film bit when it finally starts is only on for 20 minutes or so excluding " \
                   "the Smooth Criminal sequence and Joe Pesci is convincing as a psychopathic all powerful drug lord. " \
                   "Why he wants MJ dead so bad is beyond me. Because MJ overheard his plans? " \
                   "Nah, Joe Pesci's character ranted that he wanted people to know it is he who is supplying drugs etc " \
                   "so i dunno, maybe he just hates MJ's music.<br /><br />Lots of cool things in this like " \
                   "MJ turning into a car and a robot and the whole Speed Demon sequence. Also, the director must " \
                   "have had the patience of a saint when it came to filming the kiddy Bad sequence as usually " \
                   "directors hate working with one kid let alone a whole bunch of them performing a complex " \
                   "dance scene.<br /><br />Bottom line, this movie is for people who like MJ on one level or another " \
                   "(which i think is most people). If not, then stay away. It does try and give off a " \
                   "wholesome message and ironically MJ's bestest buddy in this movie is a girl! Michael Jackson " \
                   "is truly one of the most talented people ever to grace this planet but is he guilty? Well, " \
                   "with all the attention i've gave this subject....hmmm well i don't know because people can be" \
                   " different behind closed doors, i know this for a fact. He is either an extremely nice but" \
                   " stupid guy or one of the most sickest liars. I hope he is not the latter."

    def test_should_be_exists_producer_in_manager(self):
        self.manager.send_message(self.topics, 'word2vec-nlp-tutorial', self.msg)
        self.assertIsNotNone(self.manager, msg="manager is not None")

    def test_should_be_failure_none_topic_name(self):
        self.assertRaises(Exception, self.manager.send_message)


if __name__ == '__main__':
    unittest.main()
