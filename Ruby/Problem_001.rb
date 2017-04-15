array = (1..999).to_a.select{|x| x%3==0 || x%5==0}.inject(0, :+)

print array