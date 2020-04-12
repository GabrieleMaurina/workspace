var b = Buffer.from([1, 0, 1, 0])
console.log(b)

var int16BE = (buf) => {
	var arr = []
	for(var i = 0; i < buf.length; i += 2){
		arr.push(buf.readInt16BE(i))
	}
	return arr
}

var int16LE = (buf) => {
	var arr = []
	for(var i = 0; i < buf.length; i += 2){
		arr.push(buf.readInt16LE(i))
	}
	return arr
}

console.log(int16BE(b))
console.log(int16LE(b))