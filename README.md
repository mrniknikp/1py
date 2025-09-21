# Добро пожаловать!

> Мы тут просто пытаемся учиться...

> По вопросам <a href="https://t.me/slyalike">пишите сюда</a>

> <a href="@mrniknikp">GitHub профиль</a>

===

===

<!-- Остальная информация:
Никита, --->

<script>
const birthDate = new Date('2005-10-03');
const today = new Date();
let age = today.getFullYear() - birthDate.getFullYear();
const monthDiff = today.getMonth() - birthDate.getMonth();
if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
age--;
}
document.write(age);
</script>
