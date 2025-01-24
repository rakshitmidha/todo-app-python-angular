import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private apiUrl = 'http://localhost:8000/api/todos';

  constructor(private http: HttpClient) {}

  getTodos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  createTodo(todo: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, todo);
  }

  updateTodo(id: string, todo: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, todo);
  }

  deleteTodo(id: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
