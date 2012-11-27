'''
Created on 15 Nov 2012

@author: chris
'''

from math_solver import resolve_points
from graph_interface import GraphInterface

from datetime import date
from datetime import timedelta


class Interface(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor:
        Instantiates the graph interface
        '''
        self.graph = GraphInterface()
    
    
    def add_user(self, name, user_dict):
        '''
        This method is for adding a new user with the user dictionary which only adds the information that was provided by the user
        '''
        self.graph.add_node('users', name, user_dict)
    
    
    def get_user(self, name, info_list):
        '''
        This method gets the user and the info requested if it exists
        '''
        temp_dict = dict()
        user = self.graph.get_node('users', name)
        for key, value in user.items():
            if key in info_list:
                temp_dict[key] = value
        
        return temp_dict
    
    
    def add_activity(self, name, act_dict):
        '''
        This adds a new activity to the list if it did not exist before
        '''
        self.graph.add_node('activity', name, act_dict)
    
    
    def get_activity(self, name):
        '''
        This methods gets the all the information about the activity
        '''
        return self.graph.get_node('activity', name)
    
    
    def make_friends(self, user1, user2):
        '''
        This is a method for making users friends
        '''
        self.graph.add_relationship('friends', user1, user2, {})
    
    
    def view_friends(self, user):
        '''
        This is a method for getting a dictionary of a user's friends
        '''
        return self.graph.get_relationships('friends', user).keys()
    
    
    def get_completed_activities(self, user, date):
        '''
        This method gets the activities the user has completed
        '''
        #checks user exists
        try:
            self.get_user(user, {})
        except KeyError:
            raise
        
        return self.graph.get_timed_relationships('activity', date, user)
    
    
    def add_completed_activity(self, user, activity, details_dict):
        '''
        This adds a link between a user and an activity
        '''
        #checks if the activity exists
        try:
            curr_act = self.get_activity(activity)
        except KeyError:
            raise
        
        try:
            relationships = self.get_completed_activities(user, details_dict["date"])
        except KeyError:
            relationships = dict()
        
        try:
            rel_dict = relationships[activity]
        except KeyError:
            rel_dict = list()
        
        temp_dict = details_dict
        temp_dict.update(curr_act)
        
        details_dict["total_points"] = resolve_points(details_dict["equation"], temp_dict)#curr_act["points"] * details_dict["units"]
        
        rel_dict.append(details_dict)
        
        self.graph.add_timed_relationship('activity', details_dict["date"], user, activity, rel_dict, one_way=True)
    
    
    def view_friends_activity(self, name, number, time):
        '''
        This views a friends activity for the last 'number' of times before 'time'
        '''
        friends = self.view_friends(name)
        activities = dict()
        date = time #TODO: Convert time to datt
        for friend in friends:
            activities[friend] = self.get_completed_activities(friend, date)
        
        return activities
    
    def send_message(self, sender, receiver, mess_dict):
        '''
        This method is for adding a message to the graph
        '''
        try:
            self.get_user(sender, [])
        except:
            raise
        
        try:
            self.get_user(receiver, [])
        except:
            raise
        
        
        self.graph.add_timed_relationship("message", mess_dict["date"], receiver, sender, mess_dict, one_way=True)
        
    
    def get_received_messages(self, user, num, date, time):
        '''
        This method is for getting the messages received by a user
        '''
        try:
            self.get_user(user, [])
        except:
            raise
        
        temp = []
        query_date = date.today()
        next_day = timedelta(days=1)
        
        while len(temp) < num and query_date >= date:
            temp.append(self.graph.get_timed_relationships("message", str(query_date), user))
            query_date -= next_day
        
        return temp
        