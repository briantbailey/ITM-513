"""
Brian T. Bailey
ITM 513 - MP3
Message Class Module
"""


class Message(object):
    """Message Class
    
    A Message object to hold the text data of the message
    
    Attributes:
        message_text: A String containing the text of the message
    """
    
    def __init__(self, message_text):
        """Inits the Message Class."""
        self.message_text = message_text
    
    def __str__(self):
        """String method for string conversion and output."""
        return self.message_text
    

# Testing
if __name__ == '__main__':
    print('Testing Message Class')
    cls = Message('Text of a Message Object')
    print(cls.message_text)
    print(cls)