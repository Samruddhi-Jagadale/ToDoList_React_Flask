import React, { useEffect, useState } from "react";
import { getTodos } from "../api";
import TodoItem from "./TodoItem";
import AddTodo from "./AddTodo";

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  const fetchTodos = async () => {
    const response = await getTodos();
    setTodos(response.data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div>
      <h1>My To-Do List</h1>
      <AddTodo fetchTodos={fetchTodos} />
      <ul>
        {todos.map((todo) => (
          <TodoItem key={todo.id} todo={todo} fetchTodos={fetchTodos} />
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
