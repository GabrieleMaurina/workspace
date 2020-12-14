const proc = require('child_process').spawn('python', ['python.py'], ['pipe', 'pipe','pipe'])

proc.stdout.on('data', (data) => {
  process.stdout.write(data.toString())
})

proc.stderr.on('data', (data) => {
  process.stdout.write(data.toString())
})

proc.on('exit', () => {
  process.exit()
})

var string = ''
for(var i = 0; i < 100000; i++){
  string += i + ' '
}
proc.stdin.write(string + '\n')
