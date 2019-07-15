foo = 42
print  defined? foo, "\n"
print defined? $_, "\n"
print defined? bar, "\n"

print defined? puts, "\n"
print defined? puts(bar), "\n"

defined? super   

defined? yield  




MR_COUNT = 0
module Foo
  MR_COUNT = 0
  ::MR_COUNT = 1
  MR_COUNT  = 2
end

puts MR_COUNT
puts Foo::MR_COUNT

puts "=============="

CONST = ' out there'
class Inside_one
  CONST = proc {' in there'}
    def where_is_my_CONST
      ::CONST + ' inside one'
    end
end
class Inside_two
  CONST = ' inside two'
  def where_is_my_CONST
    CONST
  end
end

puts Inside_one.new.where_is_my_CONST()
puts Inside_two.new.where_is_my_CONST

puts Object::CONST + Inside_two::CONST

puts Inside_two::CONST + CONST

puts Inside_one::CONST.call  + Inside_two::CONST
