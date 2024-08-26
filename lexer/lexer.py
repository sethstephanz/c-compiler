# keywords = ['int', 'void', 'return']
symbols = ['{', '}', '[', ']', '(', ')', ';']

# breakpoints: white space, symbols, changes from str to int or vice versa
# special case: \n, which we should ignore


def lexer(filepath):
    r = open(filepath, 'r')
    program = r.read()
    if not program:
        return 'Lexer error: Read error.'
    tokens = []
    i = 0
    program = program.strip()
    while program:
        # break on white space, symbols, and changes from str to int or vice versa
        # there's no reason that a constant and a token should be cached at same time while tokenizing

        # string version of constant (to be converted to int)
        constant = ''
        # token (to be kept as string)
        token = ''
        while i < len(program):
            # print('char ' + str(i) + ':', program[i])
            # ignore comments
            if program[i] == '/' and program[i+1] and program[i+1] == '/' or program[i] == '#':
                while program[i] != '\n':
                    i += 1
            # ignore all newlines and tabs for now.
            # will have to come back to address '\n' and '\t' in string literals at some point
            if program[i] == '\n' or program[i] == '\t':
                if constant:
                    tokens.append(int(constant))
                    constant = ''
                elif token:
                    tokens.append(token)
                    token = ''
                i += 1
                continue
            # break on space. append cached constant/token
            if program[i] == ' ':
                if constant:
                    tokens.append(int(constant))
                    constant = ''
                elif token:
                    tokens.append(token)
                    token = ''
                i += 1
                continue
            # invalid char. throw error
            if not program[i].isalnum() and program[i] != '_' and program[i] not in symbols:
                return 'Lexer error: Char invalid.'

            if program[i].isalpha() or program[i] == '_':
                if constant:
                    # constant is cached. 123main is invalid. throw error
                    return 'Lexer error: Invalid name.'
                token += program[i]
            elif program[i].isnumeric():
                constant += program[i]
            elif program[i] in symbols:
                # 123() not allowed. throw error
                # actually, do we want to throw error or just push number to tokens?
                if constant:
                    # append cached constant
                    tokens.append(int(constant))
                    constant = ''
                # push token and symbol separately. clear token
                elif token:
                    tokens.append(token)
                    token = ''
                tokens.append(program[i])
            # we want to break on white space, although this is not
            # the only place to break!
            elif program[i] == ' ':
                if token:
                    tokens.append(token)
                    token = ''
                elif constant:
                    tokens.append(int(constant))
                    constant = ''

            # at end of input
            if i >= len(program)-1:
                if token:
                    tokens.append(token)
                elif constant:
                    tokens.append(int(constant))
                return tokens
            i += 1


# these should return a lexer error
# print('invalid test 1:', lexer('lexer_tests/invalid_lex/at_sign.c'))
# print('invalid test 2:', lexer('lexer_tests/invalid_lex/backslash.c'))
# print('invalid test 3:', lexer('lexer_tests/invalid_lex/backtick.c'))
# print('invalid test 4:', lexer('lexer_tests/invalid_lex/invalid_identifier.c'))
# print('invalid test 5:', lexer('lexer_tests/invalid_lex/invalid_identifier_2.c'))

# # these should return list of tokens
# print('valid test 1:', lexer('lexer_tests/valid/multi_digit.c'))
# print('valid test 2:', lexer('lexer_tests/valid/no_newlines.c'))
# print('valid test 3:', lexer('lexer_tests/valid/return_0.c'))
# print('valid test 4:', lexer('lexer_tests/valid/spaces.c'))
# print('valid test 5:', lexer('lexer_tests/valid/tabs.c'))

# custom tests
print('custom invalid test 6:', lexer(
    'lexer_tests/invalid_lex/custom_invalid_lex_tests.c'))
