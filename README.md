# reple
"Replay-based" REPLs for compiled languages.

reple provides an "interpreter" (REPL) for compiled languages.  Each time you enter a
line of code, reple will add the new code to your program, compile and run the new
iteration of your program, and then print any new output.  reple currently supports
C, C++, Go, Rust, UPC, MPI, DASH, and BCL.



## Installation
Just install the `reple` pip package.

```Cpp
[xiii@reple ~]$ pip3 install reple
[xiii@reple ~]$ reple -env cxx
> printf("Hello, World!\n");
Hello, World!
```

If you install the package locally, you might need to add `~/.local/bin` to your path.

## Usage
To start an interactive REPL session, call `reple` with the title of a configuration
file defined in the `/configs` directory.

```Cpp
[xiii@reple xiii]$ reple -env cxx
> printf("Hello, World!\n");
Hello, World!
> int x = 12;
> int y = x + 2;
> std::cout << y << std::endl;
14
```

### Functions and Global Variables
To define a new function or global variable, surround your expression
with `$`.

```Cpp
> $void foo() {
  printf("Hello, World!\n");
}$
> foo();
Hello, World!
```

### Errors
reple automatically detects compilation errors, printing them out for you without trashing
your REPL state.

```Cpp              
> int x = ;                                                                                         
/tmp/repl/repl0.cpp:8:9: error: expected expression
int x = ;
        ^
1 error generated.
>                                                                                                   
```

### Multi-Line Statements
It also automatically detects most multi-line expressions, like if statements.

```Cpp
> int x = 12;
> if (x == 12) {
>   printf("Hello, World!\n");
> }
Hello, World!
```

### Runtime Options
Some more complicated runtimes have optional runtime flags.  An
example of this is the number of processes to run a program with
in MPI.

```Cpp
[xiii@reple home]$ reple -env mpicxx --rargs "-n 8"
> int rank, nprocs;
> MPI_Comm_rank(MPI_COMM_WORLD, &rank);
> MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
> printf("Hello, world! I'm %d/%d\n", rank, nprocs);
Hello, world! I'm 0/8
Hello, world! I'm 1/8
Hello, world! I'm 2/8
Hello, world! I'm 4/8
Hello, world! I'm 6/8
Hello, world! I'm 3/8
Hello, world! I'm 5/8
Hello, world! I'm 7/8
> 
```

## Adding New Languages
Adding a new language to reple is easy.  All you need to do is write a short JSON file
that describes (1) how to append REPL lines to form a program, (2) how to compile and
run a program, and (3) terminal options, which are things like characters that enclose
expressions that can span multiple lines (like `{}` in C).  These config files are
typically only about 20 lines, and you can find examples in `/reple/configs`.

## Issues and Contributions
We've tested reple on MacOS, FreeBSD, and a few Linux distros.  If you run
into any issues installing or using reple, please make an issue using our GitHub
repo.

We welcome contributions in the form of pull requests, particularly if you'd like
to add support for a new language or runtime system.
