const { spawn } = require('child_process');

for (let i = 1; i <= 3; i++) {
    const fileName = `test_${i}.js`;
    const childProcess = spawn('node', [fileName]);

    childProcess.stdout.on('data', (data) => {
        console.log('output ', data.toString())
    })
    childProcess.stderr.on('data', (data) => {
        console.log('Error ', data)
    })
    childProcess.on('close', (data) => {
        console.log('Child process exited ', data)
    })
}