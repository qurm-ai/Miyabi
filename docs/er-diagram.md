# Деректер моделі (6-сабақ)

## Кестелер (AI-сыз, өзіңіз)
- users: id, email, full_name, role, created_at
- quizzes: id, title, topic, status, teacher_id, created_at
- questions: id, text, quiz_id, created_at
- options: id, text, is_correct, question_id
- quiz_attempts: id, student_id, quiz_id, score, completed_at
- student_answers: id, attempt_id, question_id, selected_option_id

## Байланыстар
- users 1 — көп quizzes: бір мұғалім көп тест құра алады
- quizzes 1 — көп questions: бір тестте көп сұрақ болады
- questions 1 — көп options: бір сұрақта көп жауап нұсқасы болады
- users 1 — көп quiz_attempts: бір студент көп рет тест тапсыра алады
- quizzes 1 — көп quiz_attempts: бір тестті көп студент тапсыра алады
- quiz_attempts 1 — көп student_answers: бір тест тапсыру әрекетінде көп жауап болады

## ER диаграммасы
```mermaid
erDiagram
    USERS ||--o{ QUIZZES : "creates"
    USERS ||--o{ QUIZ_ATTEMPTS : "takes"
    QUIZZES ||--o{ QUESTIONS : "contains"
    QUIZZES ||--o{ QUIZ_ATTEMPTS : "attempted_in"
    QUESTIONS ||--o{ OPTIONS : "has"
    QUIZ_ATTEMPTS ||--o{ STUDENT_ANSWERS : "includes"
    QUESTIONS ||--o{ STUDENT_ANSWERS : "answered_in"
    OPTIONS ||--o{ STUDENT_ANSWERS : "selected_in"

    USERS {
        int id PK
        string email
        string full_name
        string role
        datetime created_at
    }

    QUIZZES {
        int id PK
        string title
        string topic
        string status
        int teacher_id FK
        datetime created_at
    }

    QUESTIONS {
        int id PK
        string text
        int quiz_id FK
        datetime created_at
    }

    OPTIONS {
        int id PK
        string text
        boolean is_correct
        int question_id FK
    }

    QUIZ_ATTEMPTS {
        int id PK
        int student_id FK
        int quiz_id FK
        int score
        datetime completed_at
    }

    STUDENT_ANSWERS {
        int id PK
        int attempt_id FK
        int question_id FK
        int selected_option_id FK
    }
```
