require 'module1'

y = M1.inc(M1::PI)

puts "#{y}"

class Decade
  include M1
  
  no_of_yrs = 10
  def test
    puts M1::PI
  end
end


d1 = Decade.new
puts M1::PI
d1.test
puts d1.func(2)