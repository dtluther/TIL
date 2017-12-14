# Notes on Object Orient Programming

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
                * Any object that has these methods will work in this function; it doesn't have to be what we would expect: a duck
                * Essentially, if the object can act like a duck, we assume it's a duck
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
* When we mark methods as ***private***, the only way to access those methods is from within the class itself
    * Another method in the class can call the private method, but another class or outside user cannot use the method
    * This is an example of **encapsulation** and hiding the data from the public
* Which types of methods should be private?
    * Any that we don't want the outside user to have access to
    * Any that have low-level details that the user is not concerned with
* Instance variables are always private unless we reveal them to the public with getter/setter methods

#### Be Shy With Your Code
* Another reason to use private methods is it will make it easy to extend and update your code base in the future
    * The more you expose to users (whether people or other code), the more they will rely on those details and use those methods &rarr; thus, it can be much harder to update the code later because other people are already using it and depending on it, so a change you make can affect the performance/ability to perform of user
* The point of OOP is to present a simple, minimal interface that abstracts away the internal implementation details in the methods
    * If code is too permissive (public), you risk leaking internal details to the public, which can be extremely dangerous
        * e.g., if we allow the public to run `start_engine`, now they have to remember to run `stop_engine`
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