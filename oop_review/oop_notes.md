# Notes on Object-Oriented Programming

### What Is Object-Oriented Programming?
* A programming paradigm based on the concept of objects
    * Objects contain data (have **state**)
    * Objects have methods that can access and modify an object's state
    * Objects can interact with other objects via their methods
* OOP is popular because its main idea is to closely reflect the structure and interactions of systems in the real world

### Some Vocab
* Coupling (interdependece): when one class modifies or relies on the inner workings of another class
    * A change in one class might affect another
    * Tightly coupled is not usually a good practice: it's hard to reuse, test, and refactor, and breaking one class can break a whole system

### Principles of OOP
1) Encapsulation
    * The concept of bundling together the data and functions that manipulate the data (into a single class), and that keeps both hidden and safe from outside interference
        * The data cannot be accessed directly, rather other objects (and users) can only access the data through the object's public methods
    * Encapsulation makes the concept of data hiding possible
        * Attributes (a.k.a. state, data, instance variables) are kept private and methods are made public to manipulate these attributes
2) Abstraction
    * The concept of abstracting away the implementation details and inner workings of the class and only providing the users the relevant methods
        * The user does not need to know how things work underneath the hood; they just need to know what they can do
        * Only relevant data are shown to the user; the unnecessary implementation details are hidden in the class
3) Polymorphism
    * The concept of calling a (shared) method on an object and it being able to evaluate it correctly based on the type (class) of the object
        * Basically, one method can have multiple implementations (from a parent class, from others classes, etc.), and the implementation to be used is decided at runtime, called ***overriding***, (or at compiletime, called ***overloading***, which does not occur in dynamically typed languages like Ruby or Python) depending on the class of the object
    * NOTE: Inheritance is when a child class inherits all data and methods from its parent class. An example of Polymorphism here would be overriding a parent method in the child class. Thus, if you called the same method on the parent class as on the child class, they would operate differently.
    * **Duck Typing**
        * "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
            * It doesn't matter the type of the object, the program only cares if it has the correct methods
                ```
                def duck_typing(obj)
                    obj.quack
                    obj.swim
                end
                ```
                * Any object that has these methods will work in this function; it doesn't have to be what you would expect: a duck
                * Essentially, if the object can act like a duck, you assume it's a duck
        * Duck typing works in Ruby because Ruby sends messages to objects without first checking the type (class)
        * NOTE: This is not possible in Java or C++ (need to declare the type of the argument)
4) Inheritance
    * See below 

### Class Inheritance
* Used to establish a subclass (sometimes called child class) of a existing class, in order to reuse code
    * A **subclass** has access to all the methods of its parent class, a.k.a. its **superclass**
* A subclass **inherits** from its superclass
* A subclass can override any of its superclass's methods that you decide
* We can user the `super` call, with or without parameters, to run the parent class's version of the method
    * If you do pass parameters into `super`, you need to make sure (in Ruby, at least) that you are passing in the correct number of parameters used by the parent method, or it will throw an `ArgumentError` for the wrong number of arguments passed in

```
class User
  attr_reader :first_name, :last_name

  def initialize(first_name, last_name)
    @first_name, @last_name = first_name, last_name
  end

  def full_name
    "#{first_name} #{last_name}"
  end

  def upvote_article(article)
    article.upvotes += 1
  end
end

class SuperUser < User
  attr_reader :super_powers

  def initialize(first_name, last_name, super_powers)
    super(first_name, last_name)
    @super_powers = super_powers
  end

  def upvote_article(article)
    # extra votes
    article.upvotes += 3
  end

  def delete_user(user)
    return unless super_powers.include?(:user_deletion)

    # super user is authorized to delete user
    puts "Goodbye, #{user.full_name}!"
  end
end
```

```
[13] pry(main)> load 'test.rb'
=> true
[14] pry(main)> u = User.new("Jamis", "Buck")
=> #<User:0x007f9ba9897d98 @first_name="Jamis", @last_name="Buck">
[15] pry(main)> u.full_name
=> "Jamis Buck"
[16] pry(main)> su = SuperUser.new("David", "Heinemeier Hansson", [:user_deletion])
=> #<SuperUser:0x007f9ba98e66c8
 @first_name="David",
 @last_name="Heinemeier Hansson",
 @super_powers=[:user_deletion]>
[17] pry(main)> su.full_name
=> "David Heinemeier Hansson"
[18] pry(main)> su.delete_user(u)
Goodbye, Jamis Buck!
=> nil
```

