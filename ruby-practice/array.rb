ary = [ "fred", 10, 3.14, "this is a string",]

ary.each do |i|
  puts i
end

hsh = colors = {"red" => 0xf00, "green" => 0x0f0, "blue" => 0x00f }

  hsh.each do  |key, value|
     print key, " ", value,"\n"
  end
  
  
  (10..15).each do |n|
    print n, ' ' 
  end
  print "\n"
(10...15).each do |n|
    print n, ' ' 
  end
  
  
  
  names  = Array.new(20)
puts "\nsize #{names.size}"
puts "length #{names.length}"
puts "#{names}"

names = Array.new(4, "mac")
puts "#{names}"

nums = Array.new(10) { |e| e = e*2 }
puts "#{nums}"

nums = Array.[](0,1,2,3,4,5)
puts "#{nums}"

nums = Array[1,2,3,4,5]  
puts "#{nums}"


digits = Array(0..9)
puts "#{digits}"


num = digits.at(6)
puts "#{num}"



