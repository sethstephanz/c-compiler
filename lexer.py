keywords = ['int', 'void', 'return']
symbols = ['{', '}', '[', ']', '(', ')', ';']

# breakpoints: white space, symbols, changes from str to int or vice versa
# special case: \n and \t, which we should treat as spaces unless they're in string literals (tbd)

tokenTypes = {
    'keyword': 'KEYWORD',
    'symbol': 'SYMBOL',
    'identifier': 'IDENTIFIER',  # non-keyword string
    'integer': 'INTEGER',
    'float': 'FLOAT',
    'operator': 'OPERATOR'
}


def lexer(program):
    if not program:
        return
    tokens = []  # return an array of Token objects
    i = 0
    program = program.strip()
    while program:
        # constant and token should not be cached at same time
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
                newToken = createNewToken(constant, token)
                if newToken:
                    tokens.append(newToken)
                token = constant = ''
                i += 1
                continue
            # break on space. append cached constant/token
            if program[i] == ' ':
                newToken = createNewToken(constant, token)
                if newToken:
                    tokens.append(newToken)
                token = constant = ''
                i += 1
                continue
            # invalid char. throw error
            if not program[i].isalnum() and program[i] != '_' and program[i] not in symbols:
                print('Lexer error: Invalid char.')
                return
            if program[i].isalpha() or program[i] == '_':
                if constant:
                    # constant is cached. 123main is invalid. throw error
                    print('Lexer error: Invalid name.')
                    return
                token += program[i]
            elif program[i].isnumeric():
                constant += program[i]
            elif program[i] in symbols:
                newToken = createNewToken(constant, token)
                if newToken:
                    tokens.append(newToken)
                token = constant = ''
                tokens.append([tokenTypes['symbol'], program[i]])
            # we want to break on white space, although this is not
            # the only place to break!
            elif program[i] == ' ':
                newToken = createNewToken(constant, token)
                if newToken:
                    tokens.append(newToken)
                token = constant = ''

            # at end of input
            if i >= len(program)-1:
                newToken = createNewToken(constant, token)
                if newToken:
                    tokens.append(newToken)
                token = constant = ''
                return tokens
            i += 1


def createNewToken(constant, token):
    newToken = None
    if constant:
        newToken = [tokenTypes['integer'], int(constant)]
    elif token:
        if token in keywords:
            newToken = [tokenTypes['keyword'], token]
        else:
            newToken = [tokenTypes['identifier'], token]
    return newToken
