# Contact Tracker

Core functionality of a new professional contact management solution.

## <a name="Features"></a>Features

* Represents users personal information, profile image, location details
* Allows for bi-directional connections between users
* Calculates the degrees of separation between two users

## <a name="Data"></a>Data Structure

![Data Model Graphic](https://raw.githubusercontent.com/yvonneyeh/contact-tracker/main/data-model.png)

## Design Decisions

* Determining Breadth-First Search was the algorithm I wanted to used to find shortest path between 2 users
* Using a Deque (double-ended queue) for the queue in my BFS function, rather than a list. This greatly improves the runtime while popping from the front of the queue.
* Decimal type for Latitude/Longitude (rather than Float) - float is used to store approximate values, not exact values. It has a precision from 1 to 53 digits. I converted to using Decimal instead to preserve precision.

## About the Developer

[**Yvonne Yeh**](http://yvonneyeh.com/) is a software engineer from the Silicon Valley who has never seen the show. Curiosity, creativity, and a love of learning are at the root of everything Yvonne does. She loves that coding because it's an art form, it tickles her brain in the same spot as designing does. Before she learned how to code, she worked in K-12 education, design, and mental/physical fitness. Her personal coding journey began when she was learning alongside her 3rd grade students; she helped introduce **Hour of Code** and **Computer Science Week** into her school’s permanent curriculum. From there she dove into self-study with Scratch, CS50x, Python 4 Everybody, YouTube videos, and Codecademy. She is currently the **Chapter Leader** of [Codecademy's Silicon Valley Chapter](https://community.codecademy.com/silicon-valley/).