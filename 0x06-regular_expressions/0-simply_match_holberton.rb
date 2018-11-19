#!/usr/bin/env ruby

regexp = /Holberton/
result = ARGV[0].scan(regexp)
array_len = result.length
for i in 0..array_len
    printf("%s", result[i])
end
printf("\n")
