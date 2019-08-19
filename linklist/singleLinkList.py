#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data):
        # private variables
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next

    def setData(self, new_data):
        self.__data = new_data

    def setNext(self, new_next):
        self.__next = new_next


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        new_node = Node(data)
        # first step
        new_node.setNext(self.head)
        # second step
        self.head = new_node


    def deleteNode(self, data):
        current_node = self.head
        previous_node = None
        while current_node != None:
            if current_node.getData() == data:
                break
            previous_node = current_node
            current_node = current_node.getNext()
        # previous node is head node
        if previous_node == None:
            self.head = current_node.getNext()
        else:
            previous_node.setNext(current_node.getNext())


    def isInList(self, data):
        checking = self.head
        while checking != None:
            if checking.getData() == data:
                return True
            checking = checking.getNext()
        return False

    def isEmpty(self):
        return self.head == None

    def makeEmpty(self):
        self.head = None

    def getSize(self):
        size = 0
        current = self.head
        while current != None:
            size += 1
            current = current.getNext()
        return size


