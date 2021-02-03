'''
translation-unit:
    external-declaration
    translation-unit external-declaration

external-declarations:
    function-definition
    declaration

function-definition:
    type-specifier declarator compound-statement
'''
# Here the declaration-list(opt) was for the old K&R C which we do not want to support.
# So we are going to simplify the function definition production.
# And we always require one type-specifier
# this new production is still compatible with compiler support C89,
# so a code of this smaller C grammar will be correct to C89 compilers.

'''
declaration:
    type-specifier declarator-list ;

'''

# we assume one source file for now to keep it simple
# so there is no need for static and extern

'''
type-specifier:
    void
    char
    int
    float
    struct-or-union-specifier
    enum-specifier
'''
# we keep only the very basic types here
# and we assume they are all signed
# here char is valid as in range [0, 127]

# we do not support type qualifier for now

'''
struct-or-union-specifier:
    struct-or-union identifier { declaration-list }
    struct-or-union identifier
'''
# identifier is required instead of optional when you have a struct body

'''
struct-or-union:
    struct
    union
'''
# do not support bit fields for now declarator(opt) : constant-expression

'''
enum-specifier:
    enum identifier { enumerator-list }
    enum identifier

enumerator-list:
    enumerator
    enumerator-list , enumerator

enumerator:
    identifier
    identifier = constant-expression

declarator:
    pointer(opt) direct-declarator

direct-declarator:
    identifier
    ( declarator )
    direct-declarator [ constant-expression(opt) ]
    direct-declarator ( parameter-type-list )
    direct-declarator ( identifier-list(opt) )

pointer:
    * type-qualifier-list(opt)
    * type-qualifier-list(opt) pointer

type-qualifier-list:
    type-qualifier
    type-qualifier-list type-qualifier

parameter-type-list:
    parameter-list
    parameter-list , ...

parameter-list:
    parameter-declaration
    parameter-list , parameter-declaration

parameter-declaration:
    declaration-specifiers declarator
    declaration-specifiers abstract-declarator(opt)

identifier-list:
    identifier
    identifier-list , identifier
'''
# do not support initializer for now
# rely on assignment-statement

'''
type-name:
    type-specifier abstract-declarator(opt)

abstract-declarator:
    pointer
    pointer(opt) direct-abstract-declarator

direct-abstract-declarator:
    ( abstract-declarator )
    direct-abstract-declarator(opt) [ constant-expression(opt) ]
    direct-abstract-declarator(opt) ( parameter-type-list(opt) )

typedef-name:
    identifier

statement:
    labeled-statement
    expression-statement
    compound-statement
    selection-statement
    iteration-statement
    jump-statement

labeled-statement:
    identifier : statement
    case constant-expression : statement
    default : statement

expression-statement:
    expression(opt) ;

compound-statement:
    { declaration-list(opt) statement-list(opt) }

declaration-list:
    declaration
    declaration-list declaration

statement-list:
    statement
    statement-list statement

selection-statement:
    if ( expression ) statement
    if ( expression ) statement else statement
    switch ( expression ) statement

iteration-statement:
    while (expression) statement
    do statement while ( expression ) ;
    for ( expression(opt) ; expression(opt) ; expression(opt) ) statement

jump-statement:
    goto identifier ;
    continue ;
    break ;
    return expression(opt) ;

expression:
    assignment-expression
    expression , assignment-expression

assignment-expression:
    conditional-expression
    unary-expression assignment-operator assignment-expression

assignment-operator:
    =
    *=
    /=
    %=
    +=
    -=
    <<=
    >>=
    &=
    ^=
    |=

conditional-expression:
    logical-OR-expression
    logical-OR-expression ? expression : conditional-expression

constant-expression:
    conditional-expression

logical-OR-expression:
    logical-AND-expression
    logical-OR-expression || logical-AND-expression

logical-AND-expression:
    inclusive-OR-expression
    logical-AND-expression && inclusive-OR-expression

inclusive-OR-expression:
    exclusive-OR-expression
    inclusive-OR-expression | exclusive-OR-expression

exclusive-OR-expression:
    AND-expression
    exclusive-OR-expression ^ AND-expression

AND-expression:
    equality-expression
    AND-expression & equality-expression

equality-expression:
    relational-expression
    equality-expression == relational-expression
    equality-expression != relational-expression

relational-expression:
    shift-expression
    relational-expression < shift-expression
    relational-expression > shift-expression
    relational-expression <= shift-expression
    relational-expression >= shift-expression

shift-expression:
    additive-expression
    shift-expression << additive-expression
    shift-expression >> additive-expression

additive-expression:
    multiplicative-expression
    additive-expression + multiplicative-expression
    additive-expression - multiplicative-expression

multiplicative-expression:
    cast-expression
    multiplicative-expression * cast-expression
    multiplicative-expression / cast-expression
    multiplicative-expression % cast-expression

cast-expression:
    unary-expression
    ( type-name ) cast-expression

unary-expression:
    postfix-expression
    & cast-expression
    * cast-expression
    ~ cast-expression
    ! cast-expression
    + cast-expression
    - cast-expression
    ++ unary-expression
    -- unary-expression
    sizeof unary-expression
    sizeof ( type-name )

postfix-expression:
    primary-expression
    postfix-expression [ expression ]
    postfix-expression ( argument-expression-list(opt) )
    postfix-expression . identifier
    postfix-expression -> identifier
    postfix-expression ++
    postfix-expression --

primary-expression:
    (expression)
    identifier
    string
    integer-constant
    character-constant
    floating-constant
    enumeration-constant

argument-expression-list:
    assignment-expression
    argument-expression-list , assignment-expression
'''
