import check50

@check50.check()
def ft_putchar_compiles():
    """ft_putchar compiles"""
    check50.include("test_00.c", "ex00.h")
    check50.run("gcc -Wall -Werror -Wextra test_00.c ft_putchar.c ").exit(0)
