from time import sleep
from selene import have, command
from selene.support.shared.jquery_style import s, ss
from todomvc_testings.Model import todos


def test_e2e():
    todos.given_opened('11', '22', '33', '44')
    todos.should_be('11', '22', '33', '44')
    todos.toggle('22')
    todos.toggle('33')
    todos.toggle('22')
    s('[href="#/active"]').click()
    todos.should_be_active('11', '22', '44')
    s('[href="#/completed"]').click()
    todos.should_be_completed('33')
    todos.delete('33')
    todos.should_be_empty(0)
    s('[href="#/"]').click()
    todos.start_editing('22', '1234')
    todos.toggle_all()
    todos.toggle('11')
    todos.clear_completed()
    todos.should_be_empty(1)
    sleep(2)
