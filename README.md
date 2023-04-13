# cocus_challenge_data_engineer
Hi there,
The code I am attaching contains 3 directories at the root: challenge1, and challenge2, which respect to exercises #1 and #2, respectively, and challenge3 with pdf file with diagrams and solution.

Exercise 1:
To run just call “python3 challenge1.py "*.log" "/var/tmp”.
There is another file containing the test cases. Please change the working directory to "challenge1".
To run just type "pytest" in the command line and the file "test_challenge1.py" will run the test cases.

Please ensure '/var/tmp' exists so tests will fail.

Exercise 2:
There are three folders: oop, thread and thread_split_processes.

Thread directory has a solution approach based on parallel/concurrent programming where each farmer can collect fruit from the tree and no other farmer (excluding cleaners) can be working at the same time.
Thread_split_processes has a solution approach based on parallel/concurrent programming but was coded after my doubts about the exercise were answered.
For that, I divided the process of picking fruits into two: picking fruits, and dropping them into a dirty basket. Also, the process of cleaning was divided in two (like the problem's image suggests)
I assumed that dropping to a dirty basket/clean basket takes 1 second, so the picking instead of (3,6) seconds last (2,5) seconds and the cleaning instead of (2,4) takes (1,3).
This way, another farmer can go to the tree to pick fruit while another one is dropping fruit into the basket.
This is to me the only logical solution once the problem statement mentions no more than one farmer can be picking fruit from a tree at the same time, so would not make sense to have 3 farmers in case the process was not divided.
OOP same logic as the previous one but with a solution approach to the problem based on the OOP paradigm and state-machine without threads.

To run "Thread_split_processes" just change the working directory to this folder.
Inside, there is the main code in the file "farm.py".
To test, there are two other files "test_unit_farm.py" with unit tests and "test_integration.py" with an end-to-end test. To run tests just type "pytest" in the command line.

Case the other two directories (thread and OOP) triggers your curiosity, please just follow the same approach.
In the case of OOP, the class definitions are in one file while the farm simulator is in another file.