### Object Decomposition
* In OOP, when you break up problems, the nouns (such as `Shark` and `Minnow`) tend to be good candidates for objects, and the verbs (such as `swim`) tend to be good candidates for methods
* Stored information, like a minnow's `position` (stored in an instance variable, `@position`, for instance) is called the ***state*** of an object
* The ***behavior*** of an object is the way an object does something (its method), like how a shark and minnow both `#swim`, but they do it differently
* In Object Oriented Design, you break complex problems down into classes, each of which is responsible for its own state and behavior
    * We want to write these classes as separately of each other as possible in order to maintain modularity and make it easier to solve
    * Each class should do one thing
        * `Shark` and `Minnow` is fine, but if you had one `Aquarium` for everything without either of the other classes, it would be trying to do too many things: model the fish AND the sharks

### Inheritance and DRY
* **D**on't **R**epeat **Y**ourself: if 2+ classes share the same method for the same behavior, have them all inherit from a separete super class
    * This: 
        ```
        class Fish
            def eat
                puts "eat eat eat"
            end
        end

        class Minnow < Fish
        end

        class Shark < Fish
        end
        ```
        * We use generic code for any type of fish
    
    * is better than:
        ```
        class Minnow
            def eat
                puts "eat eat eat"
            end
        end

        class Shark
            def eat
                puts "eat eat eat"
            end
        end
        ```

        * Not DRY

* But don't get crazy! Do not introduce subclasses until you actually need them
    * The following guidelines can help:
        1) When you are facing two different subclasses of the base class
        AND
        2) The two subclasses have substantially different behavior

### Information Hiding/Encapsulation
* When you mark methods as ***private***, the only way to access those methods is from within the class itself
    * Another method in the class can call the private method, but another class or outside user cannot use the method
    * This is an example of **encapsulation** and hiding the data from the public
* Which types of methods should be private?
    * Any that you don't want the outside user to have access to
    * Any that have low-level details that the user is not concerned with
* Instance variables are always private unless you reveal them to the public with getter/setter methods

#### Be Shy With Your Code
* Another reason to use private methods is it will make it easy to extend and update your code base in the future
    * The more you expose to users (whether people or other code), the more they will rely on those details and use those methods &rarr; thus, it can be much harder to update the code later because other people are already using it and depending on it, so a change you make can affect the performance/ability to perform of user
* The point of OOP is to present a simple, minimal interface that abstracts away the internal implementation details in the methods
    * If code is too permissive (public), you risk leaking internal details to the public, which can be extremely dangerous
        * e.g., if you allow the public to run `start_engine`, now they have to remember to run `stop_engine`
* A good OOP design principle is to minimize the public interfaces between classes or to the users
    * Expose the minimum necessary amount of state and behavior, and nothing more

### Unified Modeling Language (UML)
* A visual way to represent the relationships between different objects
    * Can describe classes, such as the structure behind an object-oriented design, or behavior, such as diagramming a set of concurrent processes
* In UML, classes can be related to each other in different ways (chess example):
    * Parent-child
        * `Pawn` is a child of `Piece`
    * Association ("has a/an" relationship)
        * `Game` is associated with `Board` because a `Game` has a (i.e. `requires`) a `Board`
