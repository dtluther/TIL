# Inheritance

class Animal
    attr_accessor :name

    def initialize(name = "Nameless")
        @name = name
    end

    def make_n_noises(n = 2)
        n.times { print "Roar "}
    end
end

class Liger < Animal
    def make_n_noises(n = 4)
        n.times { print "Growl "}
        super
        # When we call super, it automatically passes in the parameters from this method
        # to the method of the parent class, or sueprclass
        # This means if the super method takes a different number of parameters (at least
        # in Ruby), it will throw an ArgumentError for the wrong number of arguments
    end
end