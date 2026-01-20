import React from "react";
import { updateTodo, deleteTodo } from "../api";

const TodoItem = ({ todo, fetchTodos }) => {
  const toggleCompleted = async () => {
    await updateTodo(todo.id, !todo.completed);
    fetchTodos();
  };

  const handleDelete = async () => {
    await deleteTodo(todo.id);
    fetchTodos();
  };

  return (
    <li>
      <input type="checkbox" checked={todo.completed} onChange={toggleCompleted} />
      <span style={{ textDecoration: todo.completed ? "line-through" : "none" }}>
        {todo.title}
      </span>
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
};

export default TodoItem;
