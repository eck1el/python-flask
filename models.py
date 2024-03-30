from sqlalchemy import Column, Integer, String, Boolean

import db

#Creating a class called Tasks
class Tasks(db.Base):

    __tablename__ = "create_task"
    id = Column(Integer, primary_key=True)#Unique ID of each task
    content = Column(String(200), nullable=False)#Task's content(max 200 characters)
    completed = Column(Boolean) #Boolean that shows whether the task has been completed or not

    def __init__(self, content, completed):
        self.content = content
        self.completed = completed

    def __repr__(self):
        return "Task {}:{} ({})".format(self.id, self.content, self.completed)

    def __str__(self):
        return "Task {}:{} ({})".format(self.id, self.content, self.completed)

