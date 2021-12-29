from argparse import ArgumentParser

from database import DatabaseHandler

class TodoApp:
    def __init__(self, parser, db_handler):
        self.parser = parser
        self.db_handler = db_handler

        self.parser.add_argument('-a', '--add', metavar='TODO', type=str, nargs='+', help='Add todo task')
        self.parser.add_argument('-l', '--list', action='store_true', help='List all todos')
        self.parser.add_argument('-c', '--completed', metavar='id', type=int, nargs='+', help='Move todos to completed')
        self.parser.add_argument('-r', '--remove', metavar='id', type=int, nargs='+', help='Remove todo from the database')

    def run(self):
        self.args = self.parser.parse_args()
        if self.args.list == True:
            self._list()
        if self.args.add is not None:
            self._add(*self.args.add)
        if self.args.completed is not None:
            self._completed(*self.args.completed)
        if self.args.remove is not None:
            self._remove(*self.args.remove)

    def _list(self):
        print('TODOs: ')
        print('-'*10)
        print('id | desc')
        print('-'*10)
        for todo in self.db_handler.get_all():
            if not todo[2]:
                print(f'{todo[0]} | {todo[1]}')
        print()
        print('Completed: ')
        print('-'*10)
        print('id | desc')
        print('-'*10)
        for todo in self.db_handler.get_all():
            if todo[2]:
                print(f'{todo[0]} | {todo[1]}')

    def _add(self, *todos):
        print('Adding tasks to todo list...')
        for todo in todos:
            self.db_handler.insert(todo)
        print('Added!')

    def _completed(self, *ids):
        print('Moving tasks to completed list...')
        for id in ids:
            self.db_handler.update(id, completed=True)
        print('Moved!')

    def _remove(self, *ids):
        print('Removing tasks from list...')
        for id in ids:
            self.db_handler.delete(id)
        print('Removed!')

if __name__ == '__main__':
    parser = ArgumentParser(description='Manage your todo tasks')
    db_handler = DatabaseHandler()
    
    app = TodoApp(parser, db_handler)
    app.run()
