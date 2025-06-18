import  { readFile, writeFile } from 'fs/promises';

try {
    let data1 = await readFile('./assets/file1.txt', 'utf8');
    let data2 = await readFile('./assets/file2.txt', 'utf8');
    await writeFile('./assets/file3.txt', `${data1} ${data2}`);
}
catch (err) {
    console.log('something is wrong')
}