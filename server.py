from livereload import Server, shell

server = Server()
server.watch('src/css/*', shell('npm run build'))
server.watch('docs/*', shell('make docs'))
server.watch('sphinx_typlog_theme/*', shell('make docs'))
server.watch('sphinx_typlog_theme/static/*', shell('make docs'))
server.serve(root='docs/_build/html', port=5234)
