# reple
Interactive REPL for executable-based software toolchains.

Ever wished you could have an interpreter for your executable-based compiled language
toolchains?  reple *simulates* an interpreter to create a REPL for you.  Each time you
enter a command, reple compiles and runs your program, printing out any new input.

The advantage to this approach is that reple only requires a simple config file to
create a REPL for a new language or executable-based runtime system.  If your language
or runtime system is not available, adding it will likely only take a few minutes!

## Installation
Just install the `reple` pip package.

```Cpp
[xiii@reple ~]$ pip3 install reple
[xiii@reple ~]$ reple -env cxx
> printf("Hello, World!\n");
Hello, World!
```

If you install the package locally, you might need to add `~/.local/bin` to your path.

## Running
To start an interactive REPL session, call `reple` with the title of a configuration
file defined in the `/configs` directory.

```Cpp
[xiii@reple xiii]$ reple -env cxx
> printf("Hello, world!\n");
Hello, world!
> int x = 12;
> int y = x + 2;
> std::cout << y << std::endl;
14
>
```

Some more complicated runtimes, like MPI, may have optional runtime flags.

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
