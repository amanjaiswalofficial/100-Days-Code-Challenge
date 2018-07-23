class student:
    
    def __init__(self,name,course,percent,is_a_boy):
        self.name=name
        self.course=course
        self.percent=percent
        self.is_a_boy=is_a_boy
    
    def distinct(self):
        if (self.percent)>70:
            return True
        else:
            return False
        
    