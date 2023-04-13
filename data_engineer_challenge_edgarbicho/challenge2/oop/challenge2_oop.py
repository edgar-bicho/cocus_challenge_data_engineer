from challenge2_oop_classes import *
import time, datetime

INITAL_FRUITS_NUMBER = 50
tree = Tree(INITAL_FRUITS_NUMBER)
dirty_basket = Basket()
clean_basket = Basket()
farmer1 = Collector()
farmer2 = Collector()
farmer3 = Collector()
farmer4 = Cleaner()
farmer5 = Cleaner()
farmer6 = Cleaner()
collectors = [farmer1, farmer2, farmer3]
cleaners = [farmer4, farmer5, farmer6]
farmers = [collectors, cleaners]

while(tree.hasFruits()):

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"- tree", tree.fruits, "- dirty basket", dirty_basket.fruits, "- clean_basket", clean_basket.fruits, "- farmer1", farmer1.fruitsOnHand(), "- farmer2", farmer2.fruitsOnHand(), "- farmer3", farmer3.fruitsOnHand(),  "- cleaner1", farmer4.fruitsOnHand(),  "- cleaner2", farmer5.fruitsOnHand(),  "- cleaner3", farmer6.fruitsOnHand())

    # end previous cycle
    for index, collector in enumerate(collectors):
        if collector.isPicking and collector.isWorkFinished():
            collector.completeWork()
            tree.end_collect()
            collector.drop()
            print("collector", index+1, "dropping.")
        if collector.isDropping and collector.isWorkFinished():
            collector.completeWork()
            dirty_basket.add()
            print("collector", index+1, "finished.")

    for index, cleaner in enumerate(cleaners):
        if cleaner.isPulling and cleaner.isWorkFinished():
            cleaner.completeWork()
            cleaner.clean()
            dirty_basket.remove()
            print("cleaner", index+1,"cleaning.")
        if cleaner.isCleaning and cleaner.isWorkFinished():
            cleaner.completeWork()
            clean_basket.add()
            print("cleaner", index+1, "finished.")


    # start new cycle
    for index, collector in enumerate(collectors):
        if not collector.isBusy() and tree.hasFruits() and not tree.hasWorker:
            tree.start_collect()
            collector.pick()
            print("collector",index+1, " picking." )

    iter = 1
    for index, cleaner in enumerate(cleaners):
        if not cleaner.isBusy() and dirty_basket.hasFruits():
            cleaner.pull()
            print("cleaner", index+1, "pulling.")
        if iter == dirty_basket.fruits:
            break # cant remove more fruits from dirty basket that actually exist
        iter+=1


    total_fruits_farmers = 0
    # work
    for farmer_category in farmers:
        for specific_farmer in farmer_category:
            specific_farmer.work()
            total_fruits_farmers += specific_farmer.fruitsOnHand()

    if tree.fruits+dirty_basket.fruits+clean_basket.fruits+total_fruits_farmers!=INITAL_FRUITS_NUMBER:
        print("Houston, we have a problem!")

    
    time.sleep(1)
