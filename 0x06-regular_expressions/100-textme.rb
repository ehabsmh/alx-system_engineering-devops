#!/usr/bin/env ruby

from = ARGV[0].scan(/from:(.\+*\w+)\]/)
to =  ARGV[0].scan(/\[to:(.\+*\w+)\]/)
flags = ARGV[0].scan(/\[flags:(-?[10]:-?[10]:-?[10]:-?[10]:-?[10])\]/)
puts [from, to, flags].join(',')
