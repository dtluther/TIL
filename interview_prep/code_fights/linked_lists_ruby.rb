# Definition for singly-linked list:
class ListNode
  attr_accessor :value, :next
  def initialize(val)
    @value = val
    @next = nil
end


# PROBLEM
# Note: Try to solve this task in O(n) time using O(1) additional space, where n is
# the number of elements in the list, since this is what you'll be asked to do
# during an interview.

# Given a singly linked list of integers l and an integer k, remove all elements
# from list l that have a value equal to k.

def removeKFroList(l, k)
# # First non-elegant solution
#     return [] if l == nil
    
#     until l.value != k
#         return [] if l.next == nil
#         l = l.next
#     end
    
#     p1 = l
#     p2 = l.next
    
#     until p2 == nil
#         unless p2.value == k
#             p1.next = p2
#             p1 = p1.next
#         end  
        
#         p2 = p2.next
#     end
    
#     p1.next = nil
   
#     l

# A more elegant solution -- My preferred
    while l and l.value == k
        l = l.next
    end
    
    curr = l
    while curr && curr.next
        if curr.next.value == k
            curr.next = curr.next.next
        else
            curr = curr.next
        end
    end
    
    l

# #  A elegant recursive solution
#     if l.nil?
#         return nil
#     else
#         l.next = removeKFromList(l.next, k)
#         l.value == k ? l.next : l
#     end
end

# PROBLEM
# Note: Try to solve this task in O(n) time using O(1) additional space, where n is
# the number of elements in l, since this is what you'll be asked to do during an
# interview.

# Given a singly linked list of integers, determine whether or not it's a palindrome.
# EXAMPLE
# For l = [0, 1, 0], the output should be
# isListPalindrome(l) = true
# For l = [1, 2, 2, 3], the output should be
# isListPalindrome(l) = false

def isListPalindrome(l)
    
end
