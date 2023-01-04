"""Defines all the functions related to the database"""
from app import postgres


def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    cursor = postgres.cursor()
    cursor.execute("Select * from tasks;")
    data = cursor.fetchall()
    postgres.commit()
    cursor.close()
    todo_list = []
    print(data)
    for result in data:
        item = {
                "id": result[0],
                "task": result[1],
                "status": result[2]
        }
        todo_list.append(item)
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """
    cursor = postgres.cursor()
    query = "Update tasks set task = '{}' where id = {};".format(text, task_id)
    cursor.execute(query)
    postgres.commit()
    cursor.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """
    cursor = postgres.cursor()
    query = "Update tasks set status = '{}' where id = {};".format(
        text, task_id)
    cursor.execute(query)
    postgres.commit()
    cursor.close()


def insert_new_task(text: str) -> int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    cursor = postgres.cursor()
    query = "Insert Into tasks (task, status) VALUES ('{}', '{}');".format(
        text, 'Todo')
    cursor.execute(query)
    cursor.execute(" SELECT CURRVAL(pg_get_serial_sequence('tasks','id'));")
    query_results = cursor.fetchall()
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    postgres.commit()
    cursor.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    try:
        cursor = postgres.cursor()
        query = 'Delete From tasks where id={}'.format(task_id)
        cursor.execute(query)
        postgres.commit()
        cursor.close()
    except:
        print("test")






# #Creating a connection cursor
# cursor = postgres.cursor()

# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')

# #Saving the Actions performed on the DB
# postgres.commit()

# #Closing the cursor
# cursor.close()
