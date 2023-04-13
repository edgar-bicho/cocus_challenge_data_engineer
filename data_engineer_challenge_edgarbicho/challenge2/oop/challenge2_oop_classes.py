import random

class Tree:
    def __init__(self, INITIAL_NUMBER) -> None:
        self.fruits = INITIAL_NUMBER
        self.hasWorker = False

    def start_collect(self):
        if not self.hasFruits():
            return
        self.hasWorker = True

    def end_collect(self):
        if not self.hasFruits():
            return
        
        if self.hasWorker:
            self.fruits -= 1

        self.hasWorker = False

    def hasFruits(self):
        return True if self.fruits > 0 else False

    

class Basket:
    def __init__(self) -> None:
        self.fruits = 0
    
    def add(self):
        self.fruits+=1
    
    def remove(self):
        self.fruits-=1

    def getFruits(self):
        return self.fruits

    def hasFruits(self):
        return True if self.fruits > 0 else False


class Farmer:
    def __init__(self) -> None:
        self.hasFruitOnHand = False
        self.timeToFinish = 0

    def isBusy (self) -> bool:
        pass

    def fruitsOnHand(self):
        return 1 if self.hasFruitOnHand else 0


class Collector(Farmer):
    def __init__(self) -> None:
        super().__init__()
        self.isPicking = False
        self.isDropping = False

    def pick(self):
        self.isPicking = True
        self.timeToFinish = random.randint(2,5)

    def drop(self):
        self.isDropping = True
        self.timeToFinish = 1

    def isBusy(self) -> bool:
        return True if self.isPicking or self.isDropping else False

    def work(self):
        if not self.isBusy():
            return

        self.timeToFinish-=1
            
    
    def isWorkFinished(self) -> bool:
        return True if self.isBusy() and self.timeToFinish == 0 else False

    def completeWork(self):
        if (self.isPicking):
            self.hasFruitOnHand = True
        if (self.isDropping):
            self.hasFruitOnHand = False
        self.isPicking = False
        self.isDropping = False

    def fruitsOnHand(self):
        return super().fruitsOnHand()
        


class Cleaner(Farmer):
    def __init__(self) -> None:
        super().__init__()
        self.isPulling = False
        self.isCleaning = False

    def pull(self):
        self.isPulling = True
        self.timeToFinish = 1
    
    def clean(self):
        self.isCleaning = True
        self.timeToFinish = random.randint(1,3)

    def isBusy(self) -> bool:
        return True if self.isPulling or self.isCleaning else False


    def work(self):
        if not self.isBusy():
            return

        self.timeToFinish-=1
            

    def isWorkFinished(self) -> bool:
        return True if self.isBusy() and self.timeToFinish == 0 else False

    def completeWork(self):
        if (self.isPulling):
            self.hasFruitOnHand = True
        if (self.isCleaning):
            self.hasFruitOnHand = False
        self.isPulling = False
        self.isCleaning = False

    def fruitsOnHand(self):
        return super().fruitsOnHand()