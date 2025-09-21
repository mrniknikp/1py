# Добро пожаловать!

> Мы тут просто пытаемся учиться...

> По вопросам <a href="https://t.me/slyalike">пишите сюда</a>

> <a href="@mrniknikp">GitHub профиль</a>

===

===

<!-- Остальная информация:
Никита, --->

```javascript
function calculateAge(birthDate) {
  const today = new Date();
  const birth = new Date(birthDate);
  let age = today.getFullYear() - birth.getFullYear();
  const monthDiff = today.getMonth() - birth.getMonth();
  
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
    age--;
  }
  
  return age;
}

// Пример использования
document.write(calculateAge('2005-10-03'));
```