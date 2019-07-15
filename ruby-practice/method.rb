def method_name(var1, var2)
  puts "#{var1}"
  puts "#{var2}"
end

method_name "c",  "C++"
  

def test 
  i = 100
  j = 200
  k = 300
  return i, j, k
end

var  = test
puts var

def variable_number_of_paramaters(*test)
  puts "The number of parameter is #{test.length}"
  for i in 0...test.length
    puts "Parmaters: #{test[i]}"
  end
end

variable_number_of_paramaters  "Zara", "6", "F"
  

class Accounts
  def reading_charge
    return "reading_charge"
  end
  def Accounts.return_data
    return "Accounts.return_data"
  end
end


puts Accounts.return_data

