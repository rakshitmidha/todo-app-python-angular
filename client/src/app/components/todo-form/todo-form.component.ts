import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { TodoService } from '../../services/todo.service';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-todo-form',
    standalone: true,
    templateUrl: './todo-form.component.html',
    styleUrls: ['./todo-form-component.css'],
    imports: [CommonModule, FormsModule],
})
export class TodoFormComponent {
    todoText: string = '';
    todoDescription: string = '';

    constructor(private todoService: TodoService) { }

    addTodo(): void {
        if (this.todoText.trim()) {
            const newTodo = {
                title: this.todoText,
                description: this.todoDescription,
                completed: false,
            };

            this.todoService.addTodo(newTodo);
            console.log('Todo added successfully:', newTodo);
            
            this.todoText = '';
            this.todoDescription = '';
        }
    }
}
