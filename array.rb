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