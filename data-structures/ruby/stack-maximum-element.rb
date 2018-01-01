=begin
You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, N. The next N lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints
1 <= N <= 10**5
1 <= x <= 10 **9
1 <= type <= 3

Output Format

For each type 3 query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
=end

# ####################################
# Solution using array with push / pop
# ####################################
stack = []
STDIN.read.split("\n").each do |line|
  nums = line.split().map(&:to_i)
  if nums[0] == 1
    stack.push(nums[1])
  elsif nums[0] == 2
    stack.pop()
  elsif nums[0] == 3 and stack.length > 0
    puts stack.max
  end
end


# ###############################################################
# Solution using Stack / Linked List with custom push /pop
# ###############################################################
module Stack
  class Node
    attr_accessor :data, :next
    def initialize(data=nil, next_node=nil)
      @data = data
      @next = next_node
    end
    def get_data()
      @data
    end
    def get_next()
      @next
    end
    def set_next(new_next)
      @next = new_next
    end
  end

  class Stack
    def initialize
      @first = nil
    end
    def push(data)
      if is_empty?
        @first = Node.new(data, @first)
      else
        current = @first
        until current.next == nil
          current = current.next
        end
        current.next = Node.new(data)
        @first
      end
    end
    def pop
      if !is_empty?
        delete_node(-1)
      end
      nil
    end
    def get_max()
      max, current = 0, @first
      until current == nil
        if current.data > max
          max = current.data
        end
        current = current.next
      end
      max
    end
    def delete_node(position)
      current = @first
      if is_empty?
        nil
      elsif position == 0 or
          (position == -1 and @first.next == nil)
        @first = nil
        nil
      else
        while current != nil
          if current.next == position
            current.next = current.next.next
            current.next = nil
            return current
          elsif position == -1 and current.next == nil
            current = nil
            return current
          end
          current = current.next
        end
      end
    end
    def get_node(position)
      index, current = 0, @first
      until current.next == nil
        if index == position
          break
        end
        index += 1
        current = current.next
      end
      current.data
    end
    def is_empty?
      @first.nil?
    end
  end
end

stack = Stack::Stack.new
STDIN.read.split("\n").each do |line|
  nums = line.split().map(&:to_i)
  if nums[0] == 1
    stack.push(nums[1])
  elsif nums[0] == 2
    stack.pop()
  elsif nums[0] == 3 and !stack.is_empty?
    puts stack.get_max()
  end
end