* In UML, a class is usually drawn with three components:
    1) Name
    2) Set of attributes (instance variables)
    3) Set of methods
    * Attributes and methods are usually marked as being public (+), private(-), or protected (#), and class methods are underlined
* e.g.

    ![chess-uml](https://user-images.githubusercontent.com/15662012/34017487-d483616a-e0da-11e7-87b3-174b15c3bc2b.png)


### OOP Design Patterns
#### Creational Patterns
* Factory method pattern
    * Creates objects without specifying the exact class to create
    * Factory methods are class methods
* Singleton pattern
    * Restricts the instantiation of a class to one object
* Builder pattern
    * Creates complex objects by separating construction and representation

### Other Important Topics
* **Cardinality**: the relational model between two objects (or tables in a database)
    * one-to-many
    * many-to-many
    * one-to-zero-or-one
* **Multiplicity**: used in a UML to specify the cardinality
    * An inclusive interval of non-negative numbers to specify the allowable number of instances for an element
    * e.g., this table from https://en.wikipedia.org/wiki/Cardinality_(data_modeling)

        ![screen shot 2017-12-14 at 8 44 02 pm](https://user-images.githubusercontent.com/15662012/34027297-901de14a-e110-11e7-934f-b8746c493597.png)

    * This chart from https://www.uml-diagrams.org/multiplicity.html further explains the multiplicity intervals:

        ![screen shot 2017-12-14 at 8 54 18 pm](https://user-images.githubusercontent.com/15662012/34027368-00c772b2-e111-11e7-8eac-8264c5078a83.png)
        
        * The *option* column show another way it could be written

    * Example from http://slideplayer.com/slide/6193568/ showing the difference between a class diagram and an object diagram
        * Shows multiplicity on the class diagram, which is how it might be represented in UML

        ![screen shot 2017-12-14 at 9 07 05 pm](https://user-images.githubusercontent.com/15662012/34027630-d0b8d85c-e112-11e7-815f-10cf1dd1e956.png)

        * A rental item can have either no or a single customer
        * A customer can rent either 0 or many rental items
        * Object names are __underlined__
    
    * A more complete example, with other terms to define:

        ![rental_uml_class_diagram](https://user-images.githubusercontent.com/15662012/34027820-1917eccc-e114-11e7-93b5-412c5d01d911.jpg)

* Instance-level relationships:
    * **Association**
        * A semantically weak relationship between otherwise unrelated objects
            * A "using" ("has a") relationship
        * For people with Rails familiarity, it would be like having a class that represented a Rails association relation
            * For instance, if you had a `Student` class and a `Seminar` class, you could use `Enrollment` as an association class. Use cases for `Enrollment` might include keeping track of the grades,But depending on the situation, you may not want/need an `Enrollment` object. e.g., UML example from http://www.agilemodeling.com/artifacts/classDiagram.htm:

                ![screen shot 2017-12-15 at 12 18 00 pm](https://user-images.githubusercontent.com/15662012/34059023-0ac69b04-e192-11e7-9f82-07d70b3ccbad.png)

        * Can be represented as one-to-one, one-to-many, and many-to-many (also known as cardinality)
        * Represented by a single arrow in a UML:

             ![screen shot 2017-12-14 at 10 15 40 pm](https://user-images.githubusercontent.com/15662012/34029250-5c48c0b8-e11c-11e7-83fa-04b3ce9f186c.png)

    * **Dependency**
        * A semantic connection bewtween an independent element an an element that depends on that element; a uni-directional association
            * An order depends on a customer, so the order will have to refer to the Customer class and save its data; any change to the Customer class *may* result in a change to the Order class
        * Represented by a dotted line with an arrow in UML:

            ![screen shot 2017-12-14 at 10 12 10 pm](https://user-images.githubusercontent.com/15662012/34029166-e869ba76-e11b-11e7-972e-9970e4b679fb.png)

    * **Aggregation**
        * A specialized association between two or more objects in which there exists ownership, but they still have their own life cycles
            * An employee can belong to many departments, but if a department gets removed, the employee object is not destroyed
        * In UML, represented using a line with a hollow diamond

            ![screen shot 2017-12-14 at 10 16 49 pm](https://user-images.githubusercontent.com/15662012/34029279-84accebe-e11c-11e7-8500-0bae43ca94bb.png)

    * **Composition**
        * A specialized form of aggregation in which if the parent object is destroyed, the child objects would also be destroyed
            * A strong type of aggregation, also referred to as the "death" relationship
            * e.g. a house has many rooms (many rooms belong to a house) &mdash; if the house is destroyed, bye-bye to the rooms
        * In UML, represented using a line witha filled in diamond:

            ![screen shot 2017-12-14 at 10 17 32 pm](https://user-images.githubusercontent.com/15662012/34029298-9f186baa-e11c-11e7-99a6-9f05a9d6ecdf.png)
    
    * Images and visual summary (below) provided by https://dotnetfreakblog.wordpress.com/2014/01/11/concept-of-dependency-generalization-association-aggregation-composition-in-object-oriented-programming/ :
         
         ![screen shot 2017-12-14 at 10 18 24 pm](https://user-images.githubusercontent.com/15662012/34029332-d15d8bea-e11c-11e7-8ad1-fe39536ac203.png)


* Class-level relatonships:
    * **Generalization/Inheritance**
        * ***Is-a-kind-of*** relationship
        * Represented by a line with a hollow arrow in UML

            ![screen shot 2017-12-14 at 10 13 07 pm](https://user-images.githubusercontent.com/15662012/34029200-0dbacbb2-e11c-11e7-8dd1-cadac2b5c21c.png)

    * **Realization/Implementation**
        * A relationship between the interface and the implementing (parent class). In other words, the relationship between the blueprint class and the object containing its respective implementation level details). The object is said to *realize* the blueprint class. (https://javapapers.com/oops/association-aggregation-composition-abstraction-generalization-realization-dependency/)
            * e.g., a specific model of a car that *implements* the blueprint of a car realizes the abstraction
        * A dotted line with a hollow arrow:

            ![screen shot 2017-12-14 at 10 24 48 pm](https://user-images.githubusercontent.com/15662012/34029468-a9715cfa-e11d-11e7-8bc2-0cc27510ec9b.png)

* Great link for UML info: http://www.agilemodeling.com/artifacts/classDiagram.htm