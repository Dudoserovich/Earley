import earleyparser


def walk(node, level=0):
    print(level * '-' + node['a'])
    for child in node['children']:
        walk(child, level+1)


if __name__ == '__main__':
    gr = earleyparser.Grammar('S')
    gr.add('S', ['a', 'S', 'b', 'S'])
    gr.add('S', ['!', '.'])
    gr.add('S', ['!'])

    pr = earleyparser.Parser(gr)
    pr.run('a!.b')

    completes = pr.get_completes()

    try:
        walk(pr.make_node(completes[0]))
    except IndexError:
        print('Error')