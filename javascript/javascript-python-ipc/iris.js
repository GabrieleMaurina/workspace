const process = require('child_process').spawn('python', ['iris.py'], ['pipe', 'pipe','pipe'])

process.stdout.on('data', (data) => {
  process.stdin.write(data)
  console.log(data.toString())
})


setTimeout(() => {
  console.log('Exiting..')
}, 5000)
