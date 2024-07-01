Two pointers is an extremely common technique used to solve array and string problems. It involves having two integer variables that both move along an iterable. In this article, we are focusing on arrays and strings. This means we will have two integers, usually named something like i and j, or left and right which each represent an index of the array or string.

There are several ways to implement two pointers. To start, let's look at the following method:

Start the pointers at the edges of the input. Move them towards each other until they meet.

Another way to use two pointers
This method where we start the pointers at the first and last indices and move them towards each other is only one way to implement two pointers. Algorithms are beautiful because of how abstract they are - "two pointers" is just an idea, and it can be implemented in many different ways. The following method is applicable when the problem has two iterables in the input, for example, two arrays.

Move along both inputs simultaneously until all elements have been checked.