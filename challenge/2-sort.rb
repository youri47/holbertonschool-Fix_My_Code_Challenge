#!/usr/bin/env ruby

numbers = []
ARGV.each do |arg|
  begin
    numbers << Integer(arg)
  rescue ArgumentError
    # ignore les arguments non numériques
  end
end

numbers.sort.each { |n| puts n }
