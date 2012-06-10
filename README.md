About
-----

An implementation of a lexer for the UWSC language, to be used in the Pygments highlighting system. See

* [http://www.uwsc.info/](http://www.uwsc.info/)
* [pygments.org](http://pygments.org)

Installation
------------

Assuming you already have Pygments installed (otherwise a simple `sudo easy_install Pygments` should suffice, or look at the other options at [pygments.org/docs/installation](http://pygments.org/docs/installation/)), in order to install the UWSCLexer package you only need to

1. `git clone git://github.com/pbelmans/uwsc-pygments-lexer.git`.
2. `cd uwsc-pygments-lexer`
3. `sudo python setup.py install`
4. `pygmentize -L lexer | grep -i uwsc`

Hacking
-------

    pygmentize -O full,style=default -f html -o <output file> <input file>

    input file encoding must be UTF-8,  
    To convert, 
    `nkf -w file > out_file`

Thanks
------

The code is based on several of the already existing gap lexers from Pygments, 
See [https://github.com/pbelmans/gap-pygments-lexer](https://github.com/pbelmans/gap-pygments-lexer)
