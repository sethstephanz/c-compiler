from lexer import lexer
from parser import parser


def driver(filepath):
    # pull filepath read out to here
    r = open(filepath, 'r')
    program = r.read()
    if not program:
        return 'Driver error: Read error.'

    # lex program
    tokens = lexer(program)
    if not tokens:
        return 'Driver error: Lexer error.'
    return tokens

    # parse tokens
    # parsed = parser(tokens)
    # if not parsed:
    #     return 'Driver error: Parser error.'
    # return parsed


# these should return a lexer error
# print('invalid test 1:', driver('tests/lexer_tests/invalid_lex/at_sign.c'))
# print('invalid test 2:', driver('tests/lexer_tests/invalid_lex/backslash.c'))
# print('invalid test 3:', driver('tests/lexer_tests/invalid_lex/backtick.c'))
# print('invalid test 4:', driver(
#     'tests/lexer_tests/invalid_lex/invalid_identifier.c'))
# print('invalid test 5:', driver(
#     'tests/lexer_tests/invalid_lex/invalid_identifier_2.c'))

# # these should return list of tokens
# print('valid test 1:', driver('tests/lexer_tests/valid/multi_digit.c'))
# print('valid test 2:', driver('tests/lexer_tests/valid/no_newlines.c'))
# print('valid test 3:', driver('tests/lexer_tests/valid/return_0.c'))
# print('valid test 4:', driver('tests/lexer_tests/valid/spaces.c'))
# print('valid test 5:', driver('tests/lexer_tests/valid/tabs.c'))

# custom tests
# print('custom invalid test 6:', driver(
#     'tests/lexer_tests/invalid_lex/custom_invalid_lex_tests.c'))
# expect: invalid name

# parser tests
