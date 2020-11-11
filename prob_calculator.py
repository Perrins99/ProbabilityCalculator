import copy
import random

class Hat:
    
    def __init__(self,**kwargs):
        self.contents=[]
        colors=list(kwargs.keys())
        
        for x in colors:
            while kwargs[x]>0:
                self.contents.append(x)
                kwargs[x]-=1

    def draw(self,number):
        if number>=len(self.contents):
            return self.contents
        tmp=[]
        for x in range(0,number):
            tmp.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
        return tmp
    
    def draw_with_replacement(self,number):
        dict={}
        loc_contents=copy.deepcopy(self.contents)
        if number>=len(loc_contents):
            number=len(loc_contents)
        
        for i in range(0,number):
            j=random.randint(0,len(loc_contents)-1)
            if loc_contents[j] in dict and dict[loc_contents[j]]>0:
                dict[loc_contents[j]]+=1
                loc_contents.pop(j)
            else:
                dict[loc_contents[j]]=1
                loc_contents.pop(j)

        return dict


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes=0
    balls=list(expected_balls.keys())

    for i in range(0,num_experiments):
        tmp=hat.draw_with_replacement(num_balls_drawn)
        extracted=True
        for x in balls:
            if x not in tmp:  
                extracted=False
                break
        if extracted:
            success=True
            for x in balls:
                if tmp[x]<expected_balls[x]:
                    success=False
                    break
            if success:
                successes+=1

    return successes/num_experiments