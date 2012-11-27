'''
Created on 21 Nov 2012

@author: chris
'''

from pickle import dump, load
from dictionaries import node_file, relationship_file, time_relationship_file

class GraphInterface(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        #try:
        node = open(node_file, 'r')
        relationship = open(relationship_file, 'r')
        time_relationships = open(time_relationship_file, 'r')
        try:
            self.nodes = load(node)
        except EOFError:
            self.nodes = dict()
        
        try:
            self.relationships = load(relationship)
        except EOFError:
            self.relationships = dict()
        
        try:
            self.time_relationships = load(time_relationships)
        except EOFError:
            self.time_relationships = dict()
        
        node.close()
        relationship.close()
        time_relationships.close()
    
    
    def close(self):
        '''
        This method stores the data into pickled files
        '''
        node = open(node_file, 'w')
        relationship = open(relationship_file, 'w')
        time_relationship = open(time_relationship_file, 'w')
        dump(self.nodes, node)
        dump(self.relationships, relationship)
        dump(self.time_relationships, time_relationship)
        node.close()
        relationship.close()
        time_relationship.close()


    def print_stuff(self):
        '''
        This is a pickle test method
        '''
        print "\n".join(("Dictionary of Nodes", str(self.nodes)))
        print "###########################################################"
        print "###########################################################"
        print "\n".join(("Dictionary of Relationships", str(self.relationships)))
        print "###########################################################"
        print "###########################################################"
        print "\n".join(("Dictionary of Time Relationships", str(self.time_relationships)))
    
    
    def add_node(self, node_type, name, in_dict):
        '''
        Generic method for adding a node
        '''
        try:
            self.nodes[node_type]
        except KeyError:
            self.nodes[node_type] = dict()
            
        try:
            self.nodes[node_type][name] = in_dict
        except KeyError:
            raise
    
    
    def get_node(self, node_type, name):
        '''
        Generic method for getting all node information
        '''
        return self.nodes[node_type][name]
    
    
    def add_relationship(self, rel_type, node1, node2, rel_dict, one_way=False):
        '''
        This is a generic method for adding a relationship
        '''
        if not isinstance(rel_dict, list):
            rel_dict = [rel_dict]
            
        try:
            self.relationships[rel_type]
        except KeyError:
            self.relationships[rel_type] = dict()
        
        try:
            self.relationships[rel_type][node1]
        except KeyError:
            self.relationships[rel_type][node1] = dict()
        
        try:
            self.relationships[rel_type][node1][node2] = rel_dict
        except KeyError:
            raise
        if not one_way:
            try:
                self.relationships[rel_type][node2]
            except KeyError:
                self.relationships[rel_type][node2] = dict()
        
            try:
                self.relationships[rel_type][node2][node1] = rel_dict
            except KeyError:
                raise
        
    
    def add_timed_relationship(self, rel_type, date, node1, node2, rel_dict, one_way=False):
        '''
        This is a generic method for adding a relationship
        '''
        if not isinstance(rel_dict, list):
            rel_dict = [rel_dict]
        
        try:
            self.time_relationships[date]
        except KeyError:
            self.time_relationships[date] = dict()
        
        try:
            self.time_relationships[date][rel_type]
        except KeyError:
            self.time_relationships[date][rel_type] = dict()
        
        try:
            self.time_relationships[date][rel_type][node1]
        except KeyError:
            self.time_relationships[date][rel_type][node1] = dict()
        
        try:
            self.time_relationships[date][rel_type][node1][node2] = rel_dict
        except KeyError:
            raise
        if not one_way:
            try:
                self.time_relationships[date][rel_type][node2]
            except KeyError:
                self.time_relationships[date][rel_type][node2] = dict()
        
            try:
                self.time_relationships[date][rel_type][node2][node1] = rel_dict
            except KeyError:
                raise

    
    def get_relationships(self, rel_type, node):
        '''
        This is a generic method for getting a nodes relationships
        '''
        return self.relationships[rel_type][node]
        
    
    def get_timed_relationships(self, rel_type, date, node):
        '''
        This is a generic method for getting a nodes relationships
        '''
        return self.time_relationships[date][rel_type][node]