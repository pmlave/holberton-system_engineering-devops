#!/usr/bin/env ruby

regexp = /Holberton/
result = ARGV[0].scan(regexp)
for i in 0..result.length
    printf("%s", result[i])
end
printf("\n")
