import check50

@check50.check()
def ft_putchar_compiles():
    """ft_putchar compiles"""
    check50.include("test_00.c", "ex00.h")
    check50.run("gcc -Wall -Werror -Wextra ft_putchar.c test_00.c")
