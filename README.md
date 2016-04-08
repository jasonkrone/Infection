
README by Jason Krone


----------- TECHNOLOGY USED / TO INSTALL ------------

 - Scripts: All of the scripts are writen for python2


 - Graph Library: In my code I make use of the networkx graph library

   1) To install run:   pip install networkx

   link: https://networkx.github.io/documentation/latest/install.html 


 - Tests: I use the nose testing framwork.  

   1)   To install nose run:    pip install nose

   2)   Once nose is installed you can run my tests using:
               nosetests -s test_*.py 



Note: pip is a python package manager. If you do not yet have pip installed
visit       https://pip.pypa.io/en/stable/installing/

------------------- DATA DEFINITIONS ----------------


- User Graph: 


    A User Graph is an undirected networkx.Graph wherein each node
    represents a KA user and there is an edge between two users A and B if and 
    only if there is a coaching relationship between A and B.

    In my code I use the variable name G to refer to User Graphs. 


- Student Graph:


    A Student Graph is an undirected networkx.Graph wherein each node
    represents a student (there are no teacher nodes in this graph). 
    There is an edge between two students A and B if and only if those
    students share a class.


    In a Student Graph connected components represent groups of students
    that share at least one class with each other. This is extremely useful
    for the implementation of limited_infection because by only allowing the  
    spread of a version of the KA website to an entire connected component 
    of students, you can prevent the situation where two students are in the same
    class but are looking at different versions of the website.


    In my code I use the variable name SG to refer to Student Graphs.


------------------ OVERVIEW OF FILES ----------------


 - user: User class, which represents KA users.


 - infection: Contains implementation of total_infection and limited_infection.


 - utils: Implementation of subset_sum_within_range, a variation of subset
   sum that returns a subset that sums to a given number within the given range.
   This is used in the implementation of limited_infection to ensure that we
   only infect components if we can garantee that the total sum of students infected
   will be in the desired range.


 - graph_generator: Random graph generator class, which creates both user graphs
   and student graphs to be used for testing.


 - test_infection: Randomized testing class that ensures the correctness of 
   total_infection and limited infection.


 - test_utils: Testing class for utils function subset_sum_within_range.



