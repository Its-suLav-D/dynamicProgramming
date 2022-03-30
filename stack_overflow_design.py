
import enum 
import datetime 
class QuestionStatus(enum.Enum):
  OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4


class QuestionClosingRemark(enum.Enum):
  DUPLICATE, OFF_TOPIC, TOO_BROAD, NOT_CONSTRUCTIVE, NOT_A_REAL_QUESTION, PRIMARILY_OPINION_BASED = 1, 2, 3, 4, 5, 6


class AccountStatus(enum.Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class Account:
    def __init__(self,id,password,name,address,email,phone,status= AccountStatus.ACTIVE):
        self.__id = id 
        self.__password = password
        self.__name = name 
        self.__address = address 
        self.__email = email 
        self.__phone = phone
        self.__status = status 
        self.__reputation = 0  

    def reset_passwod(self):
        None 

class Member:  
    def __init__(self,account):
        self.__account = account 
        self.__badges = [] 
    
    def get_reputation(self): 
        return self.__account.get_reputation() 

    def get_email(self): 
        return self.__account.get_email() 

    def create_question(self,question): 
        None  
    
    def create_tag(self,tag): 
        None 

class Admin(Member): 
    def block_member(self,member): 
        None  
    
    def unblock_member(self,member): 
        None   

class Moderator(Member):
    def close_question(self,question):
        None 
    
    def undelete_question(self,question): 
        None  


class Badge: 
    def __init__(self, name, description):
        self.name = name 
        self.description = description

class Tag: 
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.daily_asked_frequency = 0 
        self.weekly_asked_frequency = 0 


class Notification:
    def __init__(self,id, content): 
        self.notification_id = id 
        self.created_on = datetime.datetime.now()
        self.cotent = content  
    
    def send_notification(self):
        pass 


class Photo:
  def __init__(self, id, path, member):
    self.__photo_id = id
    self.__photo_path = path
    self.__creation_date = datetime.datetime.now()
    self.__creating_member = member

  def delete(self):
    None

# import datetime

 
class Bounty:
  def __init__(self, reputation, expiry):
    self.__reputation = reputation
    self.__expiry = expiry

  def modify_reputation(self, reputation):
    None


class Comment:
  def __init__(self, text, member):
    self.__text = text
    self.__creation_time = datetime.datetime.now()
    self.__flag_count = 0
    self.__vote_count = 0
    self.__asking_member = member

  def increment_vote_count(self):
    None


class Answer:
  def __init__(self, text, member):
    self.__answer_text = text
    self.__accepted = False
    self.__vote_count = 0
    self.__flag_count = 0
    self.__creation_time = datetime.datetime.now()
    self.__creating_member = member
    self.__photos = []

  def increment_vote_count(self):
    None
