import check50

main_str = """


int main()
{
    ft_putchar('A');
}
"""

@check50.check()
def ft_putchar_compiles():
    """ft_putchar compiles"""
    check50.include("test_00.c", "ex00.h")
    check50.run(f"echo {main_str} >> test_00.c")
    check50.run("gcc -Wall -Werror -Wextra test_00.c ft_putchar.c ").stdout("")
