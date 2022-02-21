import re

s = 'geeks.forgeeks'

match = re.search(r'\.', s)
print(match.start(), ",",  match.end())

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

# Using re.findall
regex = '\d+'
match = re.findall(regex, string)
print(match)
#[#'123456789', '987654321']

# Using re.findall
string1 = "Aye, said Mr. Gibenson Stark"
match = re.findall('[a-e]', string1)
print(match)
#['e', 'a', 'd', 'b', 'e', 'a']

# Using re.compile
r = re.compile('[a-e]')
print(r.findall(string1))
#['e', 'a', 'd', 'b', 'e', 'a']

r = re.compile("ab*")
print(r.findall("ababbaabbb"))
#['ab', 'abb', 'a', 'abbb']

#Using split
print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
#['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']

print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
#['On ', 'th Jan ', ', at ', ':', ' AM'] 

'''
O/P
5 , 6
'''


