const names: string[] = [
    'Freddy Krueger',
    'Jason',
    'Michael Myers',
    'Chucky',
    'Carrie',
    'Pennywise',
    'Dracula',
    'Nosferatu',
];

function getRandomElement<T>(array: T[]): T {
    const index = Math.floor(Math.random() * array.length);
    return array[index];
}

function generateName(): string {
    const name = getRandomElement(names);
    return `${name}`;
}

console.log('Your character is:', generateName());
