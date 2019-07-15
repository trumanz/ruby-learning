$global_variable = 10

class Customer
  @@no_of_customers = 0
  def initialize(id, name, addr)
    @cust_id = id
    @cust_name = name
    @cust_addr = addr
  end
  def hello
    puts "hello ruby"
  end
  def print_global
    puts "Global variable  global_variable=#$global_variable"
  end
  def display_details()
    puts "cust_id=#@cust_id"
    puts "cust_name=#@cust_name"
    puts "cust_addr=#@cust_addr"
  end
  def total_no_of_customers()
    @@no_of_customers += 1
    puts "no_of_customers=#@@no_of_customers"
  end
  
  VAR1 = 100
  def show
    puts "Value of VAR1 = #{VAR1}"
  end
end

cust1 = Customer.new("1", "John", "Widom #1")
cust2 = Customer.new("2", "Poul", "New Empire #2")

cust1.hello()
cust1.print_global()
cust2.print_global()
cust2.display_details()
cust1.total_no_of_customers()
cust2.total_no_of_customers()
cust1.show()