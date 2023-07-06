python one liners
-----------------

# get the ascii code
python -c "print ord(';')"

# ascii code in hex
python -c "print hex(ord(';'))"


# run HTTP server in a directory :
cd /home/dir
python -m SimpleHTTPServer 8080


# Share folder using HTTP
twistd web –path /home/code/shared –port 8081 &

# Share folder using FTP
twistd -n ftp -r /home/code/shared &

# to hex
python -c "print hex(17)"
python -c "print int(0x11)"


# See all parameters of a function
def f(a,b,c):
    d = 7
    print a,b,c,d


print f.func_code.co_argcount
print f.func_code.co_varnames


# Show current objects
dir()

# parsing a string to extract values
string_date="01-08-1934"
day, month, year = map(int, string_date.split('-'))
date1 = Date(dat, month, year)

#inline ternary
f = lambda(n): re.split(r"(?<=\]):" if n.startswith('[') else r"(?<=\d):", n)




