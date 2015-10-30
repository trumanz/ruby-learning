module M1
  PI = 3.1415926
  def M1.inc(x)
    return x + 1
  end
  def func(x)
    return x-1
  end
end

module M2
  BAD = 0
  def M2.func(par)
    return par
  end
end

