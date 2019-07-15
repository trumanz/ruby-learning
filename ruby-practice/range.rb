
digits = 0..9

puts digits.include?(5)

puts "Min value  is  #{digits.min}"
puts "Max value  is  #{digits.max}"


ret = digits.reject{|i| i < 5}
puts "Rejected values are #{ret}"

digits.each do  |digit|
  puts "In Loop #{digit}"
end

score = 70
result = case score
when 0..40 then "Fail"
when 41..100 then "Pass"
else "Invalid score"
end
puts result


if ((1..10) === 5)
  puts "5 lies in (1..10)"
end