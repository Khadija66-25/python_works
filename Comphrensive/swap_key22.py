num_dict = {"one":1,"two":2,"three":3,"four":4,"five":5}

#swap the key and value

new_dict = {v:k for k,v in num_dict.items()}

print(new_dict)