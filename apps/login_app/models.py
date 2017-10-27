# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def loginVal(self, postData):
        
        results = {
            'status': True,
            'errors': [], 
            'user': None
            }
        
        users = self.filter(user_name = postData['user_name'])
        
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results


    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], user_name = postData['user_name'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user
    
    
    def validate(self, postData):
        results = {
            "status": True,
            "errors": [],
        }
        if len(postData['first_name']) < 3:
            results ['errors'].append('Your first name is too short!')
            results ['status'] = False
        if len(postData['user_name']) < 3:
            results ['errors'].append('Your user name is too short!')
            results ['status'] = False    
        if postData['password'] != postData['C_password']:
            results ['errors'].append('Passwords do not match!')
            results ['status'] = False
        if len(postData['password']) < 8:
            results ['errors'].append('Password needs to be atleast 8 characters!')
            results ['status'] = False 
        if len(self.filter(user_name = postData['user_name'])) > 0:
            results ['errors'].append('User name already exists')
            results ['status'] = False 
            
        if not any(char.isalpha() for char in postData['first_name']):
            results['errors'].append('First name must contain at least one character')
            results['status'] = False
        if not any(char.isalpha() for char in postData['user_name']):
            results['errors'].append('User name must contain at least one character')
            results['status'] = False     
        
        
        return results
    
    
    
class User(models.Model):
    first_name=models.CharField(max_length = 200)
    user_name=models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    objects = UserManager()
