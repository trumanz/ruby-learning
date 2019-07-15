def test
  puts "You are in the method"
  yield
  puts "You are again back to the method"
  yield
end

test { puts "you are in the block"}
  
  
  
def block_with_parameter
  yield 5
  puts "you are in the block_with_parameter test"
  yield 100
end


block_with_parameter{ |i| puts "you are in the block #{i}"}
  
  

def block_with_parameters
  yield 5, 100
  puts "you are in the block_with_parameters test"
  yield 100
end

block_with_parameters{ |i, j| puts "you are in the block #{i}, #{j}"}
  
  
  
def test(&block)
  block.call
end

test {puts "this is sdafasf"}


BEGIN{
  puts "BEGIN code block"
}

END {
  puts  "END code block"
}


puts "MAIN code block"
