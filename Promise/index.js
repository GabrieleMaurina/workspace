var Promise = require('promise');

new Promise((res, rej) => {
	res();
}).then(() => {
	console.log(1);
	return new Promise((res, rej) => {
		setTimeout(() => {
			console.log(2);
			res();
		}, 200);
	});
}).then(() => {
	console.log(3);
});