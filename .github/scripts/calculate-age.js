const fs = require('fs');
const path = require('path');

const birthDate = new Date('2005-10-03');
const today = new Date();

let age = today.getFullYear() - birthDate.getFullYear();
const monthDiff = today.getMonth() - birthDate.getMonth();

if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
    age--;
}

const readmePath = path.join(process.cwd(), 'README.md');
let readmeContent = fs.readFileSync(readmePath, 'utf8');

readmeContent = readmeContent.replace(/Никита, \*script\* лет/g, `Никита, ${age} лет`);

fs.writeFileSync(readmePath, readmeContent, 'utf8');

console.log(`Updated age to ${age}`);