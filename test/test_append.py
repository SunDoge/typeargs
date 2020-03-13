from typed_args import TypedArgs, add_argument
from dataclasses import dataclass
from typing import List, Tuple


def test_append():
    @dataclass
    class Args(TypedArgs):
        foo: List[str] = add_argument('--foo', action='append')

    args = Args.from_args('--foo 1 --foo 2'.split())

    assert args.foo == ['1', '2']


def test_same_dest():
    # @dataclass
    # class Args(TypedArgs):
    #     types: Tuple[str, int] = (
    #         add_argument('--str', action='append_const', const=str),
    #         add_argument('--int', action='append_const', const=int)
    #     )

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='types', action='append_const', const=str)
    parser.add_argument('--int', dest='types', action='append_const', const=int)

    # args = Args.from_args('--str --int'.split())
    # args = parser.parse_args('--str --int'.split())
    args = parser.parse_args('--int --str'.split())

    assert args.types == [str, int]
