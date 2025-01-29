import { Component, OnInit } from '@angular/core';
import { TodoService } from '../../services/todo.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-todo-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css'],
})
export class TodoListComponent implements OnInit {
  todos: any[] = [];
  searchText: string = '';

  constructor(private webSocketService: TodoService) { }

  ngOnInit(): void {
    this.webSocketService.todos$.subscribe((data) => {
      this.todos = data;
    });
    this.webSocketService.getTodos().subscribe();
  }

  addTodo(todo: any) {
    this.webSocketService.addTodo(todo);
  }

  editTodo(todo: any) {
    todo.isEditing = true;
  }
  
  saveTodo(todo: any) {
    todo.isEditing = false;
    this.webSocketService.updateTodo(todo.id, todo);
  }

  deleteTodo(id: string) {
    this.webSocketService.deleteTodo(id);
  }

  filteredTodos(): any[] {
    return this.todos.filter(todo =>
      todo.title.toLowerCase().includes(this.searchText.toLowerCase())
    );
  }
}

