import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { webSocket } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private socket$;
  private todosSubject = new BehaviorSubject<any[]>([]);
  todos$ = this.todosSubject.asObservable();

  constructor() {
    this.socket$ = webSocket('ws://localhost:8000/api/ws/todos'); 

    this.socket$.subscribe({
      next: (message: any) => {
        if (message.action === 'update') {
          this.todosSubject.next(message.todos);
        }
      },
      error: (err: any) => console.error(err),
      complete: () => console.warn('WebSocket Closed')
    });
  }

  getTodos(): Observable<any[]> {
    this.socket$.next({ action: 'get' });
    return this.todosSubject.asObservable();
  }

  addTodo(todo: any) {
    this.socket$.next({ action: 'add', todo });
  }

  updateTodo(id: string, todo: any) {
    this.socket$.next({ action: 'update', id, todo });
  }

  deleteTodo(id: string) {
    this.socket$.next({ action: 'delete', id });
  }
}

